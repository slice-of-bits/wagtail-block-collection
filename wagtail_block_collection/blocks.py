from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtailfontawesome.blocks import IconBlock
from wagtail_color_panel.blocks import NativeColorBlock


class TypeWriter(blocks.StructBlock):
    heading_type = blocks.ChoiceBlock(choices=[('h1', 'h1'), ('h2', 'h2'), ('h3', 'h3'), ('h4', 'h4'), ('h5', 'h5')])
    heading_size = blocks.CharBlock(required=False, help_text="any CSS unit supported px, %, rem, vh enz")
    google_font = blocks.CharBlock(required=False, help_text="Choose a font from Google Font")
    texts = blocks.ListBlock(
        blocks.StructBlock([
            ("text", blocks.CharBlock(required=True, max_length=265)),
            ("time", blocks.IntegerBlock(required=True)),
        ])
    )
    
    class Meta:
        icon = ""
        template = "wagtail_block_collection/special/typewriter_block.html"
        group = "Special"
        label = "Typewriter"


class ImageSlider(blocks.StructBlock):
    """A slider of images using tiny slider"""
    slides = blocks.ListBlock(
        blocks.StructBlock([
            ("image", ImageChooserBlock(required=False)),
        ])
    )

    class Meta:
        icon = 'fa-object-ungroup'
        template = 'wagtail_block_collection/media/slider_block.html'
        group = "Media"
        label = "IMG Slider"


class Spacer(blocks.StructBlock):
    """Just a spacer to add space between to other streamfields"""
    height = blocks.CharBlock(required=True, help_text="any CSS unit supported px, %, rem, vh enz")

    class Meta:
        icon = 'fa-arrows-v'
        template = 'wagtail_block_collection/layout/spacer_block.html'
        group = "Layout"
        label = "Spacer"


class Line(blocks.StructBlock):
    """A simple line with a few options"""
    width = blocks.CharBlock(required=False, help_text="any CSS unit supported px, %, rem, vh enz")
    thickness = blocks.CharBlock(required=True, help_text="any CSS unit supported px, %, rem, vh enz")
    color = NativeColorBlock(required=False)
    style = blocks.ChoiceBlock(required=True, choices=[('solid', 'solid'), ('dashed', 'dashed'), ('dotted', 'dotted')])

    class Meta:
        icon = 'fa-ellipsis-h'
        template = 'wagtail_block_collection/basic/line_block.html'
        group = "Basic"
        label = "Line"


#TODO a easy way to add scaling options
class ImageBlock(blocks.StructBlock):
    """A basic image"""
    img = ImageChooserBlock(required=True, help_text="Select a nice photo")

    class Meta:
        icon = 'image'
        template = 'wagtail_block_collection/media/img_block.html'
        group = "Media"
        label = "Image"


class TextBlock(blocks.StructBlock):
    """The main text block using the rich text option"""
    text_align = blocks.ChoiceBlock(required=False, help_text="If not set section settings wil be used", choices=[
        ('left', 'left'),
        ('center', 'center'),
        ('right', 'right'),
    ])
    text_color = NativeColorBlock(required=False, help_text="If not set section settings wil be used")
    google_font = blocks.CharBlock(required=False, help_text="Choose a font from Google Font")
    text = blocks.RichTextBlock(required=True, help_text="Text for this block")

    class Meta:
        icon = 'fa-font'
        template = 'wagtail_block_collection/basic/text_block.html'
        group = "Basic"
        label = "Text"


class BasicButtonBlock(blocks.StructBlock):
    """A button with some bootstrap styling options"""
    page = blocks.PageChooserBlock(required=False, help_text="the page you want tot point the button to")
    url = blocks.URLBlock(required=False, help_text="Point to a external URL")
    text = blocks.CharBlock(required=True, help_text="The text on the button")
    background_color = NativeColorBlock(required=True, help_text="HEX value of a color")
    text_color = NativeColorBlock(required=True, help_text="HEX value of a color")
    size = blocks.ChoiceBlock(choices=[('btn-lg', 'big'), (' ', 'normal'), ('btn-sm', 'small')])
    google_font = blocks.CharBlock(required=False, help_text="Choose a font from Google Font")

    class Meta:
        icon = 'fa-square'
        template = 'wagtail_block_collection/basic/button_block.html'
        group = "Basic"
        label = "Button"


class TextAndImageBlock(blocks.StructBlock):
    """Image with the text beside"""
    title = blocks.CharBlock(required=False, max_length=128, help_text="Title for this block")
    text = blocks.RichTextBlock(required=True, help_text="Text for this block")
    img = ImageChooserBlock()
    position = blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')])

    class Meta:
        icon = 'fa-id-card-o'
        template = 'wagtail_block_collection/basic/text_and_image_block.html'
        group = "Basic"
        label = "Text and Image"


class YoutubeVideoBlock(blocks.StructBlock):
    """Easy way to add a YouTube video"""
    video_id = blocks.CharBlock(required=True, help_text="the part after ?v=")
    aspect_ratio = blocks.ChoiceBlock(required=False, help_text="this helps with scaling",
                                      choices=[('embed-responsive-21by9', '21:9'), ('embed-responsive-16by9', '16:9'),
                                               ('embed-responsive-4by3', '4:3'), ('embed-responsive-1by1', '1:1')])

    class Meta:
        icon = 'fa-youtube'
        template = 'wagtail_block_collection/media/youtube_video_block.html'
        group = "Media"
        label = "Youtube video"


class EmbedBlock(blocks.StructBlock):
    """For all the stuff that has no streamfield"""
    source = blocks.RawHTMLBlock(required=True, help_text="Just raw HTML code")

    class Meta:
        icon = 'fa-code'
        template = 'wagtail_block_collection/embed_block.html'
        group = "Advanced"
        label = "Embed code"


class BasicTitleBlock(blocks.StructBlock):
    """"Title with styling options"""
    title = blocks.CharBlock(required=True, max_length=255)
    heading_type = blocks.ChoiceBlock(choices=[('h1', 'h1'), ('h2', 'h2'), ('h3', 'h3'), ('h4', 'h4'), ('h5', 'h5')])
    heading_size = blocks.CharBlock(required=False, help_text="any CSS unit supported px, %, rem, vh enz")
    google_font = blocks.CharBlock(required=False, help_text="Choose a font from Google Font")

    class Meta:
        icon = 'fa-header'
        template = "wagtail_block_collection/basic/title_block.html"
        group = "Basic"
        label = "Title"


class IconBlock(blocks.StructBlock):
    """Basic fontawesome icons"""
    icon_color = NativeColorBlock(required=True)
    icon_size = blocks.CharBlock(max_length=10, required=True, help_text="any CSS unit supported px, %, rem, vh enz")
    icon_icon = IconBlock(required=True)

    class Meta:
        icon = 'pick'
        template = 'wagtail_block_collection/basic/icon_block.html'
        group = "Basic"
        label = "icon"


class BasicCardDeck(blocks.StructBlock):
    """Bootstrap card deck"""
    title = blocks.CharBlock(required=False, max_length=128)
    cards = blocks.ListBlock(
        blocks.StructBlock([
            ("image", ImageChooserBlock(required=False)),
            ("title", blocks.CharBlock(required=False, max_length=64)),
            ("description", blocks.TextBlock(required=False)),
            ("button_page", blocks.PageChooserBlock(required=False)),
            ("button_url", blocks.URLBlock(required=False, help_text="is used if no page is set")),
            ("background_color", NativeColorBlock(required=False)),
        ])
    )

    class Meta:
        icon = 'fa-th'
        template = "wagtail_block_collection/card_deck_block.html"
        group = "Cards"
        label = "Card Equal Height"


class GoogleMapsBlock(blocks.StructBlock):
    """Google maps block"""
    location = blocks.CharBlock(required=True, max_length=128,
                              help_text="the google maps search where you want to put the marker")
    height = blocks.CharBlock(required=True, help_text="any CSS unit supported px, %, rem, vh enz")

    class Meta:
        icon = 'fa-map'
        template = 'wagtail_block_collection/miscellaneous/google_maps.html'
        label = "Google maps"
        group = "Miscellaneous"


content_blocks = [
    ("TextBlock", TextBlock()),
    ("TextAndImageBlock", TextAndImageBlock()),
    ("BasicTitleBlock", BasicTitleBlock()),
    ("BasicCardDeck", BasicCardDeck()),
    ("IconBlock", IconBlock()),
    ("BasicButtonBlock", BasicButtonBlock()),
    ("ImageBlock", ImageBlock()),
    ("YoutubeVideoBlock", YoutubeVideoBlock()),
    ("EmbedBlock", EmbedBlock()),
    ("Spacer", Spacer()),
    ("Line", Line()),
    ("GoogleMapsBlock", GoogleMapsBlock()),
    ("TypeWriter", TypeWriter()),
    ("ImageSlider", ImageSlider()),
]
#################
# Layout blocks #
#################
class Row(blocks.StructBlock):
    """Bootstrap collum system"""
    columns = blocks.ListBlock(
        blocks.StructBlock([
            ("col_width", blocks.ChoiceBlock(choices=(('12', '12/12'), ('10', '10/12'), ('8', '8/12'), ('6', '6/12'), ('4', '4/12'), ('2', '2/12')))),
            ("col_content", blocks.StreamBlock(content_blocks))
        ])
    )

    class Meta:
        icon = "fa-table"
        template = 'wagtail_block_collection/layout/row.html'
        group = "Layout"
        label = "Column"


class CollapseBlockButton(blocks.StructBlock):
    """Collapse some context using a button"""
    button_text = blocks.CharBlock(required=True)
    button_background_color = NativeColorBlock(required=True)
    button_text_color = NativeColorBlock(required=True)
    button_size = blocks.ChoiceBlock(choices=[('btn-lg', 'big'), (' ', 'normal'), ('btn-ls', 'small')])
    button_google_font = blocks.CharBlock(required=False, help_text="Choose a font from Google Font")
    content_background_show = blocks.BooleanBlock(help_text="If selected the content wil be on a card")
    content_background_color = NativeColorBlock(required=False)
    content = blocks.StreamBlock(content_blocks)

    class Meta:
        icon = "fa-compress"
        template = 'wagtail_block_collection/layout/collapse_button.html'
        group = "Layout"
        label = "Collapse with button"


class Accordion(blocks.StructBlock):
    items = blocks.ListBlock(
        blocks.StructBlock([
            ("title", blocks.CharBlock(required=True, max_length=128)),
            ("content", blocks.StreamBlock(content_blocks))
        ])
    )

    class Meta:
        icon = ''
        template = 'wagtail_block_collection/layout/accordion.html'
        group = "Layout"
        label = "Accordion"


layout_blocks = [
    ("Row", Row()),
    ("CollapseBlockButton", CollapseBlockButton()),
    ("Accordion", Accordion()),
]
############
# Sections #
############
all_blocks = content_blocks + layout_blocks


class BasicSection(blocks.StructBlock):
    """Basic section with a solid color background"""
    background_color = NativeColorBlock(required=True, help_text="The hex value of the background")
    text_color = NativeColorBlock(required=True, help_text="The hex value of the text")
    full_width = blocks.BooleanBlock(required=False)
    bottom_effect = blocks.ChoiceBlock(required=False, choices=[('zigzag', 'zigzag'), ('arrow', 'arrow'), ('arrow_big', 'arrow_big')])
    content = blocks.StreamBlock(all_blocks)

    class Meta:
        template = 'wagtail_block_collection/sections/basic_section.html'
        label = "Basic color background"


class SectionImgParalax(blocks.StructBlock):
    """Section with a image as a background and a paralax effect"""
    background_img = ImageChooserBlock(required=True)
    text_color = NativeColorBlock(required=True, help_text="The hex value of the text")
    full_width = blocks.BooleanBlock(required=False)
    bottom_effect = blocks.ChoiceBlock(required=False, choices=[('zigzag', 'zigzag'), ('arrow', 'arrow'), ('arrow_big', 'arrow_big')])
    content = blocks.StreamBlock(all_blocks)

    class Meta:
        template = 'wagtail_block_collection/sections/section_img_paralex.html'
        label = "Section with paralax img background"


class SectionImg(blocks.StructBlock):
    """Section with a image background"""
    background_img = ImageChooserBlock(required=True)
    text_color = NativeColorBlock(required=True, help_text="The hex value of the text")
    full_width = blocks.BooleanBlock(required=False)
    bottom_effect = blocks.ChoiceBlock(required=False, choices=[('zigzag', 'zigzag'), ('arrow', 'arrow'), ('arrow_big', 'arrow_big')])
    content = blocks.StreamBlock(all_blocks)

    class Meta:
        template = 'wagtail_block_collection/sections/section_img.html'
        label = "Section img background"


class SectionGradient(blocks.StructBlock):
    """Section with a CSS gradient"""
    text_color = NativeColorBlock(required=True)
    angel = blocks.IntegerBlock(min_value=0, max_value=360, required=True)
    full_width = blocks.BooleanBlock(required=False)
    bottom_effect = blocks.ChoiceBlock(required=False, choices=[('zigzag', 'zigzag'), ('arrow', 'arrow'), ('arrow_big', 'arrow_big')])
    stops = blocks.ListBlock(
        blocks.StructBlock([
            ('color', NativeColorBlock(required=True)),
            ('stop', blocks.IntegerBlock(min_value=0, max_value=100))
        ])
    )
    content = blocks.StreamBlock(all_blocks)

    class Meta:
        template = 'wagtail_block_collection/sections/section_gradient.html'
        label = "Section with color gradient background"


class SectionImgBesideContent(blocks.StructBlock):
    """Show a full width and height image with steamfields beside that"""
    background_img = ImageChooserBlock(required=True)
    background_color = NativeColorBlock(required=True)
    text_color = NativeColorBlock(required=True, help_text="All the text inside the section will get this collor")
    position = blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')])
    bottom_effect = blocks.ChoiceBlock(required=False, choices=[('zigzag', 'zigzag'), ('arrow', 'arrow'), ('arrow_big', 'arrow_big')])
    content = blocks.StreamBlock(all_blocks)

    class Meta:
        template = 'wagtail_block_collection/sections/section_img_beside_content.html'
        label = "Section img with content beside"


class CarouselSlider(blocks.StructBlock):
    id = blocks.CharBlock(required=True, help_text="A unique name that can not contain spaces")
    slides = blocks.ListBlock(
        blocks.StructBlock([
            ("image", ImageChooserBlock(required=True)),
            ("title", blocks.CharBlock(required=False)),
            ("subline", blocks.CharBlock(required=False))
        ])
    )

    class Meta:
        icon = 'fa-object-ungroup'
        template = 'wagtail_block_collection/sections/carousel_slider_section.html'
        label = "IMG Slider"


sections = [
    ("BasicSection", BasicSection()),
    ("SectionImgParalax", SectionImgParalax()),
    ("SectionImg", SectionImg()),
    ("SectionGradient", SectionGradient()),
    ("SectionImgBesideContent", SectionImgBesideContent()),
    ("CarouselSlider", CarouselSlider())
]