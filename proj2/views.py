
from flask import Flask, request, redirect, url_for
app = Flask(__name__)

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":

        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # Alternatively

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        return redirect(request.url)

    return render_template("public/sign_up.html")

if__name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

