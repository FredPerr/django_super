- Custom user model (email based instead of username based).
- (DEV) Preinstall Sass integration.
-> Must install Dart SASS for it to work.
- (DEV) Preinstall Free FontAwesome.
- Psycopg2 Database setup
- Hidden Configuration from public source files.
- Default core HTML files with easy extending for content and header integration.
- User system which includes password recovery and profile update.
- Basic Styling and functions. 


Setup:
python -m venv venv
[Activate the virtual environment]
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser [... Create a superuser ...]