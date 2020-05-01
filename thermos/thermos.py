from flask import Flask, render_template, url_for

app = Flask(__name__)


class User:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def initials(self):
        return f"{self.name[0]}. {self.lastname[0]}."


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', text=['Welcome,...', 'Secondly,...', 'Also,...'], user=User("John", "Wick"))


@app.route('/add')
def add():
    return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)
