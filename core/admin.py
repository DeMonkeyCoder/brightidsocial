from django.contrib import admin

# Register your models here.
from core.models import SocialMedia, SocialMediaVariation, ProfileHash

admin.site.register(SocialMedia)
admin.site.register(SocialMediaVariation)
admin.site.register(ProfileHash)
