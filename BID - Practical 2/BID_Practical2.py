import csv
from flask import Flask, render_template, request

app=Flask(__name__)

app.secret_key='12345'

@app.route('/')
def webpage():
    return render_template('form.html')


@app.route('/process',methods=['POST'])
def process():
    fname=request.form['fname']
    lname=request.form['lname']
    noOfPeople=request.form['noOfPeople']
    seatType=request.form['seatType']

    

    with open('bid2.csv', 'a') as csvfile:
       csv_writer= csv.writer(csvfile)
       #csv_writer.writerow(['Firstname','Lastname','No Of People','Seat Type'])
       csv_writer.writerow([fname,lname,noOfPeople,seatType])
    return 'Records Inserted'

    
        

        






if __name__=='__main__':
    app.run(debug=True)