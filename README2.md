## step 2:

📊 Step 3: Data Visualization with Apache Superset
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
superset db upgrade
superset fab create-admin
superset init
ℹ️ Ensure PostgreSQL is running and accessible before launching Superset.

🚀 Running Superset (without Docker)
bash
Copy
Edit
superset run -p 8088 --with-threads --reload --debugger


⚠ Common Superset Connection Errors & Fixes
❗ Error Message	🔍 Reason	✅ Fix
Could not locate a Flask application	Wrong working directory or missing app config	Ensure you're in the venv and run from a correct initialized Superset folder
psycopg2.errors.InvalidPassword	Wrong DB credentials	Double-check the username/password
Driver not found or ClassNotFoundException: org.postgresql.Driver	PostgreSQL JDBC JAR missing for PySpark	Add JAR to Spark config:
--packages org.postgresql:postgresql:42.2.27
No charts or datasets shown	Connection added but dataset not imported	Click ➕ next to the database, choose table, and click "Add"

🐞 Top Connection Errors (PowerShell)
❌ Error: Could not locate a Flask application
✅ Fix:

powershell
Copy
Edit
$env:FLASK_APP="superset"
superset run -p 8088 --with-threads --reload --debugger
❌ psycopg2 not found
✅ Fix:

bash
Copy
Edit
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
bash
Copy
Edit
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





