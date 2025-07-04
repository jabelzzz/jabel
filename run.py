from app import create_app

app = create_app()

# TODO - Change to False when deploying
if __name__ == '__main__':
    app.run(debug=True)