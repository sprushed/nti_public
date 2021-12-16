import random
from flask import Flask, render_template, request, render_template_string

app = Flask(__name__, static_folder='./static')

bubliki = ["Lion", "Colt", "Shelly", "Bull", "Dynamike", "Jessie"]
banned = ["{{", "}}"]

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        prep_html = '''
                        {{% extends "base.html" %}}
                        {{% block content %}}
                        <h3> Your BubbleCarder`s name is: {bubbler} </>
                        {{% endblock %}}
                    '''
        bu = random.choice(bubliki)
        bb = request.form.get("Card number")
        li = request.form.get("Full name")
        ki = request.form.get("CVV")

        bubblik = bu + bb + li + ki

        for ban in banned:
            if ban in bubblik:
                bubblik = "We should ban you from BubbleCard :("

        prep_html = prep_html.format(bubbler=bubblik)

        return render_template_string(prep_html)

if __name__ == '__main__':
   app.run(host='0.0.0.0')
