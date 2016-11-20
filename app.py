from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return 'Flask is running!'


@app.route('/data')
def names():
    data = {
        "first_names": ["John", "Jacob", "Julie", "Jennifer"],
        "last_names": ["Connor", "Johnson", "Cloud", "Ray"],
        "nick_names": ["Joe", "Jac", "Ju", "J"]

    }
    return jsonify(data)


if __name__ == '__main__':
    app.run()
