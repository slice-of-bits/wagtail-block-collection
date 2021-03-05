[![Build Status](https://drone.sliceofbits.com/api/badges/slice-of-bits/wagtail-block-collection/status.svg)](https://drone.sliceofbits.com/slice-of-bits/wagtail-block-collection)
![PyPI](https://img.shields.io/pypi/v/wagtail-block-collection)
![PyPI - Downloads](https://img.shields.io/pypi/dw/wagtail-block-collection?label=donwloads%2Fweek)
![PyPI - Downloads](https://img.shields.io/pypi/dm/wagtail-block-collection?label=donwloads%2Fmonth)
![PyPI - License](https://img.shields.io/pypi/l/wagtail-block-collection)
![PyPI](https://img.shields.io/pypi/v/wagtail-block-collectiontail-block-collection)
![GitHub followers](https://img.shields.io/github/followers/slice-of-bits?style=social)
![GitHub Repo stars](https://img.shields.io/github/stars/slice-of-bits/wagtail-block-collection?style=social)
# wagtail-block-collection
A collection of some basic wagtail streamfields blocks.
Based on bootstrap 5.0

The blocks are divided in two categories:  
**Sections**  
Sections are a group of multiple blocks and include settings like the background.
They are perfect for the basic one page layout  
**Blocks**  
These are just your normal streamfields to fill your site with content.
They van be used without the sections

## Sections
- Basic color background
- paralax img background
- img background
- gradient background
- section content and image side by side
- Full with (and hight) slider
## Blocks
- Text
- Img + Text
- Title
- Icon
- Button
- Image
- Youtube video
- Bootstrap card deck
- Bootstrap column
- Spacer
- Collapse content by button
- Line
- Google maps
- IMG slider

Planed
- Vimeo video
- More sliders
- Bootstrap accordion
- Bootstrap alert
- Bootstrap buttongroup
- Icon list
- Price table

## Quickstart
You need to have a working Wagtail project and the bootstrap 5.0 .css and .js
```
pip install wagtail-block-collection
```
Add the following enteries to your settings.py in the INSTALLED_APPS section:
```
'wagtail_block_collection',
'wagtailfontawesome',
'wagtail_color_panel',
```
No you can import any of the blocks from ``wagtail_block_collection.blocks``  
Or you can import them all using ``all_blocks``

## Todo
- Add documentation
- Add scaling options to the img block
- Animations
- Build a easy way to select icons