import sys
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
    
def GetInfo():
{
    global username, userpasswod;
    print("I am GrtInfo");
    useremail=request.form.get('txtusername')
    userpassword=request.form.get('txtpassword')
    AddFile()
    print(username + password)
}

def AddFile():
    filename= username + "info.doc"
    pythfile = open(filename, "w")
    pythfile.write("Usrename:" + username + "\nPassword:" + password)
    
    FileConnectivity()
    return render_template('frmOutput.html', username=useremail)

if __name__ == "__main__":
    app.run()
 
