# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-3f2wxt7c_c6+my=nmhk3d7smza&0g^e8(u@^-42!%9uok8==o'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'datarestdb',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
