TYPES = {
    'db': 'django.core.cache.backends.db.DatabaseCache',
    'dummy': 'django.core.cache.backends.dummy.DummyCache',
    'file': 'django.core.cache.backends.filebased.FileBasedCache',
    'locmem': 'django.core.cache.backends.locmem.LocMemCache',
    'memcached': 'django.core.cache.backends.memcached.PyLibMCCache'
}

OPTIONS = (
    'LOCATION',
    'PREFIX'
)

DEFAULT = 'locmem://'

def build_vars(url):
    if url.scheme == 'file':
        return {'LOCATION': url.path}
    return {'LOCATION': url.netloc, 'PREFIX': url.path[1:]}

