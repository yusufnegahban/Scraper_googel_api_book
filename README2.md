
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


⚠ Common Superset Connection Errors & Fixes
Error Message	Cause	Fix
Could not locate a Flask application	Wrong working directory or missing app config	Make sure you're in the virtual environment and run from the correct Superset folder:
```bash
source venv/bin/activate
cd /path/to/superset_project
superset run
```
psycopg2.errors.InvalidPassword	Wrong DB credentials	Double-check the username/password
Driver not found or ClassNotFoundException: org.postgresql.Driver	PostgreSQL JDBC JAR missing for PySpark	Add JAR to Spark config:
```bash
--packages org.postgresql:postgresql:42.2.27
```
No charts or datasets shown	Connection added but dataset not imported	Click ➕ next to the database, choose table, and click "Add"




