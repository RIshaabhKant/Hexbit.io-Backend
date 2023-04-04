from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from userprofile.models import UserProfile

def get_tokens_for_user(user: UserProfile) -> dict:
    refresh = RefreshToken.for_user(user)

    return get_access_from_refresh_token(str(refresh))

def get_access_from_refresh_token(refresh: str) -> dict:
    try:
        token = RefreshToken(refresh)
        return {
            'refresh': str(token),
            'access': str(token.access_token)
        }
    except:
        return {'error': 'Token Expired'}

def get_user_for_request(request) -> UserProfile:
    auth = JWTAuthentication()
    user, _ = auth.authenticate(request)

    return user