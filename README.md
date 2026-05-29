# SweetCake Cakeshop

A modern, responsive Django web application for a premium cake bakery, featuring:
- A customer portal with a product gallery and shopping cart.
- An admin portal with customer management, product addition, and stock controls.

---

## Setup and Installation Instructions

Follow these step-by-step instructions to set up and run the project locally on your machine.

### Prerequisites
Make sure you have Python (version 3.8 or higher) and Git installed on your system.

### Step 1: Clone the Repository
Clone the repository using Git and navigate into the project directory:
```bash
git clone https://github.com/sujithtr24/slot4Cakeshop.git
cd slot4Cakeshop
```

### Step 2: Create a Virtual Environment
It is highly recommended to use a virtual environment to manage dependencies.

**On Windows (cmd or PowerShell):**
```bash
python -m venv env
```

**On macOS and Linux:**
```bash
python3 -m venv env
```

### Step 3: Activate the Virtual Environment

**On Windows (cmd):**
```cmd
env\Scripts\activate
```

**On Windows (PowerShell):**
```powershell
env\Scripts\Activate.ps1
```

**On macOS and Linux:**
```bash
source env/bin/activate
```

*(You should now see `(env)` at the beginning of your terminal prompt)*

### Step 4: Install Dependencies
Install all the required Python libraries using the generated `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### Step 5: Run Database Migrations
Create the database tables and prepare the schema:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create an Admin Superuser (Optional)
To access Django's default admin interface, create a superuser account:
```bash
python manage.py createsuperuser
```
Follow the prompts in the terminal to enter a username, email, and password.

### Step 7: Run the Development Server
Start the local Django server:
```bash
python manage.py runserver
```

Open your browser and navigate to:
- **Home / Customer Portal**: [http://127.0.0.1:8000/home/](http://127.0.0.1:8000/home/)
- **Admin Dashboard**: [http://127.0.0.1:8000/adminapp/home/](http://127.0.0.1:8000/adminapp/home/)
- **Django admin portal**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
