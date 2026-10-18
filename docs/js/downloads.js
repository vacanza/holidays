function holidayDownloads() {
  const currentYear = new Date().getFullYear();
  const PREVIEW_LIMIT = 200;

  return {
    // State
    isLoading: true,
    isListing: false,
    manifest: {},
    fetchMode: null,
    remoteBaseUrl: 'https://vacanza.github.io/holidays/downloads/',
    requestGeneration: 0,

    // Selection
    type: 'countries',
    selectedEntities: [],
    selectedSubdiv: 'ALL',
    selectedLang: 'default',
    selectedCategories: ['public'],
    entitySearch: '',

    // Results
    showCalendarList: false,
    calendarRows: [],
    showPreview: false,
    previewRows: [],
    previewTotal: 0,            // events actually shown
    previewAvailableTotal: 0,   // events available before the cap
    previewRegionCount: 0,      // regions shown in the preview
    previewAvailableRegions: 0, // regions available before the cap
    previewTruncated: false,

    // Year range
    startYear: currentYear,
    endYear: currentYear,
    allYears: Array.from({ length: 21 }, (_, i) => 2015 + i),

    async init() {
      try {
        const localResponse = await fetch('ics/index.json');
        if (!localResponse.ok) throw new Error('Local manifest missing');
        this.manifest = await localResponse.json();
        this.fetchMode = 'local';
      } catch (e) {
        try {
          const remoteResponse = await fetch(this.remoteBaseUrl + 'ics/index.json');
          if (!remoteResponse.ok) throw new Error('Remote manifest failed');
          this.manifest = await remoteResponse.json();
          this.fetchMode = 'remote';
        } catch (remoteError) {
          console.error('Failed to load manifest', remoteError);
          this.manifest = { countries: {}, financial: {} };
        }
      } finally {
        this.isLoading = false;
      }
    },

    // --- Paths and fetching ---

    _getRelativePath(entity, category, ext) {
      const language = this._getLanguage(entity);
      const subdiv =
        this.selectedEntities.length === 1 && this.selectedEntities[0] === entity
          ? this.selectedSubdiv
          : 'ALL';
      return `ics/${this.type}/${entity}/${subdiv}_${language}_${category}.${ext}`;
    },

    _fetchFile(path, options = {}) {
      const url = this.fetchMode === 'remote' ? this.remoteBaseUrl + path : path;
      return fetch(url, options);
    },

    // --- Computed ---

    get currentManifest() {
      return this.manifest[this.type] || {};
    },

    get filteredManifest() {
      const query = this.entitySearch.trim().toLowerCase();
      if (!query) return this.currentManifest;

      return Object.fromEntries(
        Object.entries(this.currentManifest).filter(([code, data]) =>
          code.toLowerCase().includes(query) ||
          String(data?.name || '').toLowerCase().includes(query)
        )
      );
    },

    get availableMultiCategories() {
      const categories = new Set();
      this.selectedEntities.forEach(entity => {
        const data = this.currentManifest[entity] || {};
        (data.categories || ['public']).forEach(category => categories.add(category));
      });
      return [...categories].sort((a, b) => a.localeCompare(b));
    },

    get availableLanguages() {
      const languages = new Map();
      this.selectedEntities.forEach(entity => {
        const data = this.currentManifest[entity] || {};
        Object.entries(data.languages || {}).forEach(([code, name]) => {
          if (!languages.has(code)) languages.set(code, name);
        });
      });
      return [...languages.entries()]
        .map(([code, name]) => ({ code, name }))
        .sort((a, b) => a.name.localeCompare(b.name));
    },

    get availableSubdivisions() {
      if (this.selectedEntities.length !== 1) return [];

      const data = this.currentManifest[this.selectedEntities[0]] || {};
      const subs = data.subdivisions || {};

      const subdivisions = Object.entries(subs)
        .map(([code, name]) => ({ code, name }))
        .sort((a, b) => a.name.localeCompare(b.name));

      return [{ code: 'ALL', name: 'Entire Country' }, ...subdivisions];
    },

    get showSubdivisionPicker() {
      return this.selectedEntities.length === 1 &&
             this.availableSubdivisions.length > 1;
    },

    // --- Helpers ---

    formatLabel(str) {
      if (!str) return '';
      return str.charAt(0).toUpperCase() + str.slice(1).replaceAll('_', ' ');
    },

    _getLanguage(entity) {
      const data = this.currentManifest[entity] || {};
      const languages = data.languages || {};

      if (this.selectedLang !== 'default' && languages[this.selectedLang]) {
        return this.selectedLang;
      }

      return data.default_language || Object.keys(languages)[0] || 'en_US';
    },

    _getLanguageName(entity, languageCode) {
      const data = this.currentManifest[entity] || {};
      return data.languages?.[languageCode] || languageCode;
    },

    _getWebcalUrl(entity, category) {
      const path = this._getRelativePath(entity, category, 'ics');
      const url = this.remoteBaseUrl + path;
      return url.replace(/^https?:\/\//, 'webcal://');
    },

    // --- Selection ---

    toggleEntity(code) {
      if (this.selectedEntities.includes(code)) {
        this.selectedEntities = this.selectedEntities.filter(entity => entity !== code);
      } else {
        this.selectedEntities = [...this.selectedEntities, code];
      }
      this.selectedSubdiv = 'ALL';
      this._syncCategories();
      this._refreshOrReset();
    },

    selectAllVisibleEntities() {
      const visibleCodes = Object.keys(this.filteredManifest);
      this.selectedEntities = [...new Set([...this.selectedEntities, ...visibleCodes])];
      this.selectedSubdiv = 'ALL';
      this._syncCategories();
      this._refreshOrReset();
    },

    clearEntitySelection() {
      this.selectedEntities = [];
      this.selectedCategories = ['public'];
      this.selectedSubdiv = 'ALL';
      this._resetResults();
    },

    toggleCategory(category) {
      if (this.selectedCategories.includes(category)) {
        this.selectedCategories = this.selectedCategories.filter(cat => cat !== category);
      } else {
        this.selectedCategories = [...this.selectedCategories, category];
      }
      this._refreshOrReset();
    },

    _syncCategories() {
      const available = this.availableMultiCategories;
      this.selectedCategories = this.selectedCategories.filter(c => available.includes(c));

      if (this.selectedCategories.length === 0 && available.length > 0) {
        this.selectedCategories = [available.includes('public') ? 'public' : available[0]];
      }
    },

    _resetResults() {
      this.requestGeneration++;
      this.isListing = false;
      this.calendarRows = [];
      this.previewRows = [];
      this.previewTotal = 0;
      this.previewAvailableTotal = 0;
      this.previewRegionCount = 0;
      this.previewAvailableRegions = 0;
      this.previewTruncated = false;
      this.showCalendarList = false;
      this.showPreview = false;
    },

    _refreshOrReset() {
      const hasResults = this.showCalendarList || this.showPreview;
      const hasSelection =
        this.selectedEntities.length > 0 && this.selectedCategories.length > 0;

      if (hasResults && hasSelection) {
        void this.listCalendars();
      } else {
        this._resetResults();
      }
    },

    updateType() {
      this.selectedEntities = [];
      this.selectedCategories = ['public'];
      this.selectedSubdiv = 'ALL';
      this.selectedLang = 'default';
      this.entitySearch = '';
      this._resetResults();
    },

    setRange(range) {
      const ranges = {
        current: [currentYear, currentYear],
        next3: [currentYear, Math.min(currentYear + 3, 2035)],
        all: [2015, 2035]
      };
      [this.startYear, this.endYear] = ranges[range] || [currentYear, currentYear];
      this.validateYears();
    },

    validateYears() {
      if (this.startYear > this.endYear) this.endYear = this.startYear;
      this._resetResults();
    },

    // --- Preview ---

    _filterEventsByYearRange(events, startYear, endYear) {
      return (events || []).filter(event => {
        const year = Number.parseInt(String(event.date).slice(0, 4), 10);
        return year >= startYear && year <= endYear;
      });
    },

    // Flatten events into single-root rows for Alpine's x-for.
    _buildPreviewRows(events) {
      const grouped = {};

      events.forEach(event => {
        const region = event._entity || 'Unknown';
        const year = String(event.date).slice(0, 4);

        if (!grouped[region]) grouped[region] = {};
        if (!grouped[region][year]) grouped[region][year] = [];
        grouped[region][year].push(event);
      });

      const rows = [];

      Object.keys(grouped).sort((a, b) => a.localeCompare(b)).forEach(region => {
        rows.push({ type: 'region', label: region });

        Object.keys(grouped[region]).sort((a, b) => a.localeCompare(b)).forEach(year => {
          rows.push({ type: 'year', label: year });

          grouped[region][year]
            .slice()
            .sort((a, b) => a.date.localeCompare(b.date))
            .forEach(event => {
              rows.push({ type: 'holiday', date: event.date, name: event.name });
            });
        });
      });

      return rows;
    },

    // Take whole regions in alphabetical order until we hit the hard limit.
    // A region is never split unless it alone exceeds the limit, in which
    // case we take only the first `limit` events from that region.
    _limitByRegion(events, limit) {
      const byRegion = new Map();

      events.forEach(event => {
        const region = event._entity || 'Unknown';
        if (!byRegion.has(region)) byRegion.set(region, []);
        byRegion.get(region).push(event);
      });

      const sortedRegions = [...byRegion.keys()].sort((a, b) => a.localeCompare(b));
      const kept = [];
      let truncated = false;

      for (const region of sortedRegions) {
        const regionEvents = byRegion.get(region);
        const remaining = limit - kept.length;

        if (remaining <= 0) {
          truncated = true;
          break;
        }

        if (regionEvents.length <= remaining) {
          kept.push(...regionEvents);
        } else {
          if (kept.length === 0) {
            kept.push(...regionEvents.slice(0, remaining));
          }
          truncated = true;
          break;
        }
      }

      return { events: kept, truncated };
    },

    async loadPreview(gen = ++this.requestGeneration) {
      if (!this.selectedEntities.length || !this.selectedCategories.length) {
        this._resetResults();
        return new Set();
      }

      const pairsWithEvents = new Set();
      const fetchPromises = [];

      for (const entity of this.selectedEntities) {
        const entityLabel = this._getEntityLabel(entity);
        const data = this.currentManifest[entity] || {};
        const supported = data.categories || ['public'];

        for (const category of this.selectedCategories) {
          if (!supported.includes(category)) continue;

          fetchPromises.push(
            this._fetchCategoryEvents(
              entity,
              category,
              entityLabel,
              gen,
              pairsWithEvents
            )
          );
        }
      }

      const results = await Promise.all(fetchPromises);
      if (this.requestGeneration !== gen) return new Set();

      const allEvents = results.flat();

      const deduped = this._dedupeEvents(allEvents);
      const availableRegions = new Set(deduped.map(e => e._entity));
      const { events, truncated } = this._limitByRegion(deduped, PREVIEW_LIMIT);

      if (this.requestGeneration !== gen) return new Set();

      this.previewAvailableTotal = deduped.length;
      this.previewAvailableRegions = availableRegions.size;
      this.previewTotal = events.length;
      this.previewRegionCount = new Set(events.map(e => e._entity)).size;
      this.previewTruncated = truncated;
      this.previewRows = this._buildPreviewRows(events);
      this.showPreview = this.previewRows.length > 0;

      return pairsWithEvents;
    },

    _getEntityLabel(entity) {
      const data = this.currentManifest[entity] || {};
      const subdivName = data.subdivisions?.[this.selectedSubdiv];
      const subdivLabel =
        this.selectedEntities.length === 1 && this.selectedSubdiv !== 'ALL' && subdivName
          ? ` - ${subdivName}`
          : '';
      return (data.name || entity) + subdivLabel;
    },

    async _fetchCategoryEvents(entity, category, entityLabel, gen, pairsWithEvents) {
      try {
        const path = this._getRelativePath(entity, category, 'json');
        const response = await this._fetchFile(path);
        if (this.requestGeneration !== gen || !response.ok) return [];

        const events = await response.json();
        if (this.requestGeneration !== gen) return [];
        const filtered = this._filterEventsByYearRange(events, this.startYear, this.endYear);

        if (filtered.length > 0) {
          pairsWithEvents.add(`${entity}|${category}`);
        }

        filtered.forEach(event => {
          event._entity = entityLabel;
        });

        return filtered;
      } catch (e) {
        if (this.requestGeneration !== gen) return [];
        console.warn(`Could not load preview for ${entity}/${category}`, e);
        return [];
      }
    },

    _dedupeEvents(events) {
      const seen = new Set();
      const deduped = [];
      for (const event of events) {
        const key = `${event._entity}|${event.date}|${event.name}`;
        if (!seen.has(key)) {
          seen.add(key);
          deduped.push(event);
        }
      }
      return deduped.sort((a, b) => a.date.localeCompare(b.date));
    },

    // --- Downloads ---

    async listCalendars() {
      if (!this.selectedEntities.length || !this.selectedCategories.length) {
        this._resetResults();
        return;
      }

      const gen = ++this.requestGeneration;
      this.isListing = true;

      try {
        const pairsWithEvents = await this.loadPreview(gen);
        if (this.requestGeneration !== gen) return;

        this.calendarRows = this.selectedEntities.map(entity => {
          const data = this.currentManifest[entity] || {};
          const language = this._getLanguage(entity);
          const supported = data.categories || ['public'];

          return {
            entity,
            name: this._getEntityLabel(entity),
            languageName: this._getLanguageName(entity, language),
            calendars: this.selectedCategories.map(category => {
              const hasEvents =
                supported.includes(category) &&
                pairsWithEvents.has(`${entity}|${category}`);
              return {
                category,
                available: hasEvents,
                icsDownloading: false,
                jsonDownloading: false,
                error: false,
                webcal: hasEvents ? this._getWebcalUrl(entity, category) : ''
              };
            })
          };
        });

        this.showCalendarList = true;
      } finally {
        if (this.requestGeneration === gen) {
          this.isListing = false;
        }
      }
    },

    async downloadCalendar(entity, category, format) {
      const row = this.calendarRows.find(r => r.entity === entity);
      const cell = row?.calendars.find(c => c.category === category);
      if (!cell?.available) return;

      const flagKey = format === 'json' ? 'jsonDownloading' : 'icsDownloading';
      cell[flagKey] = true;
      cell.error = false;

      try {
        const path = this._getRelativePath(entity, category, format);
        const response = await this._fetchFile(path);
        if (!response.ok) throw new Error(`Failed to fetch ${format} file`);

        const filename = this._getDownloadFilename(entity, category, format);

        if (format === 'json') {
          const events = await response.json();
          const filtered = this._filterEventsByYearRange(events, this.startYear, this.endYear);
          this._triggerDownload(JSON.stringify(filtered, null, 2), filename, 'application/json');
        } else {
          const text = await response.text();
          const filtered = this._filterIcsByYearRange(text, this.startYear, this.endYear);
          this._triggerDownload(filtered, filename, 'text/calendar');
        }
      } catch (e) {
        console.error('Failed to generate calendar download', e);
        cell.error = true;
      } finally {
        cell[flagKey] = false;
      }
    },

    _getDownloadFilename(entity, category, format) {
      const data = this.currentManifest[entity] || {};
      const name = (data.name || entity).replaceAll(/\s+/g, '-');
      const subdiv =
        this.selectedEntities.length === 1 &&
        this.selectedEntities[0] === entity &&
        this.selectedSubdiv !== 'ALL'
          ? `-${this.selectedSubdiv}`
          : '';
      const yearLabel =
        this.startYear === this.endYear
          ? `${this.startYear}`
          : `${this.startYear}-${this.endYear}`;
      return `${name}${subdiv}-${category}-${yearLabel}.${format}`;
    },

    _filterIcsByYearRange(icsText, startYear, endYear) {
      const [header, ...chunks] = icsText.split('BEGIN:VEVENT');
      if (chunks.length === 0) return icsText;

      let footer = '';
      const kept = [];

      chunks.forEach((chunk, index) => {
        const endIndex = chunk.indexOf('END:VEVENT');
        if (endIndex === -1) return;

        const body = chunk.slice(0, endIndex);
        const isLast = index === chunks.length - 1;
        let tail = chunk.slice(endIndex);

        if (isLast) {
          const footerIndex = tail.indexOf('END:VCALENDAR');
          if (footerIndex !== -1) {
            footer = tail.slice(footerIndex);
            tail = tail.slice(0, footerIndex);
          }
        }

        const match = body.match(/DTSTART[^:\r\n]*:(\d{4})/);
        const year = match ? Number.parseInt(match[1], 10) : null;

        if (year !== null && year >= startYear && year <= endYear) {
          kept.push('BEGIN:VEVENT' + body + tail);
        }
      });

      return header + kept.join('') + footer;
    },

    _triggerDownload(content, filename, mimeType) {
      const blob = new Blob([content], { type: mimeType });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.download = filename;
      document.body.appendChild(link);
      link.click();
      link.remove();
      URL.revokeObjectURL(url);
    }
  };
}
