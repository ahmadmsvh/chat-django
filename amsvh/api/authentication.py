from rest_framework.authentication import TokenAuthentication as BaseTokenAuth


class TokentAuthentication(BaseTokenAuth):
    # keyword = 'Bearer'
    keyword = 'Token'
