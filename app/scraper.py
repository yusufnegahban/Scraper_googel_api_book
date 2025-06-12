import requests
from .models import Book
from . import db
from . import create_app

def scrape_books_from_google_api(query="python programming", max_pages=2):
    print("Scraping started...")
    base_url = "https://www.googleapis.com/books/v1/volumes"
    books_added = 0

    for page in range(max_pages):
        params = {
            'q': query,
            'startIndex': page * 10,
            'maxResults': 10
        }
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            items = data.get('items', [])
            for item in items:
                volume_info = item.get('volumeInfo', {})
                sale_info = item.get('saleInfo', {})

                title = volume_info.get('title', 'Unknown Title')
                authors = volume_info.get('authors', ['Unknown Author'])
                published_date = volume_info.get('publishedDate', '')
                industry_identifiers = volume_info.get('industryIdentifiers', [])
                isbn = None
                for identifier in industry_identifiers:
                    if identifier.get('type') == 'ISBN_13':
                        isbn = identifier.get('identifier')
                        break
                if not isbn:
                    isbn = 'Unknown ISBN'
                price = 0.0
                if sale_info.get('saleability') == 'FOR_SALE':
                    price_info = sale_info.get('listPrice', {})
                    price = price_info.get('amount', 0.0)

                # Check if book already exists
                if not Book.query.filter_by(title=title, author=authors[0]).first():
                    new_book = Book(
                        title=title,
                        author=authors[0],
                        published_date=published_date,
                        isbn=isbn,
                        price=price
                    )
                    db.session.add(new_book)
                    books_added += 1
        else:
            print(f"Error fetching page {page + 1}: {response.status_code}")

    db.session.commit()
    print(f"{books_added} books scraped and stored.")

    if books_added > 0:
        print("✅ Scraping was successful!")
    else:
        print("⚠️ No new books were added.")

if __name__ == "__main__":
    app = create_app()  # <-- Create the app
    with app.app_context():  # <-- Use the app context
         scrape_books_from_google_api(max_pages=50)