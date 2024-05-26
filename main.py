from flask import Flask, render_template, request
import gyaan as gn

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template("index.html")

# @app.route('/login', methods=["POST", "GET"])
# def Login():
#     if request.method == "POST":
#         user = request.form["nm"]
#         return None
#     else:
#         return render_template("login.html")

@app.route('/basic-arithmetic', methods=["POST", "GET"])
def Basic_Arith():
    Title = "Basic Arithmetic"
    if request.method == "POST":
        num_1 = int(request.form['num_1'])
        num_2 = int(request.form['num_2'])
        arith = request.form.get('operation')
        if arith == 'add':
            result = gn.Basic.add(num_1, num_2)
        elif arith == 'sub':
            result = gn.Basic.sub(num_1, num_2)
        elif arith == 'mul':
            result = gn.Basic.mul(num_1, num_2)
        elif arith == 'divi':
            result = gn.Basic.div(num_1, num_2)
        else:
            return f"Sorry for Inconvinience!!!"
        return render_template("calculator.html", Title=Title,  result=result)
    else:
        return render_template("calculator.html", Title=Title)

@app.route('/basic-calculations', methods=["POST", "GET"])
def Basic_Calci():
    Title = "Basic Calculations"
    if request.method == "POST":
        num_1 = int(request.form['num_1'])
        num_2 = int(request.form['num_2'])
        basic = request.form.get('operation')
        if basic == 'sq':
            result = gn.Sq_Cb.sq_cb(basic, num_1)
        elif basic == 'cb':
            result = gn.Sq_Cb.sq_cb(basic, num_1)
        elif basic == 'sqrt':
            result = gn.Sq_Cb.square_rt(num_1)
        elif basic == 'cbrt':
            result = gn.Sq_Cb.cube_rt(num_1)
        elif basic == 'ex':
            result = gn.Sq_Cb.expo(num_1, num_2)
        elif basic == 'per':
            result = gn.Sq_Cb.percentage(num_1,num_2)
        else:
            return f"Sorry for Inconvinience!!!"
        return render_template("calculator.html", Title=Title,  result=result)
    else:
        return render_template("calculator.html", Title=Title)
    
@app.route('/commercial-math', methods=["POST", "GET"])
def Com_Math():
    Title = "Commercial Math"
    if request.method == "POST":
        num_1 = int(request.form['num_1'])
        num_2 = int(request.form['num_2'])
        comm = request.form.get('operation')
        if comm == "Pro_or_Los":
            result = gn.Commercial.profit_loss(num_1, num_2)
        elif comm == "pl_per":
            result = gn.Commercial.p_l_pecntge(num_1, num_2)
        elif comm == "inter":
            num_3 = int(request.form['num_3'])
            result = gn.Commercial.interest(num_1, num_2, num_3)
        elif comm == "ab_per":
            result = gn.Commercial.A_by_Percen(num_1, num_2)
    else:
        return render_template("calculator.html", Title=Title)
    
# @app.route('/about', methods=["POST", "GET"])
# def About():
#     return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)