# 📚 Flask Web App – Mini Bookstore Demo

A cool app that scrapes book info from a website, stores it in a database, and shows it on a simple web page.  
It’s like a mini online bookstore! 

![screenshot](preview.png) <!-- replace preview.png with your image file name -->

---

[🔗 Live Demo](https://your-live-demo-link.com) &nbsp;&nbsp;&nbsp;  
[📂 GitHub Repo](https://github.com/yourusername/your-repo-name) &nbsp;&nbsp;&nbsp;  
[📽️ Demo Video](https://your-video-link.com)

---

## 🚀 What We Did
**Flask App Structure 📚**

-The create_app function builds the Flask app foundation 🏛️:

-Sets up the app with a PostgreSQL database connection 🗄️.

-Fetches data using a scraper from the Google Books API 📦.

**Displays data via:**

Route (main_bp): Shows books in a pretty HTML page 🌐.

API (api_bp): Sends raw JSON data for other apps 🚀.


### 1️⃣ Data Scraping
- Used **Python**, `requests`, and `BeautifulSoup` to grab book info from [books.toscrape.com](http://books.toscrape.com)
- Scraped:
  - Book Title
  - Author *(improved later)*
  - Price
  - Availability
  - Publish Date
  - ISBN
- Handled **pagination** to scrape all pages one by one  
  📄 ➡️ 📄 ➡️ 📄

---

### 2️⃣ Data Storage
- Used **PostgreSQL** to keep the data safe and organized
- Created a `Book` model with **SQLAlchemy** to store book details in tables

---

### 3️⃣ Flask Web App
- Built a simple **Flask** app to display books in a neat table
- Added **search** to find books by title or author 🔎
- Added **pagination** (10 books per page)
- Made a **detail page** to show full info of each book 📖

---

### 4️⃣ REST API
- Created a RESTful API that serves book data in **JSON** format
- Now you can use the API for other apps or future projects

---

### 5️⃣ Testing & Code Quality
- Wrote basic tests using **pytest** to ensure the main page and API work ✅
- Kept code **clean**, **modular**, and **maintainable**

---

### 6️⃣ Git & Version Control
- Used **Git** to track project changes
- Made **clear and descriptive commits** for every step
- Created **branches and pull requests** like pros ✨

---

## 🛠️ How to Run

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/your-repo-name

# 2. Navigate into the project directory
cd your-repo-name

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py




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





