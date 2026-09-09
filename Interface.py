from flask import Flask, render_template, request
import pickle
import pandas as pd

interface = Flask(__name__)

model = pickle.load(open("salary_model.pkl", "rb"))
encoders = pickle.load(open("encoders.pkl", "rb"))

@interface.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        exp = int(request.form["experience"])
        age = int(request.form["age"])
        edu = request.form["education"]
        dept = request.form["department"]
        skill = request.form["skills"]

        edu_enc = encoders["education"].transform([edu])[0]
        dept_enc = encoders["department"].transform([dept])[0]
        skill_enc = encoders["skills"].transform([skill])[0]

        input_df = pd.DataFrame([[exp, age, edu_enc, dept_enc, skill_enc]],columns=['Experience','Age','Education_enc','Department_enc','Skills_enc'])
        print(input_df)

        pred = model.predict(input_df)[0]
        print("Predicted Salary:", pred)
        prediction = f"Rs. {int(pred):,}"

    return render_template("index.html",prediction=prediction,education=encoders["education"].classes_,departments=encoders["department"].classes_,skills=encoders["skills"].classes_)

if __name__ == "__main__":
    interface.run(debug=True)


