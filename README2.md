
    ...


    # Step 2:  
📊 **Data Visualization with Apache Superset**  

---

## ✅ Prerequisites & Environment Setup  

### Create virtual environment  
```bash
python -m venv venv
.\venv\Scripts\activate


Install Superset
pip install apache-superset

Initialize Superset
ℹ️ Ensure PostgreSQL is running and accessible before launching Superset.

superset db upgrade
superset fab create-admin
superset init


🚀 Running Superset (without Docker)

superset run -p 8088 --with-threads --reload --debugger

🐞 Top Connection Errors (PowerShell)
❌ Error: Could not locate a Flask application
✅ Fix:

powershell
Copy
Edit
$env:FLASK_APP="superset" superset run -p 8088 --with-threads --reload --debugger





