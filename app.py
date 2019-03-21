from flask import Flask
from flask_mako import render_template, MakoTemplates

mako = MakoTemplates()

app = Flask(__name__)
mako.init_app(app)


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
