import locale

from django.conf import settings
from django.template import engines
from django.template.backends.jinja2 import Jinja2
from django.utils.formats import localize_input

from jinja2 import Environment

locale.setlocale(locale.LC_ALL, settings.LANGUAGE_CODE)

def environment(**options):
    env = Environment(**options)
    env.filters['localize'] = localize_input
    return env

class TeXEngine(Jinja2):
    app_dirname = 'templates'

params = {
    'NAME': 'tex',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
        'environment': 'tex.engine.environment'
    },
}

engine = TeXEngine(params)