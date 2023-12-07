# flake8: NOQA: F403,F405
from test_proj.settings import *

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}
