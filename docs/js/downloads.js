function holidayDownloads() {
    const currentYear = new Date().getFullYear();

    return {
        // Initial State Variables
        isLoading: true,
        isGenerating: false,
        manifest: {},
        previewYears: [],
        abortController: null,

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
                const response = await fetch('ics/index.json');
                this.manifest = await response.json();
            } catch (e) {
                console.error("Failed to load data", e);
            } finally {
                this.isLoading = false;
            }
        },

        // Formatting Helper Functions
        formatLabel: (str) => str.charAt(0).toUpperCase() + str.slice(1).replace(/_/g, ' '),
        formatDate: (dateStr) => new Date(dateStr).toLocaleDateString(undefined, { year: 'numeric', month: 'short', day: 'numeric', weekday: 'short' }),
        _getPath: function(year, cat, ext) {
            return `ics/${this.type}/${this.selectedEntity}/${year}/${this.selectedSubdiv}_${this.selectedLang}_${cat}.${ext}`;
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
        get selectableCategories() { return ['ALL', ...this.availableCategories]; },
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
            this.selectedCategory = 'ALL';

            this.startYear = currentYear;
            this.endYear = currentYear;

            // Determine default language
            const langs = Object.keys(this.activeData?.languages || {});
            const defLang = this.activeData?.default_language || this.activeData?.defaultLanguage;

            this.selectedLang = (defLang && langs.includes(defLang)) ? defLang : (langs[0] || 'en_US');

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
            const promises = [];

            // Fetch data for each selected year
            for (let year = this.startYear; year <= this.endYear; year++) {
                const fetchYear = async () => {
                    const reqs = categories.map(cat =>
                        fetch(this._getPath(year, cat, 'json'), { signal })
                            .then(r => r.ok ? r.json() : [])
                            .catch(e => {
                                if (e.name !== 'AbortError') return []; // Ignore aborts gracefully
                            })
                    );

                    if (signal.aborted) return null;

                    const eventsList = await Promise.all(reqs);
                    if (signal.aborted) return null;

                    const events = eventsList
                        .flat()
                        .filter(Boolean)
                        .sort((a, b) => new Date(a.date || a.start || 0) - new Date(b.date || b.start || 0));

                    return events.length > 0 ? { year, events } : null;
                };
                promises.push(fetchYear());
            }

            const results = await Promise.all(promises);

            // Only update the UI if this specific request batch wasn't cancelled
            if (!signal.aborted) {
                this.previewYears = results.filter(Boolean);
            }
        },

        // Download ICS File
        async downloadICS() {
            this.isGenerating = true;
            const categories = this.categoriesToFetch;
            const fetches = [];

            // Fetch calendar data for all selected years and categories
            for (let year = this.startYear; year <= this.endYear; year++) {
                categories.forEach(cat => {
                    fetches.push(fetch(this._getPath(year, cat, 'ics')).then(r => r.ok ? r.text() : "").catch(() => ""));
                });
            }

            const results = await Promise.all(fetches);

            // Extract dynamic header or fallback to default
            const dynamicHeader = results.find(text => text)?.match(/^BEGIN:VCALENDAR[\s\S]*?(?=BEGIN:VEVENT)/i)?.[0].trim()
                || "BEGIN:VCALENDAR\r\nVERSION:2.0\r\nCALSCALE:GREGORIAN";

            // Combine events from all fetched files
            const combinedEvents = results.flatMap(text => text.match(/BEGIN:VEVENT[\s\S]*?END:VEVENT/gi) || []);

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
