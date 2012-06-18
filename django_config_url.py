# -*- coding: utf-8 -*-

import os
import urlparse


backends = []
# loop backend.* modules and import?

# get backend TYPES, add them to netloc here
urlparse.uses_netloc.append('db')

DEFAULT_ENV = 'CACHE_URL'

def config(backend, default=None):
# def config(env=DEFAULT_ENV, default='locmem://'):
    """Returns configured CACHES dictionary from CACHE_URL"""
    var = '{0}_url'.format(backend).upper()

    # want to get the default for the backend here
    default = backends[backend].DEFAULT
    config = {}

    s = os.environ.get(var, default)

    if s:
        config = parse(s, backend)

    return config

def parse(url, backend):
    """Parses a URL."""
    url = urlparse.urlparse(url)

    config = {}
    config['BACKEND'] = backend[url.scheme]
    config.update(backend.build_vars(url))
    return config

