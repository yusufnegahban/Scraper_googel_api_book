# 🚀 DEV NOTES - Scraper Google Books Project 📚

### 🔑 Key Points Today:

- **Push Error Fix:**  
  If you get this error:
  It means the remote repo has files you don’t have locally.  
**Fix:**  
```bash
git push -u origin main --force

Ignore Virtual Env & Cache:
Don’t push folders like venv/ or __pycache__/.
Use .gitignore with:

markdown
Copy
Edit
venv/
__pycache__/
To remove them if already pushed:

bash
Copy
Edit
git rm -r --cached venv
git rm -r --cached __pycache__
git commit -m "Remove venv and cache"
git push origin main
Folders Purpose:

scraper/ → main scraping code

test/ → unit tests for code and Flask routes


