ENVIRONMENT = 'production'

if ENVIRONMENT == 'production':
    URL = 'https://www.google.com/'
    USERNAME = 'production_user'
    PASSWORD = 'production_password'
elif ENVIRONMENT == 'development':
    USERNAME = 'development_user'
    PASSWORD = 'development_password'
else:
    USERNAME = 'default_user'
    PASSWORD = 'default_password'
