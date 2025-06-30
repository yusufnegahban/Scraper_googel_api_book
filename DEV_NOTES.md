# 🚀 DEV NOTES - Scraper Google Books Project 📚

### 🔑 Key Points Today:

- **Push Error Fix:**  
  If you get this error:
  It means the remote repo has files you don’t have locally.  
**Fix:**  
```bash
git push -u origin main --force



googel_book/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── scraper.py
│   ├── api.py
│   └── templates/
│       └── index.html
│
├── create_tables.py
├── run.py
├── requirements.txt
└── README.md

http://127.0.0.1:5000/api/books

**How to fix:**
You are getting `ModuleNotFoundError: No module named 'app'` because Python does not see your app folder as a package when running the script this way.



### Solution 1: Set PYTHONPATH

Before running your script, set the `PYTHONPATH` to your project root:

```powershell
$env:PYTHONPATH = "D:\manager_k\googel_book"
python app/scraper.py
```

---

### Solution 2: Run as a module

Change your imports in scraper.py to **relative imports**:

```python
from .models import Book
from . import db
```

Then run from the project root with:

```powershell
python -m app.scraper
```

---

**Summary:**  
- For `python app/scraper.py` use `from app.models import Book` and set `PYTHONPATH`.
- For `python -m app.scraper` use `from .models import Book`.

Pick one method and make sure your imports and run command match!


-----------------
Great! Your code is working and scraping 18 books.  
If you want to scrape **more books**, you need to increase the `max_pages` parameter in your function call.

For example, to scrape 100 books (10 books per page × 10 pages):

```python
if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        scrape_books_from_google_api(max_pages=10)  # Scrape 10 pages (about 100 books)
```

You can set `max_pages` to any number you want.  
**Each page usually returns up to 10 books.**

If you want to scrape, for example, 50 pages (about 500 books):

```python
scrape_books_from_google_api(max_pages=50)
```

Just change the number in `max_pages` to your desired amount!

----------------------------

Great question!  
Here’s the difference:

---

### 1. **scraper.py**
- You run `scraper.py` **only when you want to fetch (scrape) new books from Google and save them to your database**.
- This script is for updating your database with new data.

---

### 2. **run.py**
- You run run.py **to start your Flask web app** and show the data (books) in your browser.
- This script is for running your website and displaying the books already in your database.

---

**Summary:**  
- To **scrape new data**: run `scraper.py`
- To **show data on your app**: run run.py

---------------------------------
The message **"Not Found. The requested URL was not found on the server."** means your Flask app is running, but there is no route defined for the URL you visited (probably `/`).

**How to fix:**

1. **Check your `routes.py`:**
   Make sure you have a route for `/` like this:
   ```python
   @main_bp.route("/")
   def home():
       # your code here
   ```

2. **Register your blueprint in `__init__.py`:**
   In your __init__.py, after creating the app, add:
   ```python
   from .routes import main_bp
   app.register_blueprint(main_bp)
   ```

3. **Restart your Flask app** after making changes.

---

**Summary:**  
- Make sure you have a route for `/` in your `routes.py`.
- Make sure the blueprint is registered in `__init__.py`.
- Restart your app and try again.

-----------------------------
# 🚀 Upload Project Folder to GitHub

### 1️⃣ Open terminal in your project folder:

```bash
git init
git add .
git commit -m "first commit"

2️⃣ Create a new repo on GitHub. Copy its URL.
3️⃣ Back in terminal:
git remote add origin <your-repo-url>
git push -u origin main

