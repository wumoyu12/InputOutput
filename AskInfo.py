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
    global useremail,userpassword;
    useremail=request.form.get('txtusername')
    userpassword=request.form.get('txtpassword')
    
    while (useremail=="" or userpassword==""):
        print(useremail + userpassword)
        return render_template('InputOutput.html', valid="Please enter all information.")
    
    FileConnectivity()
    return render_template('ouput.html', username=useremail, password=userpassword)


def FileConnectivity():
    global exist, filename
    filename = "userinfo.doc"
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    fileexist = bool(path.exists(filename))
    if (fileexist == True):
        WriteFile()
    else:
        CreateFile()
        WriteFile()

def CreateFile():
    pythfile = open(filename, "x")
    pythfile.close();

def WriteFile():
    pythfile = open(filename, "w")
    pythfile.write(useremail + "," + userpassword)
    pythfile.close();

if __name__ == "__main__":
    app.run()
 
