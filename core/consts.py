from django.db import models
from django.utils.translation import gettext as _


class SocialMediaType(models.TextChoices):
    SOCIAL_PROFILE = 'so', _('Social Profile')
    CONTACT_INFO = 'co', _('Contact Info')


class SocialMediaShareType(models.TextChoices):
    USERNAME = 'username', _('Username')
    TELEPHONE = 'telephone #', _('Telephone')
    URL = 'url', _('Url')


class SocialMediaShareTypeDisplay(models.TextChoices):
    USERNAME = 'username', _('Username')
    TELEPHONE = 'telephone #', _('Telephone')
    URL = 'url', _('Url')
    USERNAME_OR_TELEPHONE = 'username or telephone', _('Username or Telephone')


class SocialMediaShareActionType(models.TextChoices):
    OPEN_LINK = 'ol', _('Open Link')
    COPY = 'cp', _('Copy')
    COPY_IF_PHONE_LINK_IF_USERNAME = 'cl', _('Copy if phone number and link if username')


class BrightIdNetwork(models.TextChoices):
    TEST = 'test', _('test')
    NODE = 'node', _('node')


class SocialMediaBrightVerificationStatus(models.TextChoices):
    PENDING = '0', _("Pending")
    VERIFIED = '1', _("Verified")
