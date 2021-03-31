[![Build Status](https://drone.sliceofbits.com/api/badges/slice-of-bits/wagtail-block-collection/status.svg)](https://drone.sliceofbits.com/slice-of-bits/wagtail-block-collection)
[![Docs](https://img.shields.io/badge/docs-passing-brightgreen)](https://wagtail-block-collection.sliceofbits.com/)
[![PyPI](https://img.shields.io/pypi/v/wagtail-block-collection)](https://pypi.org/project/wagtail-block-collection/)
[![PyPI - Downloads](https://img.shields.io/pypi/dw/wagtail-block-collection?label=downloads%2Fweek)](https://pypi.org/project/wagtail-block-collection/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/wagtail-block-collection?label=downloads%2Fmonth)](https://pypi.org/project/wagtail-block-collection/)
![PyPI - License](https://img.shields.io/pypi/l/wagtail-block-collection)
![GitHub followers](https://img.shields.io/github/followers/slice-of-bits?style=social)
![GitHub Repo stars](https://img.shields.io/github/stars/slice-of-bits/wagtail-block-collection?style=social)

:exclamation: This project is very beta everything can change any second  
:exclamation: And this is my first python package   
:exclamation: So no garanties of any kind  
# wagtail-block-collection
A collection of some basic wagtail streamfields blocks.
Based on bootstrap 5.0

The blocks are divided in two categories:  
**Sections**  
Sections are a group of multiple blocks and include settings like the background.
They are perfect for the basic one-page layout  
**Blocks**  
These are just your normal streamfields to fill your site with content.
They van be used without the sections

## Sections
- Basic color background
- Paralax img background
- img background
- gradient background
- section content and image side by side
- Full-width (and height) slider
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
- Alert
- Bootstrap accordion
- Bootstrap alert
- Countdown

Planed
- More sliders
- Bootstrap buttongroup
- Icon list
- Price table
- Counter

## Quickstart
This is the short version of what is in the [docs](https://wagtail-block-collection.sliceofbits.com/)  

You need to have a working Wagtail project and the [bootstrap 5.0 .css and .js](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
```
pip install wagtail-block-collection
```
Add the following entries to your settings.py in the INSTALLED_APPS section:
```
'wagtailfontawesome',
'wagtail_color_panel',
'wagtail.contrib.settings',
'wagtail_block_collection',
```
Make sure you have the ``'wagtail.contrib.settings.context_processors.settings',`` templates context_processors 

Now you can import any of the blocks from ``wagtail_block_collection.blocks``  
Or you can import them all using ``all_blocks``

## Todo
- Add more documentation
- Add scaling options to the img block
- Animations
- Build a easy way to select icons
- Charts
- Tabs
- Masonry image
- Image lazy loading

## Support this project
### Committing code
If you want to add a new cool block or see something that could be better?
Just fork this project and then open a pull request.
I know I am not perfect but please clean and understandable code.
### Send me a coffee
<a href="https://buymeacoffee.com/SliceOfBits">
    <img alt="Buy Me A Coffee" src="https://www.buymeacoffee.com/assets/img/custom_images/yellow_img.png" style="height: auto !important; width: auto !important;" />
</a>