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
