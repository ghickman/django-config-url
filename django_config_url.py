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
    config = {}

    url = urlparse.urlparse(url)

    # CACHE
    config['BACKEND'] = backend[url.scheme]
    if url.scheme == 'file':
        config['LOCATION'] = url.path
        return config

    config['LOCATION'] = url.netloc
    config['PREFIX'] = url.path[1:]

    # DATABASE
    config.update({
        'NAME': url.path[1:],
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port,
    })

    return config


