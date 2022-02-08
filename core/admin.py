from django.contrib import admin

# Register your models here.
from core.models import SocialMedia, SocialMediaVariation

admin.site.register(SocialMedia)
admin.site.register(SocialMediaVariation)
