from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/nirmesh")

def hello():
    #return "Hello Nirmesh again"
    return render_template("/index.html")


@app.route("/sub",methods=["POST"])

def submit():
    if request.method=="POST" :
        name=request.form["username"]
    return render_template("/submit.html",n=name)


if __name__=="__main__":
    app.run(debug=True)
