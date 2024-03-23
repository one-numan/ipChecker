import ipapi
from flask import Flask, render_template, url_for, redirect, request


app = Flask(__name__)


@app.route('/maps')
def maps():
    return render_template("maps.html")


@app.route('/error')
def error():
    return render_template("error.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/myip')
def myip():
    try:
        a = ipapi.location()
        return render_template("myip.html", a=a)
    except:
        render_template('error.html')


@app.route('/inputip', methods=["POST", "GET"])
def inputip():
    if request.method == 'POST':
        try:
            ip = request.form['search']
            a = ipapi.location(ip=ip)
            return render_template('myip.html', a=a)
        except Exception as e:
            print(e)
            return render_template('error.html')


if __name__ == "__main__":
    app.run(debug=True)

"""
Page 
1.Index 
2.myip
3.inputIp [form Redirect]
"""
