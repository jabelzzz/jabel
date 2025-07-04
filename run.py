from app import create_app
from instance.populate_db import populate_database

app = create_app()

populate_database()  # Esto poblará la base de datos en cada arranque

if __name__ == '__main__':
    app.run(debug=True)