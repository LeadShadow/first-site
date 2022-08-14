from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/')
@app.route('/main')
def main_page():
    return render_template('main.html')


@app.route('/catalog')
def catalog():
    return render_template('page_catalog.html')


if __name__ == "__main__":
    app.run(debug=True)
