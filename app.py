from flask import Flask, render_template

app = Flask(__name__)

app.debug = True

@app.route('/itadmin')
def itadmin():
    return render_template('it-admin.html')

@app.route('/ituser')
def ituser():
    return render_template('it-user.html')

@app.route('/links_it')
def links_it():
    return render_template('links-it.html')

@app.route('/links_management')
def links_management():
    return render_template('links-management.html')

@app.route('/redirect')
def redirect():
    return render_template('redirect.html')

@app.route('/hr')
def hr():
    return render_template('hr.html')

@app.route('/management')
def management():
    return render_template('management.html')

@app.route('/reset')
def reset():
    return render_template('reset.html')

@app.route('/updatelinks')
def updatelinks():
    return render_template('updatelinks.html')

@app.route('/customer')
def customer():
    return render_template('customer.html')

if __name__ == '__main__':
    app.run()
