from flask import Flask, render_template

app = Flask(__name__)

app.debug = True

@app.route('/itadmin')
def itadmin():
        return render_template('it-admin.html')

@app.route('/redirect')
def redirect():
    return render_template('redirect.html')

@app.route('/hr')
def hr():
    return render_template('hr.html')

@app.route('/management')
def management():
    return render_template('management.html')

if __name__ == '__main__':
    app.run()
