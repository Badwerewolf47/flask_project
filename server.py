from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html", name="Jim")

@app.route("/user/<id>/")
def user_profile(id):
	
	return "Profile page of user #{}".format(id)




if __name__ == "__main__":
    app.run(host="194.87.206.56", port = 80)
