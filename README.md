# To initialize this project: #

1. Within the project directory, type: `. venv/bin/activate`
2. To run the dev server: `python manage.py rundserver` or `python manage.py rundserver 0.0.0.0:8000`
3. Admin user for /admin is: `admin` / `password`
4. If you need to install some dependancies:
	- ``

---

**When adding new columns to the database, update the model class in models.py, and then run the following commands on the terminal:**
- `python manage.py makemigrations`
- `python manage.py migrate`

---

**To create a new app:**
- `python manage.py startapp <name of app>`
- make sure to add the <name of app> to your `settings.py` file, inside, and at the end of the 'INSTALLED_APPS' list