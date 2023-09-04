from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/mypage/me")
def about():
    return render_template('omnie.html')

@app.route("/mypage/contact", methods=["POST", "GET"])
def about2():
    if request.method == "POST":
        user = request.form["nick"]
        return redirect(url_for("test", nick=user))
    else:
        return render_template('contact.html')
    
@app.route("/<nick>")
def test(nick):
    return f"Dziękujemy za kontakt {nick}"

if __name__ == "__main__":
    app.run()




