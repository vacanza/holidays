function holidayDownloads() {
    const currentYear = new Date().getFullYear();

    return {
        // Initial State Variables
        isLoading: true,
        manifest: {},
        fetchMode: null,
        remoteBaseUrl: 'https://vacanza.github.io/holidays/downloads/',

        // User Selection Configuration
        type: 'countries',
        selectedEntities: [],
        selectedSubdiv: 'ALL',
        selectedLang: 'default',
        selectedCategories: ['public'],
        entitySearch: '',

        // Calendar list state
        showCalendarList: false,
        calendarRows: [],

        // Year Range Configuration
        startYear: currentYear,
        endYear: currentYear,
        allYears: Array.from({ length: 21 }, (_, i) => 2015 + i),

        // Initialize Data Manifest
        async init() {
            try {
                try {
                    const localResponse = await fetch('ics/index.json');

                    if (!localResponse.ok) {
                        throw new Error('Local missing');
                    }

                    this.manifest = await localResponse.json();
                    this.fetchMode = 'local';
                } catch (e) {
                    const remoteResponse = await fetch(
                        this.remoteBaseUrl + 'ics/index.json'
                    );

                    this.manifest = await remoteResponse.json();
                    this.fetchMode = 'remote';
                }
            } catch (e) {
                console.error('Failed to load data', e);
            } finally {
                this.isLoading = false;
            }
        },

        // Formatting Helper Functions
        formatLabel(str) {
            if (!str) return '';
            return str.charAt(0).toUpperCase() +
                str.slice(1).replace(/_/g, ' ');
        },

        _getPath(entity, subdiv, lang, cat, ext) {
            return `ics/${this.type}/${entity}/${subdiv}_${lang}_${cat}.${ext}`;
        },

        // Fetch file based on active mode
        async _fetchFile(path, options = {}) {
            if (this.fetchMode === 'remote') {
                return fetch(this.remoteBaseUrl + path, options);
            }

            if (this.fetchMode === 'local') {
                return fetch(path, options);
            }

            try {
                const response = await fetch(path, options);

                if (response.ok) {
                    return response;
                }

                throw new Error('Local file not found');
            } catch (e) {
                if (e.name === 'AbortError') {
                    throw e;
                }

                return fetch(this.remoteBaseUrl + path, options);
            }
        },

        // Computed Data Getters
        get currentManifest() {
            return this.manifest[this.type] || {};
        },

        get filteredManifest() {
            const query = this.entitySearch.trim().toLowerCase();

            if (!query) {
                return this.currentManifest;
            }

            return Object.fromEntries(
                Object.entries(this.currentManifest).filter(([code, data]) =>
                    code.toLowerCase().includes(query) ||
                    String(data?.name || '')
                        .toLowerCase()
                        .includes(query)
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
                    if (!languages.has(code)) {
                        languages.set(code, name);
                    }
                });
            });

            return [...languages.entries()]
                .map(([code, name]) => ({ code, name }))
                .sort((a, b) => a.name.localeCompare(b.name));
        },

        // Get the language for an entity.
        // "default" means use the entity's default language.
        _getLanguage(entity) {
            const data = this.currentManifest[entity] || {};
            const languages = data.languages || {};

            if (
                this.selectedLang !== 'default' &&
                languages[this.selectedLang]
            ) {
                return this.selectedLang;
            }

            return (
                data.default_language ||
                Object.keys(languages)[0] ||
                'en_US'
            );
        },

        _getLanguageName(entity, languageCode) {
            const data = this.currentManifest[entity] || {};

            return data.languages?.[languageCode] || languageCode;
        },

        _getCalendarUrl(entity, category, ext) {
            const path = this._getRelativePath(entity, category, ext);

            return this.fetchMode === 'remote'
                ? this.remoteBaseUrl + path
                : path;
        },

        // Relative path (no base URL) for use with _fetchFile, which
        // already knows how to fall back between local and remote.
        _getRelativePath(entity, category, ext) {
            const language = this._getLanguage(entity);

            return this._getPath(
                entity,
                'ALL',
                language,
                category,
                ext
            );
        },

        _getWebcalUrl(entity, category) {
            return this
                ._getCalendarUrl(entity, category, 'ics')
                .replace(/^https?:\/\//, 'webcal://');
        },

        // -----------------------------
        // Entity Selection
        // -----------------------------

        toggleEntity(code) {
            if (this.selectedEntities.includes(code)) {
                this.selectedEntities =
                    this.selectedEntities.filter(
                        entity => entity !== code
                    );
            } else {
                this.selectedEntities = [
                    ...this.selectedEntities,
                    code
                ];
            }

            this._syncCategories();

            this.showCalendarList = false;
            this.calendarRows = [];
        },

        selectAllVisibleEntities() {
            const visibleCodes = Object.keys(
                this.filteredManifest
            );

            this.selectedEntities = [
                ...new Set([
                    ...this.selectedEntities,
                    ...visibleCodes
                ])
            ];

            this._syncCategories();

            this.showCalendarList = false;
            this.calendarRows = [];
        },

        clearEntitySelection() {
            this.selectedEntities = [];
            this.selectedCategories = ['public'];
            this.calendarRows = [];
            this.showCalendarList = false;
        },

        _syncCategories() {
            const available = this.availableMultiCategories;

            this.selectedCategories =
                this.selectedCategories.filter(
                    category => available.includes(category)
                );

            if (
                this.selectedCategories.length === 0 &&
                available.length > 0
            ) {
                this.selectedCategories = [available[0]];
            }
        },

        // -----------------------------
        // Category Selection
        // -----------------------------

        toggleCategory(category) {
            if (this.selectedCategories.includes(category)) {
                this.selectedCategories =
                    this.selectedCategories.filter(
                        cat => cat !== category
                    );
            } else {
                this.selectedCategories = [
                    ...this.selectedCategories,
                    category
                ];
            }

            this.showCalendarList = false;
            this.calendarRows = [];
        },

        selectAllCategories() {
            this.selectedCategories = [
                ...this.availableMultiCategories
            ];

            this.showCalendarList = false;
            this.calendarRows = [];
        },

        // -----------------------------
        // Year-scoped ICS/JSON downloads
        // -----------------------------

        // The static index files cover every year (2015-2035), so
        // to honor a custom year range we fetch the full file, trim
        // it down client-side, and hand the browser a generated Blob
        // instead of linking straight to the static file.
        async downloadCalendar(entity, category, format) {
            const row = this.calendarRows.find(r => r.entity === entity);
            const cell = row?.calendars.find(c => c.category === category);

            if (!cell || !cell.available) {
                return;
            }

            const flagKey = format === 'json' ? 'jsonDownloading' : 'icsDownloading';

            cell[flagKey] = true;
            cell.error = false;

            try {
                const path = this._getRelativePath(entity, category, format);
                const response = await this._fetchFile(path);

                if (!response.ok) {
                    throw new Error(`Failed to fetch ${format} file`);
                }

                const filename = this._getDownloadFilename(
                    entity,
                    category,
                    format
                );

                if (format === 'json') {
                    const events = await response.json();

                    const filtered = this._filterEventsByYearRange(
                        events,
                        this.startYear,
                        this.endYear
                    );

                    this._triggerDownload(
                        JSON.stringify(filtered, null, 2),
                        filename,
                        'application/json'
                    );
                } else {
                    const icsText = await response.text();

                    const filtered = this._filterIcsByYearRange(
                        icsText,
                        this.startYear,
                        this.endYear
                    );

                    this._triggerDownload(
                        filtered,
                        filename,
                        'text/calendar'
                    );
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

            const yearLabel =
                this.startYear === this.endYear
                    ? `${this.startYear}`
                    : `${this.startYear}-${this.endYear}`;

            return `${name}-${category}-${yearLabel}.${format}`;
        },

        // events: array of { date: 'YYYY-MM-DD', name: string }
        _filterEventsByYearRange(events, startYear, endYear) {
            return (events || []).filter(event => {
                const year = parseInt(String(event.date).slice(0, 4), 10);
                return year >= startYear && year <= endYear;
            });
        },

        // Keeps the VCALENDAR header/footer intact and drops any
        // VEVENT block whose DTSTART year falls outside the range.
        // Preserves each block's original trailing whitespace so
        // kept blocks stay correctly newline-separated when rejoined.
        _filterIcsByYearRange(icsText, startYear, endYear) {
            const [header, ...eventChunks] = icsText.split('BEGIN:VEVENT');

            if (eventChunks.length === 0) {
                return icsText;
            }

            let footer = '';
            const keptBlocks = [];

            eventChunks.forEach((chunk, index) => {
                const endIndex = chunk.indexOf('END:VEVENT');

                if (endIndex === -1) {
                    return;
                }

                const eventBody = chunk.slice(0, endIndex);
                const isLast = index === eventChunks.length - 1;

                // tail = 'END:VEVENT' + whatever trails it (a newline
                // before the next block, or, for the last block, a
                // newline followed by the VCALENDAR footer).
                let tail = chunk.slice(endIndex);

                if (isLast) {
                    const footerIndex = tail.indexOf('END:VCALENDAR');

                    if (footerIndex !== -1) {
                        footer = tail.slice(footerIndex);
                        tail = tail.slice(0, footerIndex);
                    }
                }

                const dtstartMatch = eventBody.match(
                    /DTSTART[^:\r\n]*:(\d{4})/
                );
                const year = dtstartMatch
                    ? parseInt(dtstartMatch[1], 10)
                    : null;

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

        // -----------------------------
        // Calendar Table
        // -----------------------------

        listCalendars() {
            if (
                !this.selectedEntities.length ||
                !this.selectedCategories.length
            ) {
                this.calendarRows = [];
                this.showCalendarList = false;
                return;
            }

            this.calendarRows = this.selectedEntities.map(entity => {
                const data =
                    this.currentManifest[entity] || {};

                const language = this._getLanguage(entity);

                const supportedCategories =
                    data.categories || ['public'];

                return {
                    entity,
                    name: data.name || entity,
                    language,
                    languageName:
                        this._getLanguageName(
                            entity,
                            language
                        ),

                    calendars:
                        this.selectedCategories.map(category => {
                            const available =
                                supportedCategories.includes(
                                    category
                                );

                            return {
                                category,
                                available,

                                // ICS/JSON are generated on click (see
                                // downloadCalendar) so they can be
                                // trimmed to the selected year range.
                                icsDownloading: false,
                                jsonDownloading: false,
                                error: false,

                                webcal: available
                                    ? this._getWebcalUrl(
                                          entity,
                                          category
                                      )
                                    : ''
                            };
                        })
                };
            });

            this.showCalendarList = true;
        },

        // -----------------------------
        // Existing Controls
        // -----------------------------

        updateType() {
            this.selectedEntities = [];
            this.selectedCategories = ['public'];
            this.selectedLang = 'default';
            this.entitySearch = '';
            this.calendarRows = [];
            this.showCalendarList = false;
        },

        setRange(range) {
            const ranges = {
                current: [
                    currentYear,
                    currentYear
                ],

                next3: [
                    currentYear,
                    Math.min(currentYear + 3, 2035)
                ],

                all: [
                    2015,
                    2035
                ]
            };

            [
                this.startYear,
                this.endYear
            ] = ranges[range] ||
                [currentYear, currentYear];

            this.validateYears();
        },

        validateYears() {
            if (this.startYear > this.endYear) {
                this.endYear = this.startYear;
            }

            this.showCalendarList = false;
            this.calendarRows = [];
        }
    };
}
