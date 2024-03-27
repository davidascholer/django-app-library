**OVERRIDE USER MODEL**

## about
Override the AbstractUser model before initial migration (otherwise a db drop is required)

## overrides the default User model in settings.py
AUTH_USER_MODEL = 'core.User'

## change serializers as needed
In ./serializers.py, change the Meta classes to the signatures required


---


**JWT AUTHENTICATION**

## dependencies
- https://djoser.readthedocs.io/en/latest/getting_started.html
- pipenv install djoser
- pipenv install djangorestframework_simplejwt #for JWT engine

## add new libraries to mainfolder/settings.INSTALLED_APPS
`INSTALLED_APPS = (
    'django.contrib.auth',
    (...),
    'rest_framework',
    'djoser',
    (...),
)`

## configure the urls for djoser
`urlpatterns = [
    ...,
    #url(r'^auth/', include('djoser.urls')),
    #url(r'^auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]`

## configure auth engine (JWT approach)
- Use django-rest-framework's token-based authentication (saves token in db and checks on every request)
- Use a third party JWT authentication (all info in token so no db request required)
 
## configure mainfolder/settings
- add DEFAULT_AUTHENTICATION_CLASSES to REST_FRAMEWORK object:
    `REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 10,
        'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        ),
        ...

    }`
- add SIMPLE_JWT:
#prefixes the token with JWT e.g. 
    `SIMPLE_JWT = {
        'AUTH_HEADER_TYPES': ('JWT',),
    }`

## create user serializers in core/serializers.py
e.g.
`
from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer

#purely responsible to deserialize user data and creating a user record
class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = [...]

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = [...]
`

## add serializers via djoser property in settings.py
https://djoser.readthedocs.io/en/latest/settings.html#serializers
e.g.
`
DJOSER = {
    'SERIALIZERS': {...}
}
`

---


