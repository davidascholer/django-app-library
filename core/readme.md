# About
Override the AbstractUser model before initial migration (otherwise a db drop is required)

# Overrides the default User model in settings.py
AUTH_USER_MODEL = 'core.User'

# Change serializers as needed
In ./serializers.py, change the Meta classes to the signatures required
