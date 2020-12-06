from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/main')
@app.route('/front/templates/main_page.html')
def index():
    return render_template('main_page.html')


if __name__ == '__main__':
    app.run(debug=True)
