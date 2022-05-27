from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method=="GET":
        return render_template('home.html')
    elif request.method=="POST":
        from_textbar=request.form["first_last"]
        here_go = request.form.getlist('here_go') #check boxes
        tortilla_flavor = request.form['tortilla_flavor'] #radio buttons
        rice_flavor = request.form['rice_flavor'] #radio buttons
        bean_flavor = request.form['bean_flavor'] #radio buttons
        protein_flavor = request.form['protein_flavor'] #radio buttons
        extras = request.form.getlist('extras') ['Cheese', 'Sour Cream', 'Guacamole', 'Pico de Gallo', 'Fajita Veggies', 'Corn Salsa' ] #check boxes
        print(extras)
        return render_template("home.html", from_textbar=from_textbar, here_go=here_go, tortilla_flavor=tortilla_flavor, rice_flavor=rice_flavor,bean_flavor=bean_flavor, protein_flavor=protein_flavor, extras=extras)



app.run(debug=True)