function holidayDownloads() {
    const currentYear = new Date().getFullYear();

    return {
        // Initial State Variables
        isLoading: true,
        isGenerating: false,
        manifest: {},
        previewYears: [],
        abortController: null,
        fetchMode: null,
        remoteBaseUrl: 'https://vacanza.github.io/holidays/downloads/',

        // User Selection Configuration
        type: 'countries',
        selectedEntity: '',
        selectedSubdiv: 'ALL',
        selectedLang: 'en_US',
        selectedCategory: 'public',

        // Year Range Configuration
        startYear: currentYear,
        endYear: currentYear,
        allYears: Array.from({ length: 21 }, (_, i) => 2015 + i),

        // Initialize Data Manifest
        async init() {
            try {
                try {
                    const localResponse = await fetch('ics/index.json');
                    if (!localResponse.ok) throw new Error('Local missing');
                    this.manifest = await localResponse.json();
                    this.fetchMode = 'local';
                } catch (e) {
                    const remoteResponse = await fetch(this.remoteBaseUrl + 'ics/index.json');
                    this.manifest = await remoteResponse.json();
                    this.fetchMode = 'remote';
                }
            } catch (e) {
                console.error("Failed to load data", e);
            } finally {
                this.isLoading = false;
            }
        },

        // Formatting Helper Functions
        formatLabel: (str) => str.charAt(0).toUpperCase() + str.slice(1).replace(/_/g, ' '),
        _getPath: function(cat, ext) {
            return `ics/${this.type}/${this.selectedEntity}/${this.selectedSubdiv}_${this.selectedLang}_${cat}.${ext}`;
        },

        // Fetch file based on active mode
        async _fetchFile(path, options = {}) {
            // Fast path: Use saved mode if initialized
            if (this.fetchMode === 'remote') return fetch(this.remoteBaseUrl + path, options);
            if (this.fetchMode === 'local') return fetch(path, options);

            // Safe path: Fallback during initial load
            try {
                const response = await fetch(path, options);
                if (response.ok) return response;
                throw new Error('Local file not found');
            } catch (e) {
                if (e.name === 'AbortError') throw e;
                return fetch(this.remoteBaseUrl + path, options);
            }
        },

        // Computed Data Getters

        get currentManifest() { return this.manifest[this.type] || {}; },
        get activeData() { return this.currentManifest[this.selectedEntity] || {}; },
        get hasSubdivisions() { return Object.keys(this.activeData?.subdivisions || {}).length > 0; },

        // Category and Subdivision Configuration
        get availableSubdivisions() {
            return Object.entries(this.activeData?.subdivisions || {}).map(([code, name]) => ({ code, name }));
        },
        get availableLanguages() {
            return Object.entries(this.activeData?.languages || { 'en_US': 'English (US)' }).map(([code, name]) => ({ code, name }));
        },
        get availableCategories() { return this.activeData?.categories || ['public']; },
        get selectableCategories() { return [...this.availableCategories, 'ALL']; },
        get categoriesToFetch() {
            return this.selectedCategory === 'ALL' ? this.availableCategories : [this.selectedCategory];
        },

        // Generate Download Filename
        get filename() {
            if (!this.selectedEntity) return '';

            const name = (this.activeData?.name || this.selectedEntity).replace(/ /g, '-');
            const sub = this.selectedSubdiv !== 'ALL' ? this.selectedSubdiv : '';
            const cat = this.selectedCategory === 'ALL' ? 'all' : this.selectedCategory;
            const years = this.startYear !== this.endYear ? `${this.startYear}-${this.endYear}` : this.startYear;

            return [name, sub, cat, years].filter(Boolean).join('-') + '.ics';
        },

        // Handle Type Updates
        updateType() {
            this.selectedEntity = '';
            this.previewYears = [];
        },

        // Handle Option Updates
        updateOptions() {
            this.selectedSubdiv = 'ALL';

            // Set default category
            this.selectedCategory = 'public';

            // Set default language
            this.selectedLang = 'en_US';

            this.startYear = currentYear;
            this.endYear = currentYear;

            this.updatePreview();
        },

        // Set Year Range Based on Selection
        setRange(range) {
            const ranges = {
                current: [currentYear, currentYear],
                next3:   [currentYear, Math.min(currentYear + 3, 2035)],
                all:     [2015, 2035]
            };

            [this.startYear, this.endYear] = ranges[range] || [currentYear, currentYear];
            this.validateYears();
        },

        // Validate Selected Years
        validateYears() {
            if (this.startYear > this.endYear) this.endYear = this.startYear;
            this.updatePreview();
        },

        // Update Preview Data
        async updatePreview() {
            if (!this.selectedEntity) return (this.previewYears = []);

            // Abort previous requests if a new one is triggered
            if (this.abortController) {
                this.abortController.abort();
            }
            this.abortController = new AbortController();
            const signal = this.abortController.signal;

            const categories = this.categoriesToFetch;
            const reqs = categories.map(cat =>
                this._fetchFile(this._getPath(cat, 'json'), { signal })
                    .then(r => r.ok ? r.json() : [])
                    .catch(e => {
                        if (e.name !== 'AbortError') return [];
                    })
            );

            const eventsList = await Promise.all(reqs);
            if (signal.aborted) return;

            const events = eventsList
                .flat()
                .filter(Boolean)
                .filter(event => {
                    const year = new Date(event.date || event.start).getFullYear();
                    return year >= this.startYear && year <= this.endYear;
                })
                .sort((a, b) => new Date(a.date || a.start || 0) - new Date(b.date || b.start || 0));

            const grouped = {};
            for (const event of events) {
                const year = new Date(event.date || event.start).getFullYear();

                if (!grouped[year]) {
                    grouped[year] = [];
                }
                grouped[year].push(event);
            }

            this.previewYears = Object.entries(grouped)
                .sort(([a], [b]) => Number(a) - Number(b))
                .map(([year, events]) => ({ year: Number(year), events }));
        },

        // Download ICS File
        async downloadICS() {
            this.isGenerating = true;
            const categories = this.categoriesToFetch;
            const fetches = categories.map(cat =>
                this._fetchFile(this._getPath(cat, 'ics')).then(r => r.ok ? r.text() : "").catch(() => "");
            );

            const results = await Promise.all(fetches);

            // Extract dynamic header or fallback to default
            const dynamicHeader = results.find(text => text)?.match(/^BEGIN:VCALENDAR[\s\S]*?(?=BEGIN:VEVENT)/i)?.[0].trim()
                || "BEGIN:VCALENDAR\r\nVERSION:2.0\r\nCALSCALE:GREGORIAN";

            // Combine events from all fetched files
            const combinedEvents = results
                .flatMap(text => text.match(/BEGIN:VEVENT[\s\S]*?END:VEVENT/gi) || [])
                .filter(eventText => {
                    const match =
                        eventText.match(/^DTSTART;VALUE=DATE:(\d{4})/m) ||
                        eventText.match(/^DTSTART:(\d{4})/m);

                    if (!match) return false;

                    const year = Number(match[1]);
                    return year >= this.startYear && year <= this.endYear;
                });

            if (combinedEvents.length === 0) {
                alert("No data found for the selected range.");
                this.isGenerating = false;
                return;
            }

            // Create and trigger file download
            const finalContent = [dynamicHeader, ...combinedEvents, "END:VCALENDAR"].join("\r\n");
            const url = URL.createObjectURL(new Blob([finalContent], { type: "text/calendar;charset=utf-8" }));

            Object.assign(document.createElement("a"), { href: url, download: this.filename }).click();

            // Cleanup
            URL.revokeObjectURL(url);
            this.isGenerating = false;
        }
    };
}
