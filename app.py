from distutils.log import debug
from operator import truediv
from cgi import print_arguments
from flask import Flask, render_template, request 

#initialise the app
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/predict', methods = ['post'])
def predict():
    first_name= request.form.get("fname")
    last_name= request.form.get("lname")
    email= request.form.get("email")
    phone= request.form.get('phone')

    print(first_name)
    print(last_name)
    print(email)
    print(phone)

    return "form submitted"


#@app.route('/contact')
#def contact():
#    return render_template('contact.html')

#@app.route('/blog')
#def blog():
#    return render_template('blog.html')

#@app.route('/gallery')
#def gallery():
#    return ' welcome to gallery'
#run the app
app.run(debug=True)