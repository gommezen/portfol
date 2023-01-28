from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)#main


@app.route("/")
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["email", "subject", "message"])
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
        try:
            data = request.form.to_dict()#method
            # write_to_file(data) #for the database.txt
            #print(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'









#C:\Users\gomme\myserver>set FLASK_APP=server.py
# to start: C:\Users\gomme\myserver>flask run

#  * Serving Flask app "server.py"
#  * Environment: production
#    WARNING: This is a development server. Do not use it in a production deployment.
#    Use a production WSGI server instead.
#  * Debug mode: off
# server
#  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

#active debug mode in FLASK_ENV=development