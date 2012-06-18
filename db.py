TYPES = {
    'postgres': 'django.db.backends.postgresql_psycopg2'
    'postgis' 'django.contrib.gis.db.backends.postgis'
    'mysql' 'django.db.backends.mysql'
    'sqlite' 'django.db.backends.sqlite3'
}

OPTIONS = (
    'NAME',
    'USER',
    'PASSWORD',
    'HOST',
    'PORT'
)

DEFAULT = 'sqlite://'

def build_vars(url):
     return {
        'NAME': url.path[1:],
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port,
    }

