from fileinput import filename
import socket
import requests
import ipapi
from flask import Flask, render_template, url_for, redirect, request
import csv
from csv import writer


app = Flask(__name__)

"""
print("Hello WOrld")

ip = '8.8.8.8'
url = "https://ipapi.co/8.8.8.8/json/"

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(hostname, ip_address)

url = "https://ipapi.co/google.com/json/"

a = requests.get(url)
print(a.json())
b = a.json()
print(type(b))

for i, j in b.items():
    print(i, j)
"""

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
    except :
        render_template('error.html')

@app.route('/inputip', methods=["POST", "GET"])
def inputip():
    if request.method == 'POST':
        try:
            ip = request.form['search']
            a = ipapi.location(ip=ip)
            filename='ip-'+ip+'.csv'
            with open(filename,'w', encoding='UTF8') as csvfile:
                csvwriter = csv.writer(csvfile) 
                
                for i,j in a.items():
                    csvwriter.writerow(["Parameter","information"])
                    csvwriter.writerows([i,j])
                csvfile.close()
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
