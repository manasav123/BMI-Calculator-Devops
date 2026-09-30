from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    bmi = None
    category = None

    if request.method == "POST":
        height = float(request.form["height"]) / 100
        weight = float(request.form["weight"])

        bmi = round(weight / (height * height), 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal Weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

    return render_template("index.html", bmi=bmi, category=category)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)