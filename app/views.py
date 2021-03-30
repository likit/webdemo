from wsgi import app


@app.route('/')
def index():
    return 'Welcome to the index page'