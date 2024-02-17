ALLOWED_HOSTS = ["*"]

# Modules in use, commented modules that you won't use
MODULES = [

]
BASEURL = 'http://localhost:8000'
APIS = {

}



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cuidameDB',
        'USER': 'postgres',
        'PASSWORD':'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256