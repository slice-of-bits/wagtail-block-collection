# How to install

You need to have a working Wagtail project and the bootstrap 5.0 .css and .js (bootstrap 4 wil probably work but no guaranties)
Install the plugin using pip
```
pip install wagtail-block-collection
```
Add the following entries to your settings.py in the INSTALLED_APPS section:
```
'wagtail_block_collection',
'wagtailfontawesome',
'wagtail_color_panel',
'wagtail.contrib.settings',
```
No you can import any of the blocks from ``wagtail_block_collection.blocks``  
Or you can import them all using ``all_blocks``

Add the following to the template context processors
```python
TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
                ...
                'wagtail.contrib.settings.context_processors.settings',
            ],
        },
    },
]
```

## Example usage
Example flex page:
```python
class FlexPage(Page):
    templates = "website/flex_page.html"

    content = StreamField(sections, blank=True, null=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel("content"),
    ]
```
Template:
```html
{% extends 'base.html' %}
{% load wagtailcore_tags %}

{% block title %}
    {{ page.title }}
{% endblock title %}

{% block content %}
    {%  for block in page.content %}
        {% include_block block %}
    {% endfor %}
{% endblock %}
```