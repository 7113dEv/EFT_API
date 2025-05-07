from api import app
from api.models import Post


@app.route('/')
def hello():
    return "API is running!"

