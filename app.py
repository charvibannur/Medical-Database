from flask import Flask, redirect, url_for, request, render_template


from backend import *
app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main_page.html')

@app.route('/orderfood', methods=["GET", "POST"])
def orderfood():
    global food
    if request.method == "POST":
        patient_list()
        name = request.form.get("name")
        address = request.form.get("address")
        pin= request.form.get('pin')

        number = request.form.get('number')
        suggestions = request.form.get("suggestions")
        if len(number)!=10 or len(pin)!=6:
            return redirect(url_for("details"))
        else:
            create_patient(int(number),name,address,int(pin),suggestions)
            return redirect(url_for('orderconfirmation'))

    return render_template("orderfood.html")

@app.route('/details', methods=["GET", "POST"])
def details():
    return render_template("details.html")

@app.route('/volunteer', methods=["GET", "POST"])
def volunteer():
    if request.method == "POST":
        name = request.form.get("name")
        address = request.form.get("address")
        quantity = request.form.get("quantity")
        pin= request.form.get('pin')
        number = request.form.get('number')
        password = request.form.get('password')
        option = request.form.get('option')
        if option == 'AVAILABLE':
            status='AVAILABLE'
        elif option == 'UNAVAILABLE':
            status='UNAVAILABLE'
        else:
            pass
        if len(number)!=10 or len(pin)!=6:
            return redirect(url_for('details'))
        else:
            registration_hospital(name,password,address,int(pin),int(number),status)
            return redirect(url_for('registerconfirmation'))

    return render_template("volunteer.html")

@app.route('/signin', methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        hospital_list()
        patients = sign_in(username, password)
        if patients:
            return redirect(url_for('display', name=username))
        else:
            return redirect(url_for('Invalid'))
    return render_template("signin.html")



@app.route('/orderconfirmation', methods=["GET", "POST"])
def orderconfirmation():
    return render_template("orderconfirmation.html")


@app.route('/registerconfirmation', methods=["GET", "POST"])
def registerconfirmation():
    return render_template("registerconfirmation.html")

@app.route('/request_1', methods=["GET", "POST"])
def request_1():
    return render_template("request_1.html")

@app.route('/Invalid', methods=["GET", "POST"])
def Invalid():
    return render_template("Invalid.html")

@app.route('/volunteer/<name>/', methods=['GET', 'POST'])
def display(name):
    if request.method == "POST":
        if request.form['opt'] == 'accept':
            allocate_order(name)
            return redirect(url_for('request_1'))
        else:
            deallocate(name)
            return redirect(url_for('request_1'))
    list1 = get_patients(name)
    return render_template('value.html', name=name, patients=list1)


if __name__ == '__main__':
    app.run()





