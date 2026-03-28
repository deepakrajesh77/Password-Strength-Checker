from flask import Flask, render_template, request
from password_check import check_password_strength
from breach_check import check_breach

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    description = None
    breach = None

    if request.method == 'POST':
        password = request.form.get("password")

        prediction = check_password_strength(password)
        breach = check_breach(password)

        # Optional description (you can customize)
        if prediction == "Strong":
            description = "Your password is strong and secure."
        elif prediction == "Medium":
            description = "Your password is okay, but can be improved."
        else:
            description = "Your password is weak. Try adding symbols, numbers, and uppercase letters."

    return render_template("index.html",
                           prediction=prediction,
                           description=description,
                           breach=breach)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=10000)