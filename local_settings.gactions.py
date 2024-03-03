from pathlib import Path

ALLOWED_HOSTS = ["*"]

# Modules in use, commented modules that you won't use
MODULES = [

]
BASEURL = 'http://localhost:8000'
APIS = {

}

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256