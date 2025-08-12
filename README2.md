## step 2:

📊  Data Visualization with Apache Superset
✅ Prerequisites & Environment Setup
bash
Copy
Edit
# Create virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install Superset
pip install apache-superset

# Initialize Superset
ℹ️ Ensure PostgreSQL is running and accessible before launching Superset.
--superset db upgrade
--superset fab create-admin
--superset init




🚀 Running Superset (without Docker)
bash
Copy
Edit
superset run -p 8088 --with-threads --reload --debugger


⚠ Common Superset Connection Errors & Fixes
❗ Error Message	
🔍 Reason	✅ Fix



**Could not locate a Flask application**
Cause: Wrong working directory or missing app config
Make sure you're in the virtual environment and run from the correct Superset folder

source venv/bin/activate
cd /path/to/superset_project
superset run

**psycopg2.errors.InvalidPassword**  
Cause: Wrong DB credentials  
Solution: Double-check the username/password

**Driver not found or ClassNotFoundException: org.postgresql.Driver**  
Cause: PostgreSQL JDBC JAR missing for PySpark  
Solution: Add JAR to Spark config:  
--packages org.postgresql:postgresql:42.2.27

**No charts or datasets shown**  
Cause: Connection added but dataset not imported  
Solution: Click ➕ next to the database, choose table, and click "Add"


🐞 Top Connection Errors (PowerShell)
❌ Error: Could not locate a Flask application
✅ Fix:

powershell

$env:FLASK_APP="superset"
superset run -p 8088 --with-threads --reload --debugger
❌ psycopg2 not found
✅ Fix:

pip install psycopg2-binary


📥 Connecting Superset to PostgreSQL
Fill these fields via Superset > Settings > Database > + Database:

Database Name: books_data

Host: localhost

Port: 5432

Username: your_postgres_username

Password: your_postgres_password

Display Name: Books DB

✅ Test Connection → then Save

📈 Creating a Chart (Most Sold Year)
Dataset Used
public.sales_summary

Recommended Chart Type
📊 Bar Chart

Superset Settings:
➕ Query Section
Field	Value
X-axis	year
Metric	SUM(total_sales) or total_sales
Sort By	Metric
Sort Ascending	False
Row Limit	10

🎨 Customize Chart
Option	Value
Chart Title	Top Selling Years
X Axis Title	Year
Y Axis Title	Total Sales
Bar Orientation	Vertical

✅ Click "Run" to generate the chart.

🐞 Troubleshooting Java/Spark for Superset-PySpark-Postgres


# Verify Java
java -version
$env:JAVA_HOME
& "$env:JAVA_HOME\bin\java.exe" -version
python
Copy
Edit
# Add PostgreSQL JDBC in Spark
spark = SparkSession.builder \
    .config("spark.jars.packages", "org.postgresql:postgresql:42.2.27") \
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






