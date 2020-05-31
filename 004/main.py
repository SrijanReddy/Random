from flask import Flask, render_template      
from data import generate
from data_abs import generate_abs
from data_poor import generate_poor

app = Flask(__name__)

@app.route('/')
def home():
	return render_template("temp.html")
    
@app.route('/poor')
def poor():
	label,link=generate_poor()
	print(link)
	print(label)
	return render_template("poor.html",var1=link,var2=label)

@app.route('/index')
def index():
	label,link=generate()
	print(link)
	print(label)
	return render_template("index.html",var1=link,var2=label)

@app.route('/abs')
def abs():
	label,link=generate_abs()
	print(link)
	print(label)
	return render_template("abs.html",var1=link,var2=label)

    
if __name__ == "__main__":
    app.run(debug=True)