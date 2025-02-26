import os.path
from os import path
from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def main():
    if request.method == 'GET':
        return render_template('InputOutput.html')
    else:
        GetInfo()
        return render_template('InputOutput.html')

@app.route('/info', methods=['GET', 'POST'])
def GetInfo():
    global useremail, userpasswod;
    useremail=request.form.get('txtusername')
    userpassword=request.form.get('txtpassword')
    
    print(useremail + userpasswod)
    FileConnectivity()
    
    return render_template('ouput.html', username=useremail, password=userpassword)

def FileConnectivity():
    filename = "userinfo.doc"
    pythfile = open(filename, "w")
    pythfile.write("User Email:" + useremail + "Password:" + userpasswod)
    pythfile.close();

if __name__ == "__main__":
    app.run()
 
