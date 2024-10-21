# Contributing

Thanks for your interest in contributing to buridan/ui.

Please take a moment to review this document before submitting your first pull request. We also strongly recommend that you check for open issues and pull requests to see if someone else is working on something similar.

# Important Directories & Files

| Path                                     | Description                                             |
|------------------------------------------|---------------------------------------------------------|
| `buridan_ui/routes`                      | The dir where all the routes are held.                  |
| `buridan_ui/pantry`                      | The main dir where all compoenents are stored.          |
| `buridan_ui/pages/pantry_items/items.py` | The main export file for all pages related to *pantry*. |

## Development

### Fork this repo

You can fork this repo by clicking the fork button in the top right corner of this page.

### Clone on your local machine

```bash
git clone https://github.com/your-username/buridan-ui.git
```

### Navigate to project directory

```bash
cd buridan-ui
```

### Create a new Branch

```bash
git checkout -b my-new-branch
```

### Install dependencies
Make sure to install or have installed *Reflex*
```bash
pip install reflex
```

# Build (IN PORGRESS)

The following steps should be taken to facilitate adding a new component:

1. First, add the route of the component to ```routes/pantry_routes``` if it's a completely new component design.
2. Add and normalize the dir name for the thumbnails.
3. Add a SVG to the assets
4. create a v{n} (n=1) and build the ui
5. export the file inside pantry/exports.py
6. export and add the UI using pantry_items/items.py