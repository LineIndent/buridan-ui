# Buridan UI Changelog

All notable changes to this project will be documented in this file.


## buridan/ui@0.4.0
### Added
- New charts landing page.
- New chart theme color: purple.
- New chart tooltip style sheet.
- New dynamic charting for area, bar, and line charts.
  
### Changed
- Significant UI update to entire chart codebase.

### Fixed
- Updated responsive logic for mobile view.
- Significant UI update to entire chart codebase.

---

## buridan/ui@v0.3.4 - 2024-11-26
### Added
- **New `blueprint` wrapper**: Currently excludes code preview; app preview only (WIP for code preview).
- **Additional blueprint items**: Dashboard and Layouts are live.

### Changed
- **Base wrapper refactored** and separated from other wrappers.
- **Excess component nesting refactored** in base wrapper for better readability and performance.
- **Refactoring of item wrappers** (pantry, charts, blueprints) to improve modularity.
- **Further code refactoring** in progress, including reorganizing wrappers and components.

### Fixed
- General **site patches** and smaller fixes for various components.
  
---

## buridan/ui@0.3.3 - 2024-11-20
### Added
- **Blueprint Templates**: Includes advanced app templates (front-end code, styles, and state code), which can be used out of the box with minimal changes.

### Changed
- **Fixed border issue** with `@component_wrappers` for a more consistent design.
- **Minor code refactoring** for wrappers and templates to improve readability and maintainability.
- **Mobile view adjustments** for `rx.tabs.trigger` styling to improve responsiveness.
- Enhanced the **landing page UI** with a refreshed layout and more polished styling.

### Fixed
- Various **small UI improvements** and bug fixes across the site.

---

## buridan/ui@0.3.2 - 2024-11-17
### Added
- **New site landing page** with animation to enhance user experience and aesthetics.

### Changed
- Fixed **UI scaling issue** for the site, ensuring it displays correctly on all screen sizes.
- **Updated navigation**, side menu, and other components for better user interaction and consistency across the site.

---

## buridan/ui@0.3.1 - 2024-11-15
### Fixed
- **Patched scaling issue** with site UI to ensure proper layout on different screen resolutions.

### Changed
- **General UI improvements**, including some visual tweaks and optimizations for smoother user experience.

---

## buridan/ui@0.3.0 - 2024-11-13
### Added
- **New Pantry Item**: Inputs, with a patch for a typo on the site changelog.
- **New Chart Item**: Pie Chart added to enhance data visualization capabilities.
- **New Interactive App**: PubMed A.I. for improved functionality and user interaction.

### Changed
- **UI changes** to the site landing page, including layout and styling adjustments for a modern look.
- **In-page navigation** added to the charts section to improve user navigation and usability.
- New **JavaScript key bindings** for repo cloning and Reflex site functionality to enhance productivity.

### Fixed
- Continued **code refactoring**, including cleanup of the codebase and enhancements to the responsive menu, which now includes three different selections for mobile, tablet, and desktop views.

---

## buridan/ui@0.2.0 - 2024-11-08
### Added
- **Changes to Charts component wrapper**: Enhanced structure and features for more flexibility.
- **Refactor of codebase and state changes**: Simplifying the overall code structure for easier maintainability.

### Changed
- **Code block theme** and font size updated for better visual consistency.
- **Major changes** to `@component_wrapper` menu items, adding new options and refactoring old ones.
- **Updates to the chart collection**: Additional charts and new features added for data presentation.

---

## buridan/ui@0.1.1 - 2024-11-03
### Added
- **Major changes** to site directories and files, improving overall structure.
- **Moved style props into Python dataclasses** for better readability and maintainability of code.

### Changed
- **New landing page** introduced, with improved layout and visuals.

---

## buridan/ui@0.1.0 - 2024-10-30
### Added
- **New interactive app**: RAG AI Application, a new feature for advanced data processing.
  
### Changed
- **Minor changes to styling** of pantry apps; work in progress for better integration and UI consistency.
- **Library build pass with reflex==0.6.4** confirmed as OK, ensuring stability and compatibility.

---

## buridan/ui@0.0.1 - 2024-10-16
### Added
- **First stable release** of `buridan-ui`.
- Initial features and basic components released for use.

