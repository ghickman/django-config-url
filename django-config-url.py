# -*- coding: utf-8 -*-

import os
import urlparse


# loop backend.* modules and get TYPES, add them to netloc here
urlparse.uses_netloc.append('db')

DEFAULT_ENV = 'CACHE_URL'

def config(env=DEFAULT_ENV, default='locmem://'):
    """Returns configured CACHES dictionary from CACHE_URL"""
    config = {}

    s = os.environ.get(env, default)

    if s:
        config = parse(s)

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


