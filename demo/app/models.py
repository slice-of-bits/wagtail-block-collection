from wagtail.admin.panels import StreamFieldPanel, FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from wagtail_block_collection import blocks


class FlexPage(Page):
    template = "app/flex_page.html"

    content = StreamField(blocks.sections, blank=True, null=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel("content"),
    ]