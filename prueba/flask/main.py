from flask import Flask,redirect,render_template,request,url_for ,jsonify,current_app
import form

app = Flask(__name__)

@app.route('/',methods=['POST',"GET","PUT"])
def index():
    instancia = form.CommentForm()
    return render_template("index.html",form=instancia)

app.run(debug=True)