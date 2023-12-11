from django.conf import settings

def admin_media(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {
        'SOCIAL_AUTH_GITHUB_KEY': settings.SOCIAL_AUTH_GITHUB_KEY,
        'SOCIAL_AUTH_GOOGLE_OAUTH2_KEY': '12'
            }