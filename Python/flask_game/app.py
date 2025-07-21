from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'some_secret_key'  # potrzebne do działania sesji

@app.route("/", methods=["GET", "POST"])
def index():
    # Jeśli nie mamy jeszcze wylosowanej liczby, losujemy ją
    if "secret_number" not in session:
        session["secret_number"] = random.randint(1, 10)
        session["attempts"] = 0

    message = ""

    if request.method == "POST":
        guess = request.form.get("guess")

        if guess:
            try:
                guess = int(guess)
                session["attempts"] += 1

                if guess == session["secret_number"]:
                    message = f"🎉 You guessed it in {session['attempts']} attempts!"
                    # reset gry po zgadnięciu
                    session.pop("secret_number")
                    session.pop("attempts")
                elif guess < session["secret_number"]:
                    message = "Too low! Try again."
                else:
                    message = "Too high! Try again."
            except ValueError:
                message = "Please enter a valid number."
        else:
            message = "Please enter a number."

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)