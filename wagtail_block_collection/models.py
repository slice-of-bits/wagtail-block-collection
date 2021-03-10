from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class WagtailBlockCollectionSettings(BaseSetting):
    google_api_key = models.CharField(max_length=64,
                                      help_text='The google cloud api key for google maps')
