#!/usr/bin/env python3
"""
Gallery generator for wallpapers repository.
Scans the wallpapers directory and generates a README.md with a gallery view.
"""

import os
import re
from pathlib import Path

def get_wallpaper_files(wallpapers_dir):
    """Get all image files from the wallpapers directory."""
    if not os.path.exists(wallpapers_dir):
        return []
    
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp', '.ppm'}
    wallpaper_files = []
    
    for file in os.listdir(wallpapers_dir):
        file_path = Path(file)
        if file_path.suffix.lower() in image_extensions:
            wallpaper_files.append(file)
    
    return sorted(wallpaper_files)

def format_filename_as_title(filename):
    """Convert filename to a human-readable title."""
    # Remove extension
    name = Path(filename).stem
    # Replace underscores and hyphens with spaces
    name = re.sub(r'[_-]', ' ', name)
    # Capitalize words
    return name.title()

def generate_gallery_markdown(wallpapers_dir='wallpapers'):
    """Generate markdown content for the wallpapers gallery."""
    wallpaper_files = get_wallpaper_files(wallpapers_dir)
    
    if not wallpaper_files:
        return """# Wallpapers Gallery

This repository contains a collection of wallpapers.

*No wallpapers found. Add images to the `wallpapers/` directory.*

## Adding Wallpapers

1. Place your wallpaper images in the `wallpapers/` directory
2. Run `python3 generate_gallery.py` to update this README
3. Supported formats: JPG, PNG, GIF, WebP, BMP, PPM

## Gallery

Coming soon...
"""
    
    markdown_content = """# Wallpapers Gallery

This repository contains a collection of high-quality wallpapers.

## Gallery

"""
    
    # Add gallery grid (2 columns)
    for i in range(0, len(wallpaper_files), 2):
        markdown_content += "| | |\n"
        markdown_content += "|:---:|:---:|\n"
        
        # First column
        file1 = wallpaper_files[i]
        title1 = format_filename_as_title(file1)
        markdown_content += f"| **{title1}** | "
        
        # Second column (if exists)
        if i + 1 < len(wallpaper_files):
            file2 = wallpaper_files[i + 1]
            title2 = format_filename_as_title(file2)
            markdown_content += f"**{title2}** |\n"
        else:
            markdown_content += " |\n"
        
        # Image row
        markdown_content += f"| ![{title1}](wallpapers/{file1}) | "
        if i + 1 < len(wallpaper_files):
            file2 = wallpaper_files[i + 1]
            title2 = format_filename_as_title(file2)
            markdown_content += f"![{title2}](wallpapers/{file2}) |\n"
        else:
            markdown_content += " |\n"
        
        markdown_content += "\n"
    
    markdown_content += f"""
## Collection Info

- **Total wallpapers**: {len(wallpaper_files)}
- **Last updated**: Auto-generated gallery

## Adding Wallpapers

1. Place your wallpaper images in the `wallpapers/` directory
2. Run `python3 generate_gallery.py` to update this README
3. Commit and push your changes

## Supported Formats

JPG, JPEG, PNG, GIF, WebP, BMP, PPM

## Usage

Right-click any image above and select "Save image as..." to download.
"""
    
    return markdown_content

def main():
    """Main function to generate and update README."""
    try:
        markdown_content = generate_gallery_markdown()
        
        with open('README.md', 'w') as f:
            f.write(markdown_content)
        
        print("✅ README.md updated successfully!")
        print(f"📁 Found {len(get_wallpaper_files('wallpapers'))} wallpapers")
        
    except Exception as e:
        print(f"❌ Error generating gallery: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())