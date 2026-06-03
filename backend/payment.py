from flask import Flask, send_file, request, redirect, session

app = Flask(__name__)

app.secret_key = "secret"


# PAYMENT PAGE

@app.route("/")
def home():

    return send_file("payment.html")



# PAYMENT BUTTON

@app.route("/pay", methods=["POST"])
def pay():

    session["paid"] = True

    return redirect("/certificate")



# CERTIFICATE PAGE

@app.route("/certificate")
def certificate():

    if session.get("paid") == True:

        return send_file("certificate.html")

    else:

        return "Please pay first"


if __name__ == "__main__":

    app.run(debug=True)