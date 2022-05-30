from flask import Flask, render_template
app = Flask(__name__)

#in the function return render_template(‘index.html’)

@app.route("/studentForm")
def student_webpage():
    #Create a variable
    name = 'Sridatta'
    # Pass the variable in the template
    return render_template('/studentForm.html', student_name = name)
app.run(debug=True)