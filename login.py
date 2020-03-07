from flask import Flask


app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    num1 = 10
    num2 = 200
    num3 = 30
    return 'login page'


if __main__ == '__name__':
    app.run()
