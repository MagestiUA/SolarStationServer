release: python manage.py migrate
web: gunicorn SolarStationServer.wsgi --bind=0.0.0.0:$PORT
worker: celery -A SolarStationServer worker --loglevel=info
beat: celery -A SolarStationServer beat --loglevel=info
