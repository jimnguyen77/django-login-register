# To initialize this project: #

1. Type: `python3 -m venv venv`
2. Next, type: `. venv/bin/activate`
3. Finally, type: `pip install -r requirements.txt`
4. To run the dev server, `cd` into the project directory (mybooking_website) and type: `python manage.py rundserver` or `python manage.py rundserver 0.0.0.0:8000`
5. Admin user for /admin is: `admin` / `password`

---

**When adding new columns to the database, update the model class in models.py, and then run the following commands on the terminal:**
- `python manage.py makemigrations`
- `python manage.py migrate`

---

**To create a new app:**
- `python manage.py startapp <name of app>`
- make sure to add the <name of app> to your `settings.py` file, inside, and at the end of the 'INSTALLED_APPS' list