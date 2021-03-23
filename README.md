# django
need following istallation
	pip install django
	pip install win32api
	pip install mysqlclient (for mysql db only - db used in the code is sqlite)
Config mySql:
	settings.py
	DATABASES = {
			'default': {
					'ENGINE': 'django.db.backends.mysql',
					'NAME': 'schema_name',
					'USER': 'user_name',
					'PASSWORD': 'password',
					'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
					'PORT': '3306',
			}
	}
  
