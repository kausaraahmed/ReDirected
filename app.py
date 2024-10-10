from flask import Flask, render_template, redirect

app = Flask(__name__)

database = {
    "github": "https://github.com/kausaraahmed",
    "schedulumos": "https://cpuscheduler.vercel.app/",
    "schedulumos-gh": "https://github.com/kausaraahmed/ScheduLumos",
}

@app.route("/")
def home():
    return "Welcome to ReDirected! To know more about the project, visit: \"https://github.com/kausaraahmed/ReDirected\""


@app.route("/<keyword>")
def redirect_to_user_url(keyword):
    link = database.get(keyword)

    if link:
        return redirect(link)
    else:
        return "URL not found", 404


if __name__ == "__main__":
    app.run(debug=True)

