from {{ project_name }}.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ project_name }}',
        # 'USER': 'dbuser',
        # 'PASSWORD': 'dbpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

#############################################
#     DJANGO DEBUG TOOLBAR CONFIGURATION    #
#############################################

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS += (
    'debug_toolbar',
)

INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
)

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TEMPLATE_CONTEXT': True,
}
