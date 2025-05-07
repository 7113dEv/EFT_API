from api import app



@app.route('/')
def hello():
    return "API is running!"

