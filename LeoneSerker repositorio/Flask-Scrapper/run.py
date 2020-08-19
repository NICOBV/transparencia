from flask import Flask
from flask import render_template

app =Flask(__name__)

@app.route('/') #wrap o decorador
def header():
    return render_template("index.html")


app.run()






    
