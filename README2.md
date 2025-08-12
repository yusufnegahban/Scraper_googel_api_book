
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


---

Top Connection Errors (PowerShell)
❌ Error: Could not locate a Flask application
✅ Fix:

powershell
Copy
Edit
$env:FLASK_APP="superset" superset run -p 8088 --with-threads --reload --debugger
❌ psycopg2 not found
✅ Fix:

bash
Copy
Edit
pip install psycopg2-binary

---


📥 Connecting Superset to PostgreSQL
Fill these fields via Superset > Settings > Database > + Database:

Database Name: books_data

Host: localhost

Port: 5432

Username: your_postgres_username

Password: your_postgres_password

Display Name: Books DB

✅ Test Connection → then Save

---

##Troubleshooting Java/Spark for Superset-PySpark-Postgres
Verify Java
bash
Copy
Edit
java -version
$env:JAVA_HOME & "$env:JAVA_HOME\bin\java.exe" -version
Add PostgreSQL JDBC in Spark
python
Copy
Edit
spark = SparkSession.builder \
    .config("spark.jars.packages", "org.postgresql:postgresql:42.2.27") \
    .getOrCreate()

---

##Stage 3 – Airflow Environment Setup
Navigate to project directory

powershell
Copy
Edit
cd D:\manager_Safak\googel_book\airflow_project
Activate virtual environment

powershell
Copy
Edit
.\venv\Scripts\activate
Set Airflow UID in .env file

powershell
Copy
Edit
Set-Content -Path .env -Value "AIRFLOW_UID=50000" -Encoding ASCII
Initialize Airflow

powershell
Copy
Edit
docker-compose up airflow-init

