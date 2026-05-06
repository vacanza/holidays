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

    <div class="control-group">
      <label for="selected-entity" x-text="type === 'countries' ? 'Country / Region' : 'Market'"></label>
      <select id="selected-entity" class="control-input" x-model="selectedEntity" @change="updateOptions()">
        <option value="" disabled>Select...</option>
        <template x-for="(data, code) in currentManifest" :key="code">
          <option :value="code" x-text="data.name"></option>
        </template>
      </select>
    </div>

    <div class="control-group" x-show="hasSubdivisions">
      <label for="selected-subdiv">Subdivision / State</label>
      <select id="selected-subdiv" class="control-input" x-model="selectedSubdiv" @change="updatePreview()">
        <option value="ALL">Entire Country</option>
        <template x-for="sub in availableSubdivisions" :key="sub.code">
          <option :value="sub.code" x-text="sub.name"></option>
        </template>
      </select>
    </div>

    <div class="year-range-grid" style="grid-template-columns: 1fr 1fr; gap: 12px;">
      <div class="control-group" style="margin-bottom: 0;">
        <label for="selected-lang">Language</label>
        <select id="selected-lang" class="control-input" x-model="selectedLang" @change="updatePreview()" :title="availableLanguages.find(l => l.code === selectedLang)?.name">
          <template x-for="lang in availableLanguages" :key="lang.code">
            <option :value="lang.code" x-text="lang.name" :title="lang.name"></option>
          </template>
        </select>
      </div>
      
      <div class="control-group" style="margin-bottom: 0;">
        <label for="selected-category">Category</label>
        <select id="selected-category" class="control-input" x-model="selectedCategory" @change="updatePreview()" :title="formatLabel(selectedCategory)">
          <template x-for="cat in selectableCategories" :key="cat">
            <option :value="cat" x-text="formatLabel(cat)" :title="formatLabel(cat)"></option>
          </template>
        </select>
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

    <button class="btn-download" @click="downloadICS()" :disabled="isGenerating || !selectedEntity || previewYears.length === 0">
      <span x-text="isGenerating ? 'Processing...' : 'Download .ics File'"></span>
    </button>
    <div style="text-align: center; margin-top: 8px; font-size: 0.8rem; opacity: 0.7;">
      <span x-text="filename"></span>
    </div>

  </div>

  <div class="portal-preview" x-show="!isLoading" style="display: none;">
    <div x-show="!selectedEntity" class="empty-state">Select a region to start.</div>
    <div x-show="selectedEntity && previewYears.length === 0" class="empty-state">No data available for this selection.</div>

    <div class="table-scroll-area" x-show="previewYears.length > 0">
      <table class="preview-table">
        <thead>
          <tr>
            <th style="width: 120px;">Date</th>
            <th>Holiday Name</th>
          </tr>
        </thead>
        <template x-for="yearData in previewYears" :key="yearData.year">
          <tbody>
            <tr>
              <td colspan="2" class="year-divider" x-text="yearData.year"></td>
            </tr>
            <template x-for="(event, index) in yearData.events" :key="index">
              <tr>
                <td style="font-family: monospace;" x-text="formatDate(event.date || event.start)"></td>
                <td x-text="event.name || event.summary"></td>
              </tr>
            </template>
          </tbody>
        </template>
      </table>
    </div>
  </div>

</div>
