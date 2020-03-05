from flask import Flask


app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    return 'login page'


if __main__ == '__name__':
    app.run()
