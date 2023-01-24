from flask import Flask,render_template,request
from Project_app.utils import SpeciesClass

# Creating flask app
app = Flask(__name__)

#Home Page
@app.route("/")
def home():
    return render_template("home.html")

#Result Page
@app.route("/predict", methods=["post"])
def predict():
    data = dict(request.form).values()
    Species = SpeciesClass(data)
    result = Species.predict_species()
    return render_template("result.html",res=result)
    
    
if __name__=="__main__":
    app.run(debug=True)