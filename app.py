from api import create_app

app = create_app()

@app.route('/')
def hello():
    return "API is running!"

