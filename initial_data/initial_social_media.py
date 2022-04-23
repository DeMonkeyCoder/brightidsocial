from core.consts import SocialMediaType, SocialMediaShareTypeDisplay, SocialMediaShareType, SocialMediaShareActionType
from core.models import SocialMediaVariation


class SocialMediaVariationIds:
    DISCORD = 'fab9a32f-e968-495e-807f-7f1b27642506'
    INSTAGRAM = 'efc5e269-195b-47e8-8634-b1899c00df9b'
    KEYBASE = '607223cc-7fbc-4b44-a595-e84d62146f30'
    LINKEDIN = 'd750bd42-e2d3-465f-a3fd-40fde0080022'
    MEDIUM = '50ea1e56-f53b-4fa9-bbcb-846a3f3ac7b6'
    REDDIT = '65a174ff-b823-4abd-9dbb-ae0f46f7bc53'
    SIGNAL = '0e92b39b-e1b5-4236-be40-7377aadca4db'
    TELEGRAM = '4fc96842-0d3d-40ba-bb39-1aaf59a48a59'
    TWITTER = 'a8b188b1-f9f9-416d-b002-7b7faf6e2d41'
    WHATSAPP = '283ade8a-6ef1-4d38-a744-70ee2f478ba4'
    PHONE_NUMBER = '9d79c2ec-632c-4a5f-a04f-73d8e06024ec'
    EMAIL = 'c01bee17-6f89-477f-8cd4-fe5505691a9a'


def get_initial_social_media_variations():
    directory = 'initial_data/icons/'
    f = open(directory + 'icons8-reddit.svg', 'r')
    reddit_icon = f.read()
    f.close()
    f = open(directory + 'icons8-linkedin.svg', 'r')
    linkedin_icon = f.read()
    f.close()
    f = open(directory + 'icons8-whatsapp.svg', 'r')
    whatsapp_icon = f.read()
    f.close()
    f = open(directory + 'icons8-instagram.svg', 'r')
    instagram_icon = f.read()
    f.close()
    f = open(directory + 'icons8-signal-app.svg', 'r')
    signal_icon = f.read()
    f.close()
    f = open(directory + 'icons8-telegram-app.svg', 'r')
    telegram_icon = f.read()
    f.close()
    f = open(directory + 'icons8-discord-bubble.svg', 'r')
    discord_icon = f.read()
    f.close()
    f = open(directory + 'Keybase_logo_official.svg', 'r')
    keybase_icon = f.read()
    f.close()
    f = open(directory + 'icons8-medium-monogram.svg', 'r')
    medium_icon = f.read()
    f.close()
    f = open(directory + 'icons8-twitter-circled.svg', 'r')
    twitter_icon = f.read()
    f.close()

    social_media_variations = [
        {
            'id': SocialMediaVariationIds.DISCORD,
            'name': 'Discord',
            'icon': discord_icon,
            'type': SocialMediaType.SOCIAL_PROFILE,
            'share_type': SocialMediaShareType.USERNAME,
            'share_type_display': SocialMediaShareTypeDisplay.USERNAME,
            'share_action_type': SocialMediaShareActionType.COPY,
            'share_action_data_format': '%%PROFILE%%',
            'bright_id_app_id': None,
        },
        {
            'id': SocialMediaVariationIds.INSTAGRAM,
            'name': 'Instagram',
            'icon': instagram_icon,
            'type': SocialMediaType.SOCIAL_PROFILE,
            'share_type': SocialMediaShareType.USERNAME,
            'share_type_display': SocialMediaShareTypeDisplay.USERNAME,
            'share_action_type': SocialMediaShareActionType.OPEN_LINK,
            'share_action_data_format': 'https://instagram.com/%%PROFILE%%/',
            'bright_id_app_id': None,
        },
        {
            'id': SocialMediaVariationIds.KEYBASE,
            'name': 'Keybase',
            'icon': keybase_icon,
            'type': SocialMediaType.SOCIAL_PROFILE,
            'share_type': SocialMediaShareType.USERNAME,
            'share_type_display': SocialMediaShareTypeDisplay.USERNAME,
            'share_action_type': SocialMediaShareActionType.OPEN_LINK,
            'share_action_data_format': 'https://keybase.io/%%PROFILE%%/',
            'bright_id_app_id': None,
        },
        {
            'id': SocialMediaVariationIds.LINKEDIN,
            'name': 'LinkedIn',
            'icon': linkedin_icon,
            'type': SocialMediaType.SOCIAL_PROFILE,
            'share_type': SocialMediaShareType.URL,
            'share_type_display': SocialMediaShareTypeDisplay.URL,
            'share_action_type': SocialMediaShareActionType.OPEN_LINK,
            'share_action_data_format': 'https://www.linkedin.com/in/%%PROFILE%%/',
            'bright_id_app_id': None,
        },
        {
            'id': SocialMediaVariationIds.MEDIUM,
            'name': 'Medium',
            'icon': medium_icon,
            'type': SocialMediaType.SOCIAL_PROFILE,
            'share_type': SocialMediaShareType.URL,
            'share_type_display': SocialMediaShareTypeDisplay.URL,
            'share_action_type': SocialMediaShareActionType.OPEN_LINK,
            'share_action_data_format': '%%PROFILE%%',
            'bright_id_app_id': None,
        },
        {
            'id': SocialMediaVariationIds.REDDIT,
            'name': 'Reddit',
            'icon': reddit_icon,
            'type': SocialMediaType.SOCIAL_PROFILE,
            'share_type': SocialMediaShareType.USERNAME,
            'share_type_display': SocialMediaShareTypeDisplay.USERNAME,
            'share_action_type': SocialMediaShareActionType.OPEN_LINK,
            'share_action_data_format': 'https://www.reddit.com/user/%%PROFILE%%/',
            'bright_id_app_id': None,
        },
        {
            'id': SocialMediaVariationIds.SIGNAL,
            'name': 'Signal',
            'icon': signal_icon,
            'type': SocialMediaType.SOCIAL_PROFILE,
            'share_type': SocialMediaShareType.TELEPHONE,
            'share_type_display': SocialMediaShareTypeDisplay.TELEPHONE,
            'share_action_type': SocialMediaShareActionType.OPEN_LINK,
            'share_action_data_format': '%%PROFILE%%',
            'bright_id_app_id': None,
        },
        {
            'id': SocialMediaVariationIds.TELEGRAM,
            'name': 'Telegram',
            'icon': telegram_icon,
            'type': SocialMediaType.SOCIAL_PROFILE,
            'share_type': SocialMediaShareType.USERNAME,
            'share_type_display': SocialMediaShareTypeDisplay.USERNAME_OR_TELEPHONE,
            'share_action_type': SocialMediaShareActionType.COPY_IF_PHONE_LINK_IF_USERNAME,
            'share_action_data_format': 'https://t.me/%%PROFILE%%/',
            'bright_id_app_id': None,
        },
        {
            'id': SocialMediaVariationIds.TWITTER,
            'name': 'Twitter',
            'icon': twitter_icon,
            'type': SocialMediaType.SOCIAL_PROFILE,
            'share_type': SocialMediaShareType.USERNAME,
            'share_type_display': SocialMediaShareTypeDisplay.USERNAME,
            'share_action_type': SocialMediaShareActionType.OPEN_LINK,
            'share_action_data_format': 'https://twitter.com/%%PROFILE%%/',
            'bright_id_app_id': 'twitterRegistry',
        },
        {
            'id': SocialMediaVariationIds.WHATSAPP,
            'name': 'Whatsapp',
            'icon': whatsapp_icon,
            'type': SocialMediaType.SOCIAL_PROFILE,
            'share_type': SocialMediaShareType.TELEPHONE,
            'share_type_display': SocialMediaShareTypeDisplay.TELEPHONE,
            'share_action_type': SocialMediaShareActionType.OPEN_LINK,
            'share_action_data_format': 'https://wa.me/%%PROFILE%%/',
            'bright_id_app_id': None,
        },
        {
            'id': SocialMediaVariationIds.PHONE_NUMBER,
            'name': 'Phone Number',
            'icon': None,
            'type': SocialMediaType.CONTACT_INFO,
            'share_type': SocialMediaShareType.TELEPHONE,
            'share_type_display': SocialMediaShareTypeDisplay.TELEPHONE,
            'share_action_type': SocialMediaShareActionType.COPY,
            'share_action_data_format': '%%PROFILE%%',
            'bright_id_app_id': 'phoneRegistry',
        },
        {
            'id': SocialMediaVariationIds.EMAIL,
            'name': 'Email',
            'icon': None,
            'type': SocialMediaType.CONTACT_INFO,
            'share_type': SocialMediaShareType.EMAIL,
            'share_type_display': SocialMediaShareTypeDisplay.EMAIL,
            'share_action_type': SocialMediaShareActionType.COPY,
            'share_action_data_format': '%%PROFILE%%',
            'bright_id_app_id': 'emailRegistry',
        },
    ]
    return social_media_variations


def upsert_initial_social_media_variations():
    social_media_variations = get_initial_social_media_variations()
    for variation in social_media_variations:
        qs = SocialMediaVariation.objects.filter(
            id=variation['id']
        )
        if qs.exists():
            qs.update(**variation)
        else:
            SocialMediaVariation.objects.create(**variation)
