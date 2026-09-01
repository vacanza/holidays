---
hide:
  - navigation
---
<!-- markdownlint-disable MD033 -->
<script defer src="../js/downloads.js"></script>

<script defer src="https://cdnjs.cloudflare.com/ajax/libs/alpinejs/3.13.5/cdn.min.js"></script>

<link rel="stylesheet" href="../css/downloads.css">

# Download Holiday Calendars

<div class="portal-wrapper" x-data="holidayDownloads()" x-init="init()">

  <div class="portal-sidebar" x-show="!isLoading" style="display: none;">

    <div class="control-group">
      <label for="calendar-type">Calendar Type</label>
      <select id="calendar-type" class="control-input" x-model="type" @change="updateType()">
        <option value="countries">Countries / Regions</option>
        <option value="financial">Financial Markets</option>
      </select>
    </div>

    <div class="calendar-selector">
        <label class="selector-label">Countries / Regions</label>
    
        <div class="multi-select" x-data="{ open: false }" @click.outside="open = false">
            <button
                type="button"
                class="multi-select-trigger"
                @click="open = !open"
            >
                <span
                    x-show="selectedEntities.length === 0"
                    class="multi-select-placeholder"
                >
                    Select countries or regions...
                </span>
    
                <span
                    x-show="selectedEntities.length > 0"
                    class="selected-count"
                    x-text="`${selectedEntities.length} selected`"
                ></span>
    
                <span class="multi-select-arrow">▾</span>
            </button>
    
            <div
                x-show="open"
                x-transition
                class="multi-select-dropdown"
            >
                <div class="multi-select-search">
                    <input
                        type="text"
                        x-model="entitySearch"
                        placeholder="Search countries or regions..."
                        @click.stop
                    >
                </div>
    
                <div class="multi-select-actions">
                    <button
                        type="button"
                        @click="selectAllVisibleEntities()"
                    >
                        Select all
                    </button>
    
                    <button
                        type="button"
                        @click="clearEntitySelection()"
                    >
                        Clear
                    </button>
                </div>
    
                <div class="multi-select-options">
                    <template
                        x-for="(data, code) in filteredManifest"
                        :key="code"
                    >
                        <label class="multi-select-option">
                            <input
                                type="checkbox"
                                :value="code"
                                :checked="selectedEntities.includes(code)"
                                @change="toggleEntity(code)"
                            >
    
                            <span x-text="data.name || code"></span>
                        </label>
                    </template>
    
                    <div
                        x-show="Object.keys(filteredManifest).length === 0"
                        class="multi-select-empty"
                    >
                        No countries or regions found.
                    </div>
                </div>
            </div>
        </div>
    
        <!-- Selected country chips -->
        <div
            x-show="selectedEntities.length > 0"
            class="selected-chips"
        >
            <template
                x-for="entity in selectedEntities"
                :key="entity"
            >
                <span class="selected-chip">
                    <span
                        x-text="currentManifest[entity]?.name || entity"
                    ></span>
    
                    <button
                        type="button"
                        @click="toggleEntity(entity)"
                        aria-label="Remove"
                    >
                        ×
                    </button>
                </span>
            </template>
        </div>
    </div>

    <div class="calendar-selector">
        <label class="selector-label">Categories</label>
    
        <div class="category-options">
            <template
                x-for="category in availableMultiCategories"
                :key="category"
            >
                <label class="category-option">
                    <input
                        type="checkbox"
                        :value="category"
                        :checked="selectedCategories.includes(category)"
                        @change="toggleCategory(category)"
                    >
    
                    <span x-text="formatLabel(category)"></span>
                </label>
            </template>
        </div>
    </div>

    <div class="control-group" x-show="selectedEntities.length > 0">
      <label for="selected-lang">Language</label>
      <select id="selected-lang" class="control-input" x-model="selectedLang" @change="listCalendars()">
        <option value="default">Default language for each calendar</option>
        <template x-for="lang in availableLanguages" :key="lang.code">
          <option :value="lang.code" x-text="lang.name"></option>
        </template>
      </select>
      <div class="selection-hint">
        Default uses each selected country's/market's default language.
      </div>
    </div>

    <div class="control-group" style="margin-top: 20px;">
      <label for="start-year">Year Range</label>
      <div class="year-range-grid">
        <select id="start-year" class="control-input" x-model.number="startYear" @change="validateYears()">
          <template x-for="y in allYears" :key="y">
            <option :value="y" :selected="y === startYear" x-text="y"></option>
          </template>
        </select>
        <span class="year-separator">to</span>
        <select id="end-year" class="control-input" x-model.number="endYear" @change="validateYears()">
          <template x-for="y in allYears" :key="y">
            <option :value="y" :selected="y === endYear" x-text="y"></option>
          </template>
        </select>
      </div>
      <div class="quick-actions" style="margin-top: 10px;">
        <button class="chip-btn" @click="setRange('current')">This Year</button>
        <button class="chip-btn" @click="setRange('next3')">Next 3 Years</button>
        <button class="chip-btn" @click="setRange('all')">All Years</button>
      </div>
    </div>

    <div class="calendar-actions">
      <button
          type="button"
          class="list-calendars-button"
          @click="listCalendars()"
          :disabled="selectedEntities.length === 0 || selectedCategories.length === 0"
      >
          List calendars
      </button>
    </div>

    <div class="selection-hint" x-show="selectedEntities.length > 0">
      <span x-text="selectedEntities.length"></span> region(s) ×
      <span x-text="selectedCategories.length"></span> categor<span x-text="selectedCategories.length === 1 ? 'y' : 'ies'"></span>
    </div>

    <div style="text-align: center; margin-top: 10px; font-size: 0.8rem;">
      Need data outside the 2015-2035 range?<br>Use our
      <a href="../examples/#holidays-ics-tool" target="_blank" rel="noopener">holidays-ics</a>
      tool instead.
    </div>
  </div>

    <div class="portal-preview" x-show="!isLoading" style="display: none;">

      <div
      x-show="showCalendarList"
      class="calendar-results"
      >
      <div class="calendar-results-header">
          <div>
              <h3>Available calendars</h3>
  
              <p>
                  <span x-text="selectedEntities.length"></span>
                  countries/regions ·
                  <span x-text="selectedCategories.length"></span>
                  categories ·
                  ICS/JSON downloads cover
                  <span
                      x-text="startYear === endYear ? startYear : `${startYear}-${endYear}`"
                  ></span>
              </p>
          </div>
      </div>

    <div class="calendar-table-wrapper">
        <table class="calendar-table">
            <thead>
                <tr>
                    <th>Region</th>

                    <template
                        x-for="category in selectedCategories"
                        :key="category"
                    >
                        <th x-text="formatLabel(category)"></th>
                    </template>
                </tr>
            </thead>

            <tbody>
                <template
                    x-for="row in calendarRows"
                    :key="row.entity"
                >
                    <tr>
                        <td>
                            <strong x-text="row.name"></strong>

                            <small
                                x-text="row.languageName"
                            ></small>
                        </td>

                        <template
                            x-for="calendar in row.calendars"
                            :key="calendar.category"
                        >
                            <td>
                                <template x-if="calendar.available">
                                    <div class="calendar-links">
                                        <button
                                            type="button"
                                            @click="downloadCalendar(row.entity, calendar.category, 'ics')"
                                            :disabled="calendar.icsDownloading"
                                        >
                                            <span x-text="calendar.icsDownloading ? '...' : 'ICS'"></span>
                                        </button>

                                        <span>·</span>

                                        <button
                                            type="button"
                                            @click="downloadCalendar(row.entity, calendar.category, 'json')"
                                            :disabled="calendar.jsonDownloading"
                                        >
                                            <span x-text="calendar.jsonDownloading ? '...' : 'JSON'"></span>
                                        </button>

                                        <span>·</span>

                                        <a
                                            :href="calendar.webcal"
                                        >
                                            Webcal
                                        </a>

                                        <div
                                            x-show="calendar.error"
                                            class="calendar-error"
                                        >
                                            Download failed, try again.
                                        </div>
                                    </div>
                                </template>

                                <template x-if="!calendar.available">
                                    <span class="calendar-unavailable">
                                        -
                                    </span>
                                </template>
                            </td>
                        </template>
                    </tr>
                </template>
            </tbody>
        </table>
      </div>
    </div>
    </div>
</div>
