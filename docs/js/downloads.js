function holidayDownloads() {
  const currentYear = new Date().getFullYear();

  return {
    // State
    isLoading: true,
    manifest: {},
    fetchMode: null,
    remoteBaseUrl: 'https://vacanza.github.io/holidays/downloads/',

    // User Selection
    type: 'countries',
    selectedEntities: [],
    selectedSubdiv: 'ALL',
    selectedLang: 'default',
    selectedCategories: ['public'],
    entitySearch: '',

    // Calendar list state
    showCalendarList: false,
    calendarRows: [],

    // Preview state
    showPreview: false,
    previewData: [],
    previewRows: [],

    // Year Range
    startYear: currentYear,
    endYear: currentYear,
    allYears: Array.from({ length: 21 }, (_, i) => 2015 + i),

    // Initialize
    async init() {
      try {
        try {
          const localResponse = await fetch('ics/index.json');
          if (!localResponse.ok) throw new Error('Local missing');
          this.manifest = await localResponse.json();
          this.fetchMode = 'local';
        } catch (e) {
          const remoteResponse = await fetch(this.remoteBaseUrl + 'ics/index.json');
          if (!remoteResponse.ok) throw new Error('Remote failed');
          this.manifest = await remoteResponse.json();
          this.fetchMode = 'remote';
        }
      } catch (e) {
        console.error('Failed to load data', e);
        this.manifest = { countries: {}, financial: {} };
      } finally {
        this.isLoading = false;
      }
    },

    // Helpers
    formatLabel(str) {
      if (!str) return '';
      return str.charAt(0).toUpperCase() + str.slice(1).replace(/_/g, ' ');
    },

    _getPath(entity, subdiv, lang, cat, ext) {
      return `ics/${this.type}/${entity}/${subdiv}_${lang}_${cat}.${ext}`;
    },

    async _fetchFile(path, options = {}) {
      if (this.fetchMode === 'remote') {
        return fetch(this.remoteBaseUrl + path, options);
      }
      if (this.fetchMode === 'local') {
        return fetch(path, options);
      }
      try {
        const response = await fetch(path, options);
        if (response.ok) return response;
        throw new Error('Local file not found');
      } catch (e) {
        if (e.name === 'AbortError') throw e;
        return fetch(this.remoteBaseUrl + path, options);
      }
    },

    // Computed
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

    get selectedEntityData() {
      return this.selectedEntities.map(entity => ({
        code: entity,
        data: this.currentManifest[entity] || {}
      }));
    },

    get availableMultiCategories() {
      const categories = new Set();
      this.selectedEntities.forEach(entity => {
        const data = this.currentManifest[entity] || {};
        (data.categories || ['public']).forEach(category => {
          categories.add(category);
        });
      });
      return [...categories].sort();
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

    // Subdivisions - only relevant when exactly one country is selected.
    // The manifest can expose these in several shapes; we handle all known
    // variants and always ensure an "Entire Country" (ALL) option is present.
    get availableSubdivisions() {
      if (this.selectedEntities.length !== 1) return [];
      const entity = this.selectedEntities[0];
      const data = this.currentManifest[entity] || {};
      const manifest = this.currentManifest;

      let subs = [];

      // Variant 1: nested map { "ALL": "...", "AU-NSW": "New South Wales" }
      if (data.subdivisions && !Array.isArray(data.subdivisions)) {
        subs = Object.entries(data.subdivisions).map(([code, name]) => ({
          code,
          name: typeof name === 'string' ? name : (name?.name || code)
        }));
      }
      // Variant 2: nested array [ { code, name }, ... ]
      else if (Array.isArray(data.subdivisions)) {
        subs = data.subdivisions.map(sub => ({
          code: sub.code || sub.id || sub.value,
          name: sub.name || sub.label || sub.code
        }));
      }
      // Variant 3: sibling top-level entries with a `parent` field
      else {
        const siblings = Object.entries(manifest).filter(([code, entry]) => {
          if (code === entity) return false;
          const parent = entry?.parent || entry?.country || entry?.parent_code;
          return parent === entity;
        });
        subs = siblings
          .sort(([a], [b]) => a.localeCompare(b))
          .map(([code, entry]) => ({
            code,
            name: entry?.name || entry?.subdivision_name || code
          }));
      }

      // Always ensure "Entire Country" (ALL) is present.
      if (!subs.some(sub => sub.code === 'ALL')) {
        subs.unshift({ code: 'ALL', name: 'Entire Country' });
      }

      // Keep ALL first, sort the rest alphabetically by name.
      const allOption = subs.find(sub => sub.code === 'ALL');
      const rest = subs
        .filter(sub => sub.code !== 'ALL')
        .sort((a, b) => a.name.localeCompare(b.name));

      return [allOption, ...rest];
    },

    get showSubdivisionPicker() {
      return this.selectedEntities.length === 1 &&
             this.availableSubdivisions.length > 1;
    },

    get regionCount() {
      return this.previewRows.filter(row => row.type === 'region').length;
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

    _getCalendarUrl(entity, category, ext) {
      const path = this._getRelativePath(entity, category, ext);
      return this.fetchMode === 'remote' ? this.remoteBaseUrl + path : path;
    },

    // Relative path - uses the selected subdivision when this entity is
    // the currently-selected single country, otherwise falls back to ALL.
    _getRelativePath(entity, category, ext) {
      const language = this._getLanguage(entity);
      const subdiv =
        this.selectedEntities.length === 1 && this.selectedEntities[0] === entity
          ? this.selectedSubdiv
          : 'ALL';
      return this._getPath(entity, subdiv, language, category, ext);
    },

    _getWebcalUrl(entity, category) {
      return this._getCalendarUrl(entity, category, 'ics').replace(/^https?:\/\//, 'webcal://');
    },

    // Entity Selection
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

    _syncCategories() {
      const available = this.availableMultiCategories;
      this.selectedCategories = this.selectedCategories.filter(
        category => available.includes(category)
      );
      if (this.selectedCategories.length === 0 && available.length > 0) {
        this.selectedCategories = [available[0]];
      }
    },

    _resetResults() {
      this.calendarRows = [];
      this.previewData = [];
      this.previewRows = [];
      this.showCalendarList = false;
      this.showPreview = false;
    },

    // If the preview is already showing, refresh it; otherwise just clear.
    _refreshOrReset() {
      if ((this.showCalendarList || this.showPreview) &&
          this.selectedEntities.length > 0 &&
          this.selectedCategories.length > 0) {
        this.listCalendars();
      } else {
        this._resetResults();
      }
    },

    // Category Selection
    toggleCategory(category) {
      if (this.selectedCategories.includes(category)) {
        this.selectedCategories = this.selectedCategories.filter(cat => cat !== category);
      } else {
        this.selectedCategories = [...this.selectedCategories, category];
      }
      this._refreshOrReset();
    },

    selectAllCategories() {
      this.selectedCategories = [...this.availableMultiCategories];
      this._refreshOrReset();
    },

    // Year-scoped downloads
    async downloadCalendar(entity, category, format) {
      const row = this.calendarRows.find(r => r.entity === entity);
      const cell = row?.calendars.find(c => c.category === category);
      if (!cell || !cell.available) return;

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
          const icsText = await response.text();
          const filtered = this._filterIcsByYearRange(icsText, this.startYear, this.endYear);
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
      const name = (data.name || entity).replace(/\s+/g, '-');
      const subdiv =
        this.selectedEntities.length === 1 &&
        this.selectedEntities[0] === entity &&
        this.selectedSubdiv !== 'ALL'
          ? `-${this.selectedSubdiv}`
          : '';
      const yearLabel = this.startYear === this.endYear
        ? `${this.startYear}`
        : `${this.startYear}-${this.endYear}`;
      return `${name}${subdiv}-${category}-${yearLabel}.${format}`;
    },

    _filterEventsByYearRange(events, startYear, endYear) {
      return (events || []).filter(event => {
        const year = parseInt(String(event.date).slice(0, 4), 10);
        return year >= startYear && year <= endYear;
      });
    },

    _filterIcsByYearRange(icsText, startYear, endYear) {
      const [header, ...eventChunks] = icsText.split('BEGIN:VEVENT');
      if (eventChunks.length === 0) return icsText;

      let footer = '';
      const keptBlocks = [];

      eventChunks.forEach((chunk, index) => {
        const endIndex = chunk.indexOf('END:VEVENT');
        if (endIndex === -1) return;

        const eventBody = chunk.slice(0, endIndex);
        const isLast = index === eventChunks.length - 1;
        let tail = chunk.slice(endIndex);

        if (isLast) {
          const footerIndex = tail.indexOf('END:VCALENDAR');
          if (footerIndex !== -1) {
            footer = tail.slice(footerIndex);
            tail = tail.slice(0, footerIndex);
          }
        }

        const dtstartMatch = eventBody.match(/DTSTART[^:\r\n]*:(\d{4})/);
        const year = dtstartMatch ? parseInt(dtstartMatch[1], 10) : null;

        if (year !== null && year >= startYear && year <= endYear) {
          keptBlocks.push('BEGIN:VEVENT' + eventBody + tail);
        }
      });

      return header + keptBlocks.join('') + footer;
    },

    _triggerDownload(content, filename, mimeType) {
      const blob = new Blob([content], { type: mimeType });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.download = filename;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      URL.revokeObjectURL(url);
    },

    // Build flat rows for the preview table. Each row is one of:
    // { type: 'region' }, { type: 'year' }, or { type: 'holiday' }.
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

      Object.keys(grouped).sort().forEach(region => {
        rows.push({ type: 'region', label: region });

        Object.keys(grouped[region])
          .sort((a, b) => a.localeCompare(b))
          .forEach(year => {
            rows.push({ type: 'year', label: year });

            grouped[region][year]
              .slice()
              .sort((a, b) => a.date.localeCompare(b.date))
              .forEach(event => {
                rows.push({
                  type: 'holiday',
                  date: event.date,
                  name: event.name
                });
              });
          });
      });

      return rows;
    },

    // Load Preview Data - fetches ALL selected categories for ALL selected entities.
    async loadPreview() {
      if (this.selectedEntities.length === 0 || this.selectedCategories.length === 0) {
        this.previewData = [];
        this.previewRows = [];
        this.showPreview = false;
        return;
      }

      const allEvents = [];

      for (const entity of this.selectedEntities) {
        const data = this.currentManifest[entity] || {};
        const baseName = data.name || entity;

        // Include subdivision name in the region label when one is selected.
        const subdivLabel =
          this.selectedEntities.length === 1 &&
          this.selectedSubdiv !== 'ALL' &&
          data.subdivisions &&
          data.subdivisions[this.selectedSubdiv]
            ? ` - ${data.subdivisions[this.selectedSubdiv]}`
            : '';
        const entityName = baseName + subdivLabel;

        for (const category of this.selectedCategories) {
          try {
            const path = this._getRelativePath(entity, category, 'json');
            const response = await this._fetchFile(path);

            if (!response.ok) continue;

            const events = await response.json();
            const filtered = this._filterEventsByYearRange(events, this.startYear, this.endYear);

            filtered.forEach(event => {
              event._entity = entityName;
              event._category = category;
            });

            allEvents.push(...filtered);
          } catch (e) {
            console.warn(`Could not load preview for ${entity}/${category}`, e);
          }
        }
      }

      // Deduplicate events that appear in multiple categories.
      const seen = new Set();
      const deduped = [];
      for (const event of allEvents) {
        const key = `${event._entity}|${event.date}|${event.name}`;
        if (!seen.has(key)) {
          seen.add(key);
          deduped.push(event);
        }
      }

      deduped.sort((a, b) => a.date.localeCompare(b.date));

      this.previewData = deduped.slice(0, 200);
      this.previewRows = this._buildPreviewRows(this.previewData);
      this.showPreview = this.previewRows.length > 0;
    },

    // Calendar Table
    async listCalendars() {
      if (!this.selectedEntities.length || !this.selectedCategories.length) {
        this._resetResults();
        return;
      }

      await this.loadPreview();

      this.calendarRows = this.selectedEntities.map(entity => {
        const data = this.currentManifest[entity] || {};
        const language = this._getLanguage(entity);
        const supportedCategories = data.categories || ['public'];

        // Append subdivision to the display name when applicable.
        const subdivLabel =
          this.selectedEntities.length === 1 &&
          this.selectedSubdiv !== 'ALL' &&
          data.subdivisions &&
          data.subdivisions[this.selectedSubdiv]
            ? ` - ${data.subdivisions[this.selectedSubdiv]}`
            : '';

        return {
          entity,
          name: (data.name || entity) + subdivLabel,
          language,
          languageName: this._getLanguageName(entity, language),
          calendars: this.selectedCategories.map(category => {
            const available = supportedCategories.includes(category);
            return {
              category,
              available,
              icsDownloading: false,
              jsonDownloading: false,
              error: false,
              webcal: available ? this._getWebcalUrl(entity, category) : ''
            };
          })
        };
      });

      this.showCalendarList = true;
    },

    // Controls
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
    }
  };
}
