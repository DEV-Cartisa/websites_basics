from flask import Flask, redirect, url_for, render_template 

app = Flask(__name__)

@app.route("/<name>")
def home(name):#coding the pages - the home page [ will be functions ]
    return render_template("index.html", content=name)


if __name__ == "__main__":
    app.run()


#render_template - can grab html file , that will render as our template 

 













