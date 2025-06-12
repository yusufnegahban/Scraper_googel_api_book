from scraper.book_scraper import fetch_books
def test_fetch_books_returns_list():
    books = fetch_books()
    assert isinstance(books, list)
    assert len(books) > 0
