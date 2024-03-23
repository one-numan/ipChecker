from flask import Flask, render_template, url_for, redirect, request
import ipapi  # Library


app = Flask(__name__)


@app.route('/')
def index():
    """Home Page 

    Returns:
        Render HTML Page: Index.html 
    """
    return render_template("index.html")


@app.route('/error')
def error():
    """Exceptional Page 
    If Any Error Occurs This Page Will be Rendered

    Returns:
       Render HTML Page: error.html 
    """
    return render_template("error.html")


@app.errorhandler(404)
def page_not_found(e):
    """If Page Not Found : 404

    Args:
        e (404): Not Found

    Returns:
        Render HTML Page: error.html 
    """
    return render_template("error.html")


@app.route('/myip')
def myip():
    """Render Page If Your Want to see Our Own IP
    1. Call Function ipapi.location()
    2. This Function Return dict_ip [Key:Value]
    3. Pass this dict_ip into Html Page

    If Any Exception Occurs Render Error Page
    Returns:
        Render HTML Page: myip.html with Dict_ip
    """
    try:
        # Call Function ipapi.location()
        my_own_ip = ipapi.location()
        # This Function Return dict_ip [Key:Value]
        #  Pass this dict_ip into Html Page
        return render_template("myip.html", dict_ip=my_own_ip)
    except:
        # Exceptional Error
        render_template('error.html')


@app.route('/inputip', methods=["POST", "GET"])
def inputip():
    """Taking Users input IP and Find Its IP
    1. Taking User Input IP from Form
    2. Call Function and passing IP as Parameter ipapi.location(<ip>)
    3. This Function Return dict_ip [Key:Value]
    4. Pass this dict_ip into Html Page
    Returns:
        _type_: _description_
    """
    if request.method == 'POST':
        try:
            # Taking User Input IP from Form
            user_input = request.form['search']
            # Call Function and passing IP as Parameter ipapi.location(<ip>)
            # This Function Return dict_ip [Key:Value]
            input_ip = ipapi.location(ip=user_input)
            # Pass this dict_ip into Html Page
            return render_template('myip.html', dict_ip=input_ip)
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
