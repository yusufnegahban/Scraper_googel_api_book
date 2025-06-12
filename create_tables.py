from app import create_app, db
from app.models import Book
from sqlalchemy.exc import SQLAlchemyError

app = create_app()

with app.app_context():
    try:
        db.create_all()
        print("✅ Tables created successfully.")
    except SQLAlchemyError as e:
        print("❌ Error creating tables:")
        print(e)




