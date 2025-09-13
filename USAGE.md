# Wallpapers Gallery Usage Guide

## Overview
This repository is set up as an automated wallpapers gallery that displays all wallpapers with their names in the README.md file.

## Adding New Wallpapers

1. **Add your wallpaper files** to the `wallpapers/` directory
   - Supported formats: JPG, JPEG, PNG, GIF, WebP, BMP, PPM
   - Use descriptive filenames (e.g., `mountain_sunset.jpg`, `abstract_blue.png`)

2. **Update the gallery** by running:
   ```bash
   python3 generate_gallery.py
   ```

3. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add new wallpapers"
   git push
   ```

## File Naming

The gallery script automatically converts filenames to readable titles:
- `mountain_sunset.jpg` → "Mountain Sunset"
- `abstract-blue.png` → "Abstract Blue"
- `cosmic_purple.ppm` → "Cosmic Purple"

## Gallery Features

- **Automatic grid layout**: Wallpapers are displayed in a 2-column grid
- **Responsive titles**: Filenames are converted to human-readable titles
- **Collection stats**: Shows total count and last update info
- **Multiple formats**: Supports all common image formats
- **Easy downloads**: Right-click any image to download

## Regenerating the Gallery

Run the gallery generator anytime to refresh the README:
```bash
python3 generate_gallery.py
```

This will:
- Scan the `wallpapers/` directory for image files
- Generate a new README.md with all wallpapers displayed
- Show collection statistics
- Preserve the existing format and structure