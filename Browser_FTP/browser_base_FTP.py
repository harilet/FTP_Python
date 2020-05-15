from flask import Flask,render_template,redirect,url_for
from flask import send_file
from os import listdir, getcwd,system,chdir
import socket
from os.path import isfile

app = Flask(__name__)
title="Files"
port=5000

## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)
## printing the  ip_address
ip1={ip_address}
for i in ip1:
    ip=i

@app.route('/')
def index ():
    files = listdir(getcwd())
    return render_template('page_temp.html',items=files,title=title,port=port,ip=ip)


@app.route('/download/<file>')
def downloadFile (file):
    if isfile(file):
        path = getcwd()+"/"+file
        return send_file(path, as_attachment=True)
    else:
        chdir(file)
        return redirect(url_for('index'))

@app.route('/backtrack')
def back ():
    chdir("..")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host=ip,port=port,debug=True)
