# Dynamic Project Details Implementation

## Problem
Every project page was showing "Core Drilling" content regardless of which project was clicked. The project details page was not dynamically loading project-specific information.

## Solution Implemented

### 1. Created Centralized Project Data (data/projects.json)
- Moved all 14 project definitions into a JSON file for easier management
- Each project contains: title, location, description, images, client, size, year, and categories
- Projects are keyed by their URL-friendly IDs (e.g., "quartz-morogoro", "gold-mazizi-morogoro")

### 2. Updated JavaScript (js/project-details.js)
- Implemented async/await to load project data from JSON file
- Reads the `?project=` URL parameter to determine which project to display
- Dynamically updates all page elements:
  - Page title and meta description
  - Banner title and breadcrumb
  - Project images in slider
  - Project description
  - Client, location, size, year, and categories
- Falls back to "core-drilling" as default if no project ID is provided

### 3. Updated HTML Template (projects-single.html)
- Changed hardcoded "Core Drilling" content to generic placeholders
- Page title: "Briva - Project Details"
- Banner and content use "Project Details" and "Loading..." placeholders
- JavaScript replaces these with actual project data on page load

### 4. Created Test Page (test-projects.html)
- Easy-to-use interface to test all 14 project links
- Visual grid layout showing all projects
- Testing checklist to verify dynamic loading works correctly

## How It Works

1. User clicks a project link (e.g., `projects-single.html?project=quartz-morogoro`)
2. Page loads with generic placeholder content
3. JavaScript reads the URL parameter (`quartz-morogoro`)
4. Fetches project data from `data/projects.json`
5. Updates all page elements with the specific project's information
6. Reinitializes the image slider with project-specific images

## Testing

Visit: `http://127.0.0.1:8080/test-projects.html`

Click on different projects and verify:
- ✅ Page title changes to match project name
- ✅ Banner shows correct project name
- ✅ Description is unique to each project
- ✅ Location, client, size, year are project-specific
- ✅ Images match the project

## Files Modified

1. **Created:**
   - `data/projects.json` - Centralized project data
   - `test-projects.html` - Testing interface

2. **Updated:**
   - `js/project-details.js` - Complete rewrite with async JSON loading
   - `projects-single.html` - Replaced hardcoded content with placeholders

## All 14 Projects

1. Artisanal Gold Miners (Tabora)
2. Artisanal Miners (Morogoro)
3. Beryllium (Namtumbo)
4. Beryllium Prospecting (Namtumbo)
5. Coal Outcrop Mapping (Liweta)
6. Core Drilling (Various Locations)
7. Cu-Zn Exploration (Mpanda)
8. Dolomite Prospecting (Dodoma)
9. Face Mapping in Coal Mine
10. Gold Mineralization (Mazizi, Morogoro)
11. Graphite Kyanite Gneiss Stockpile (Merelani)
12. Graphite Kyanite Gneiss (Merelani)
13. Pegmatite Lithium Exploration (Dodoma)
14. Quartz Prospecting (Morogoro)

Each project now has its own unique URL and displays its specific information!
