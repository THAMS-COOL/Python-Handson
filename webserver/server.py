from flask import Flask, render_template, request, redirect
import csv
   
app = Flask(__name__)
print(__name__)

#__name__

@app.route('/')
def my_home():
    return render_template('index.html')


# @app.route('/<username>/<int:post_id>')
# def variable_rules(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)

 

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)



def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data["message"]
        print(email, subject, message)
        file = database.write(f'\n{email}, {subject}, {message}')



def write_to_csv(data):
    with open('database.csv ', mode='a') as database2:
        email = data['email']
        print(email)
        subject = data['subject'] 
        message = data["message"]
        print(email, subject, message)
        csv_writer = csv.writer(database2, delimiter=',', quoting=csv.QUOTE_MINIMAL )
        csv_writer.writerow([email,subject,message])





@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():    
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        write_to_file(data)
        write_to_csv(data)
        print(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong!!! Please try again'


if __name__ == '__main__':
    app.run(debug=True)


 
# @app.route('/about.html')
# def blog():
#     return render_template('about.html')
