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

    // Year Range
    startYear: currentYear,
    endYear: currentYear,
    allYears: Array.from({ length: 21 }, (_, i) => 2015 + i),

    // Initialize
    async init() {
      console.log('Initializing holiday downloads...');

      try {
        // Try local first
        try {
          const localResponse = await fetch('ics/index.json');
          if (!localResponse.ok) throw new Error('Local missing');
          this.manifest = await localResponse.json();
          this.fetchMode = 'local';
          console.log('Loaded from local');
        } catch (e) {
          console.log('Local not found, trying remote...');
          const remoteResponse = await fetch(this.remoteBaseUrl + 'ics/index.json');
          if (!remoteResponse.ok) throw new Error('Remote failed');
          this.manifest = await remoteResponse.json();
          this.fetchMode = 'remote';
          console.log('Loaded from remote');
        }
      } catch (e) {
        console.error('Failed to load data', e);
        this.manifest = { countries: {}, financial: {} };
      } finally {
        this.isLoading = false;
        console.log('Loading complete');
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

    _getRelativePath(entity, category, ext) {
      const language = this._getLanguage(entity);
      return this._getPath(entity, 'ALL', language, category, ext);
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
      this._syncCategories();
      this.showCalendarList = false;
      this.showPreview = false;
      this.calendarRows = [];
      this.previewData = [];
    },

    selectAllVisibleEntities() {
      const visibleCodes = Object.keys(this.filteredManifest);
      this.selectedEntities = [...new Set([...this.selectedEntities, ...visibleCodes])];
      this._syncCategories();
      this.showCalendarList = false;
      this.showPreview = false;
      this.calendarRows = [];
      this.previewData = [];
    },

    clearEntitySelection() {
      this.selectedEntities = [];
      this.selectedCategories = ['public'];
      this.calendarRows = [];
      this.previewData = [];
      this.showCalendarList = false;
      this.showPreview = false;
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

    // Category Selection
    toggleCategory(category) {
      if (this.selectedCategories.includes(category)) {
        this.selectedCategories = this.selectedCategories.filter(cat => cat !== category);
      } else {
        this.selectedCategories = [...this.selectedCategories, category];
      }
      this.showCalendarList = false;
      this.showPreview = false;
      this.calendarRows = [];
      this.previewData = [];
    },

    selectAllCategories() {
      this.selectedCategories = [...this.availableMultiCategories];
      this.showCalendarList = false;
      this.showPreview = false;
      this.calendarRows = [];
      this.previewData = [];
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
      const yearLabel = this.startYear === this.endYear ? `${this.startYear}` : `${this.startYear}-${this.endYear}`;
      return `${name}-${category}-${yearLabel}.${format}`;
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

    // Load Preview Data
    async loadPreview() {
      if (this.selectedEntities.length === 0 || this.selectedCategories.length === 0) {
        this.previewData = [];
        this.showPreview = false;
        return;
      }

      // Only show preview if one or more entities selected
      // For multiple entities, show combined preview
      const allEvents = [];

      for (const entity of this.selectedEntities) {
        try {
          const category = this.selectedCategories[0]; // Use first selected category
          const path = this._getRelativePath(entity, category, 'json');
          const response = await this._fetchFile(path);

          if (response.ok) {
            const events = await response.json();
            const filtered = this._filterEventsByYearRange(events, this.startYear, this.endYear);
            // Add entity name to each event for context
            const entityName = this.currentManifest[entity]?.name || entity;
            filtered.forEach(event => {
              event._entity = entityName;
            });
            allEvents.push(...filtered);
          }
        } catch (e) {
          console.warn(`Could not load preview for ${entity}`, e);
        }
      }

      // Sort by date
      allEvents.sort((a, b) => a.date.localeCompare(b.date));

      // Limit preview to first 100 events for performance
      this.previewData = allEvents.slice(0, 100);
      this.showPreview = this.previewData.length > 0;
    },

    // Calendar Table
    async listCalendars() {
      if (!this.selectedEntities.length || !this.selectedCategories.length) {
        this.calendarRows = [];
        this.showCalendarList = false;
        this.showPreview = false;
        this.previewData = [];
        return;
      }

      // Load preview data
      await this.loadPreview();

      // Build calendar rows
      this.calendarRows = this.selectedEntities.map(entity => {
        const data = this.currentManifest[entity] || {};
        const language = this._getLanguage(entity);
        const supportedCategories = data.categories || ['public'];

        return {
          entity,
          name: data.name || entity,
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
      this.selectedLang = 'default';
      this.entitySearch = '';
      this.calendarRows = [];
      this.previewData = [];
      this.showCalendarList = false;
      this.showPreview = false;
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
      this.showCalendarList = false;
      this.showPreview = false;
      this.calendarRows = [];
      this.previewData = [];
    }
  };
}