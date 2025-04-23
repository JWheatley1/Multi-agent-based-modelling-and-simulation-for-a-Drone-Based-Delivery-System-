python3.11 -m venv venv
source venv/bin/activate
cd dronehackon
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runsurver



