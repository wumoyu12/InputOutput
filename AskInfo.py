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
    global password, username
    username=request.form.get('txtusername')
    password=request.form.get('txtpassword')
    AddFile()
    print(username + password)

def AddFile():
    filename= username + "info.doc"
    pythfile = open(filename, "w")
    pythfile.write("Usrename:" + username + "\nPassword:" + password)

def ReadFile():
    pythfile = open(filename, "r")
    info=file.readlines()
    print(info)
    
if __name__ == "__main__":
    app.run()
 
