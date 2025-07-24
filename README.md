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


step 2:

📘 Superset + Spark + PostgreSQL Project Summary
A full week of data engineering & visualization steps

⚙️ Part 1: Spark + PostgreSQL Integration
🔧 Environment Setup
powershell
Copy
Edit
$env:JAVA_HOME
& "$env:JAVA_HOME\bin\java.exe" -version

$env:HADOOP_HOME
& "$env:HADOOP_HOME\bin\winutils.exe" ls

$env:SPARK_HOME
& "$env:SPARK_HOME\bin\spark-shell.cmd"
✅ Sample Output
text
Copy
Edit
Welcome to Spark 4.0.0
Spark context available as 'sc'
Spark session available as 'spark'
🐘 PostgreSQL + Spark via JDBC
✅ Fixed missing driver: ClassNotFoundException: org.postgresql.Driver

🔗 Added .jar via spark.jars.packages

✅ Read data using:

scala
Copy
Edit
spark.read
  .format("jdbc")
  .option("url", "jdbc:postgresql://localhost:5432/books_data")
  .option("dbtable", "books")
  .option("user", "postgres")
  .option("password", "your_password")
  .load()
📊 Aggregated book sales by year in PySpark

📁 Saved output to PostgreSQL: sales_summary table

📊 Part 2: Superset Installation & Visualization
🧰 Superset Setup (Virtualenv)
bash
Copy
Edit
pip install apache-superset
superset db upgrade
superset fab create-admin
superset init
superset run -p 8088
🧱 (Optional) Frontend Build
bash
Copy
Edit
yarn install
yarn build
🐘 PostgreSQL Connection
➕ Added Database:
postgresql://postgres:your_password@localhost:5432/books_data

✅ Clicked "Test Connection" → Success

🔄 Created Dataset from sales_summary table

📈 Chart Creation Example
Chart Type: Bar Chart
Dataset: sales_summary

Setting	Value
X-Axis	year
Y-Axis (Metric)	total_quantity
Filters	none
Limit	1000

✅ Saved chart → Added to dashboard: "Book Sales Overview"

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
❌ Database not shown in SQL Lab
✅ Fix:

Reload metadata

Ensure table is saved as a dataset

Assign correct schema

❌ Address already in use
✅ Fix:

bash
Copy
Edit
taskkill /F /IM python.exe
✅ Recap Workflow
css
Copy
Edit
PostgreSQL → PySpark → Aggregated Data → Saved to DB → Superset → Chart → Dashboard
🔐 Login Flow
Localhost: http://localhost:8088

Admin: Created via superset fab create-admin

Data loaded with:

bash
Copy
Edit
superset load_examples
🧠 Bonus Tips
✅ Run Superset from root folder: .superset

⚠ If debugger needed, always set FLASK_APP

🧹 Clear browser cache for CSRF/login issues
