from flask import Flask, render_template, request
import os, sys
sys.path.append('static/python/')
import truth_table, relations


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('pages/placeholder.home.html')


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')


@app.route('/truth_table', methods=['GET', 'POST'])
def truth():
    if request.method == 'GET':
        return render_template('pages/placeholder.truth_table.html', result=None)
    data = request.form.get('formula')
    return render_template('pages/placeholder.truth_table.html', result=truth_table.start(data))


@app.route('/worshell', methods=['GET', 'POST'])
def worshell():
    if request.method == 'GET':
        return render_template('pages/placeholder.worshell.html')


@app.route('/relations', methods=['GET', 'POST'])
def relations():
    if request.method == 'GET':
        return render_template('pages/placeholder.relations.html', result=None)
    data = request.form.get('relation')
    return render_template('pages/placeholder.relations.html', result=relations.matrix_check(data))


@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


if __name__ == '__main__':
    app.run()