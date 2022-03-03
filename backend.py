from flask import Flask, render_template

# quick start
app = Flask(__name__)


@app.route('/Home')
def hello_world():
    return render_template('themainfile.html')

@app.route('/about')
def about():
    return 'some info'


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'User name ' + name + ' User id ' + str(id)


if __name__ == "__main__":
    app.run(debug=True)  # чтобы ошибки показывались
