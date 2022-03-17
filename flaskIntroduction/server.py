#If using VS Code install python extension from windows store
#If using gitbash type python into CL and follow instructions
#Create dir for project and cd into new dir
#In the command line type pip install virtualenv
#Next type pip install flask
#Link to tutorialhttps://pythongeeks.org/python-flask-introduction/?msclkid=76af1255a5e511ec86fedbd75138cd17
#imports flask
from flask import Flask

#creates the app that hosts the application 
app = Flask(__name__)

#defines routes
@app.route('/')
def index():
        return 'Flask Introduction!'
@app.route('/greet<name>')
def greet(name)

#calls main
if __name__ =='__main__':
    app.debug=True #setting the debugging option 

#spin up the server! 
#type into the CL python <file-name>.py
app.run()
#app.run(host='0.0.0.0', port=81)
