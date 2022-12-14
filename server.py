from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/success')
def success():
    return "Success"

@app.route('/lists')
def lists():
    
    student_info = [
        
        {'first_name' : 'Michael', 'last_name' : 'Choi', 'full_name': 'Michael_Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin', 'full_name': 'John_Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen', 'full_name':'Mark_Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel', 'full_name': 'KB_Tone1'}
    ]
    return render_template("index.html", students = student_info)

if __name__=="__main__":
    app.run(debug=True)
    