from re import L
import sympy as smp
from sympy import *
import tkinter as tk
from tkinter import ttk
from sympy.parsing.sympy_parser import parse_expr
from matplotlib import *
import matplotlib.pyplot as plt

implicit = false



#index variables
height = 3.4

#Fonts
bigFont = ("Arial", 80, "bold")
digitFont = ("Arial", 24, "bold")
defaultFont = ("Arial", 20)
smallFont = ("Arial", 30, "bold")

#Colors
offwhite = "#F8FAFF"
gray = "#F5F5F5"
label_col = "#25266E"
purplishBlue = "#5f5cbf"
lightPurple = "#855cbf"
lightBlue = "#CCEDFF"

#symbols
x = smp.symbols('x')

#Trying to connect Deriv Calc to Website

from flask import Flask, render_template, request

deriv = Flask(__name__)


def test():
    for i in range(10):
        print("test)")

@deriv.route("/")

@deriv.route("/home")
def home():
    return render_template("home.html")

@deriv.route("/derivatives")

def derivatives():
    return render_template("index.html")

@deriv.route("/integral", methods = [ 'POST', "GET"])
def integral():
    
    return render_template("second.html")

@deriv.route("/seriesexpansion", methods = [ 'POST', "GET"])
def seriesexpansion():
    return render_template("third.html")

@deriv.route("/limits", methods = [ 'POST', "GET"])
def limits():
    return render_template("limits.html")
#Definitely one day find a way to combine the result pages. A lot of the code is the same but I can't think of a way of differentiating the operations. Ex. Deriv or Integral
#To do: Improve the parser


#IMPLEMENT PI CONSTANT
@deriv.route("/result",methods = ['POST', "GET"])
def result():
    
    if request.method == 'POST':
        if request.form.get('cb1') == None:
            implicit = false
        else:
            implicit = true
    output = request.form.to_dict()
    expression = output["expression"]
    evaluate = output["evaluate"]
    print(evaluate)
    if expression == "":
        return render_template("index.html")
    original = expression
    result = ""
    for i in range(len(expression)):
        if expression[i] == "^":
            result = result + "**"
        elif i != 0 and expression[i] == "x" and expression[i-1] != "/"and expression[i-1] != "(" and expression[i-1] != "" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and expression[i-1] != "^":
            result = result + "*x"
        elif implicit == true and i != 0 and expression[i] == "y" and expression[i-1] != "/" and expression[i-1] != "(" and expression[i-1] != "" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and expression[i-1] != "^":
            result = result + "*y"
        elif i != 0 and expression[i] == "p" and expression[i+1] == "i" and expression[i-1] != "("  and expression[i-1] != "/" and expression[i-1] != "" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and expression[i-1] != "^":
                result = result + "*p"  
        elif i != 0 and expression[i] == "e" and expression[i-1] != "(" and expression[i-1] != "/"and expression[i-1] != "" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and result[i-1] != "*" and result[i-1] != "s" and expression[i-1] != "^" and expression[i-1] != "s":
            result = result + "*e"
        elif i != 0 and expression[i] == "l" and expression[i-1] != "(" and expression[i-1] != "/"and expression[i-1] != "" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and result[i-1] != "*" and result[i-1] != "s" and expression[i-1] != "^":
                result = result + "*l"
        elif i != 0 and expression[i] == "t" and expression[i-1] != "(" and expression[i-1] != "/"and expression[i-1] != "" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and result[i-1] != "*" and result[i-1] != "s" and expression[i-1] != "^" and expression[i-1] != "o":
            result = result + "*t"
        elif i != 0 and expression[i] == "s" and expression[i-1] != "(" and expression[i-1] != "/"and expression[i-1] != "" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and result[i-1] != "*" and result[i-1] != "s" and expression[i-1] != "^" and expression[i-1] != "o":
            result = result + "*s"
        elif i != 0 and expression[i] == "c" and expression[i-1] != "(" and expression[i-1] != "/"and expression[i-1] != "" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and result[i-1] != "*" and result[i-1] != "s" and expression[i-1] != "^" and expression[i-1] != "e" and expression[i-1] != "s":
            result = result + "*c"
        else:
            result = result + expression[i]
    print("expresio n after parse: " +  result)
    if implicit == true:
        y = smp.symbols('y')
        if "y" not in result or "y" not in expression:
            expression = str(simplify(smp.diff(parse_expr(result), x)))
            expression = str(latex(parse_expr(expression)))
            print("no y")
        elif "x" not in result or "x"  not in expression:
            expression = str(simplify(diff(parse_expr(result), y)))
            expression = str(latex(parse_expr(expression)))
            print("no x")
        else:
            expression = str(simplify(idiff(parse_expr(result), y, x)))
            expression = str(latex(parse_expr(expression)))
            print("both")
    else:
        expression = str(simplify(smp.diff(parse_expr(result), x)))
        expression = str(latex(parse_expr(expression)))
    if evaluate != "":
        original = str(latex(parse_expr(result)))
        expression = str(simplify(smp.diff(parse_expr(result), x)))
        result = str(latex(N(parse_expr(expression).subs(x, int(evaluate)))))
        expression = str(latex(parse_expr(expression)))
        

        return render_template("index.html", expression = expression, original = original, result = result)
    original = str(latex(parse_expr(result)))
    
    print(result)
    print(expression)
    return render_template("index.html", expression = expression, original = original)


#IMPLEMENT PI CONSTANT
@deriv.route("/result1",methods = ['POST', "GET"] )
def result1():

    output = request.form.to_dict()
    expression = output["expression"]
    lower = output["lower"]
    higher = output["higher"]
    original = expression
    print(type(expression))
    result = ""
    if expression == "":
        return render_template("second.html")
    if expression == "csc(x)":
        expression = str(latex(parse_expr("-ln(csc(x)+cot(x))+C")))
        return render_template("second.html", expression = expression, original = original)
    elif expression == "sec(x)":
        expression = str(latex(parse_expr("ln(sec(x)+tan(x))+C")))
        return render_template("second.html", expression = expression, original = original)
    else:
        for i in range(len(expression)):
            if expression[i] == "^":
                result = result + "**"
            elif i != 0 and expression[i] == "x" and expression[i-1] != "("  and expression[i-1] != "/" and expression[i-1] != "" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and expression[i-1] != "^":
                result = result + "*x"
            #sin cos tan csc sec cot
            elif i != 0 and expression[i] == "p" and expression[i+1] == "i" and expression[i-1] != "("  and expression[i-1] != "/" and expression[i-1] != "" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and expression[i-1] != "^":
                result = result + "*p"  
            elif i != 0 and expression[i] == "e" and result[i-1] != "s" and expression[i-1] != "(" and expression[i-1] != "" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and result[i-1] != "*" and expression[i-1] != "^":
                result = result + "*e"
            elif i != 0 and expression[i] == "l" and expression[i-1] != "(" and expression[i-1] != "/"and expression[i-1] != "" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and result[i-1] != "*" and result[i-1] != "s" and expression[i-1] != "^":
                result = result + "*l"
            elif i != 0 and expression[i] == "t" and expression[i-1] != "(" and expression[i-1] != "/"and expression[i-1] != "" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and result[i-1] != "*" and result[i-1] != "s" and expression[i-1] != "^" and expression[i-1] != "o":
                result = result + "*t"
            elif i != 0 and expression[i] == "s" and expression[i-1] != "(" and expression[i-1] != "/"and expression[i-1] != "" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and result[i-1] != "*" and result[i-1] != "s" and expression[i-1] != "^" and expression[i-1] != "o":
                result = result + "*s"
            elif i != 0 and expression[i] == "c" and expression[i-1] != "(" and expression[i-1] != "/"and expression[i-1] != "" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and result[i-1] != "*" and result[i-1] != "s" and expression[i-1] != "^" and expression[i-1] != "e" and expression[i-1] != "s":
                result = result + "*c"
            else:
                result = result + expression[i]
    print(result)
    print(expression)
    if lower == "infinity":
        lower = "oo"
    if higher == "infinity":
        higher = "oo"
    if lower == "-infinity":
        lower = "-oo"
    if higher == "-infinity":
        higher = "-oo"
    if lower == "" and higher == "":
        expression = str(simplify(smp.integrate(parse_expr(result), x)))
        expression = expression + " + C"
        expression = str(latex(parse_expr(expression)))
        original = str(r'\int_{}^{}') + str(latex(parse_expr(result)))+"dx"
        return render_template("second.html", expression = expression, original = original)
    #Convergence/divergence  doesnt show  when  bounds are not  infinity. Basically  doesnt show for  type 2 impropers.
    #make it so the  bound   inputs only  show  up  if a   button  is pressed 
    expression = str(simplify(smp.integrate(parse_expr(result), (x, lower, higher))))
    print("expression " + expression)
    if lower =="oo" or lower =="-oo" or higher=="oo" or higher=="-oo":
        if expression == "-oo" or expression == "oo":
            vergence = "divergent"
            expression = str(latex(parse_expr(expression)))
            original = str(r'\int_{' + lower + r'}^{' + higher + '}') + str(latex(parse_expr(result))) + "dx"
            return render_template("second.html", expression = expression, original = original, vergence = vergence)
        else:
            vergence = "convergent"
            print("vetgence " +vergence)
            expression = str(latex(parse_expr(expression)))
            original = str(r'\int_{' + lower + r'}^{' + higher + '}') + str(latex(parse_expr(result)))
            return render_template("second.html", expression = expression, original = original, vergence = vergence)
    expression = str(latex(parse_expr(expression)))
    original = str(r'\int_{' + lower + r'}^{' + higher + '}') + str(latex(parse_expr(result))) + "dx"

    return render_template("second.html", expression = expression, original = original)


#IMPLEMENT PI CONSTANT
@deriv.route("/result2",methods = ['POST', "GET"])
def result2():
    if request.method == 'POST':
        if request.form.get('cb1') == None:
            polynomial = false
        else:
            polynomial = true
    print(polynomial)
    output = request.form.to_dict()
    degree = output["degree"]
    expression = output["expression"]
    center = output["center"]
    original = expression
    if center == "":
        center = "0"
    print(type(expression))
    if expression == "" or degree == "":
        return render_template("third.html")
    result = ""
    for i in range(len(expression)):
        if expression[i] == "^":
            result = result + "**"
        elif i != 0 and expression[i] == "x" and expression[i-1] != "(" and expression[i-1] != "" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and expression[i-1] != "^":
            result = result + "*x"
            #sin cos tan csc sec cot
        elif i != 0 and expression[i] == "p" and expression[i+1] == "i" and expression[i-1] != "("  and expression[i-1] != "/" and expression[i-1] != "" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and expression[i-1] != "^":
                result = result + "*p" 
        elif i != 0 and expression[i] == "e" and result[i-1] != "s" and expression[i-1] != "(" and expression[i-1] != "" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and result[i-1] != "*" and expression[i-1] != "^":
            result = result + "*e"
        elif i != 0 and expression[i] == "l" and expression[i-1] != "(" and expression[i-1] != "/"and expression[i-1] != "" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and result[i-1] != "*" and result[i-1] != "s" and expression[i-1] != "^":
            result = result + "*l"
        elif i != 0 and expression[i] == "t" and expression[i-1] != "(" and expression[i-1] != "/"and expression[i-1] != "" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and result[i-1] != "*" and result[i-1] != "s" and expression[i-1] != "^" and expression[i-1] != "o":
            result = result + "*t"
        elif i != 0 and expression[i] == "s" and expression[i-1] != "(" and expression[i-1] != "/"and expression[i-1] != "" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and result[i-1] != "*" and result[i-1] != "s" and expression[i-1] != "^" and expression[i-1] != "o":
            result = result + "*s"
        elif i != 0 and expression[i] == "c" and expression[i-1] != "(" and expression[i-1] != "/"and expression[i-1] != "" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and result[i-1] != "*" and result[i-1] != "s" and expression[i-1] != "^" and expression[i-1] != "e" and expression[i-1] != "s":
            result = result + "*c"
        else:
            result = result + expression[i]
    #sympy knows how to make taylor polynomials i dont know why i even coded this
    if polynomial == true:
        total = parse_expr(result).subs(x, center) 
        derivatives = []
        derivatives.append(result)
        for i in range(int(degree)):
            temp = str(simplify(smp.diff(parse_expr(derivatives[i]), x)))
            derivatives.append(temp)
        print(derivatives)
        if int(center) == 0:
            for i in range(int(degree)):
                total = str(total) + " + " + str((parse_expr(derivatives[i+1]).subs(x, 0)*x**(i+1))/factorial(i+1))
                print(total)
            expression = str(latex(parse_expr(total)))
            return render_template("third.html", expression = expression, original = original, degree = degree, center = center)
        else:
            for i in range(int(degree)):
                total = str(total) + " + " + str((parse_expr(derivatives[i+1]).subs(x, center)*(x-int(center))**(i+1))/factorial(i+1))
                print(total)
            expression = str(latex(parse_expr(total)))
            return render_template("third.html", expression = expression, original = original, degree = degree, center = center)
    #EXPERIMENTAL CODE FOR SERIES NOTATION
    if "sin(x)" in expression:
        seriesText = "\sum_{n=0}^{oo}" + str(latex(parse_expr("((-1)**n*x**(2*n+1))/factorial(2*n+1)")))
    else:
        seriesText = ""
    #EXPERIMENTAL CODE FOR SERIES
    #still not sure how to implement properly 
    print(result)
    print(expression)
    expression = str((series(parse_expr(result), x, int(center), int(degree)+1))) 
    expression = str(latex(parse_expr(expression)))
    original = str(latex(parse_expr(result)))
    print(seriesText)
    print(expression)
    #If you want the series text to only show when a series is registered then pass in series as a result. Make  changes to return statements later. if we pass it in
    #we can use a line like (if expression) to make it show only when a registered series is shown

    
    return render_template("third.html", expression = expression, original = original, degree = degree, center = center, seriesText = seriesText)



#IMPLEMENT PI CONSTANT -- DONE
@deriv.route("/result3",methods = ['POST', "GET"])
def result3():
    output = request.form.to_dict()
    expression = output["expression"]
    evalAt = output["evaluate"]
    original = expression
    print(type(expression))
    result = ""
    for i in range(len(expression)):
        if expression[i] == "^":
            result = result + "**"
        elif i != 0 and expression[i] == "x" and expression[i-1] != "(" and expression[i-1] != "" and expression[i-1] != "/" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and expression[i-1] != "^":
            result = result + "*x"
            #sin cos tan csc sec cot
        elif i != 0 and expression[i] == "p" and expression[i+1] == "i" and expression[i-1] != "("  and expression[i-1] != "/" and expression[i-1] != "" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and expression[i-1] != "^":
                result = result + "*p" 
        elif i != 0 and expression[i] == "e" and result[i-1] != "s" and expression[i-1] != "(" and expression[i-1] != "" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and result[i-1] != "*" and expression[i-1] != "^":
            result = result + "*e"
        elif i != 0 and expression[i] == "l" and expression[i-1] != "(" and expression[i-1] != "/"and expression[i-1] != "" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and result[i-1] != "*" and result[i-1] != "s" and expression[i-1] != "^":
            result = result + "*l"
        elif i != 0 and expression[i] == "t" and expression[i-1] != "(" and expression[i-1] != "i" and expression[i-1] != "/"and expression[i-1] != "" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and result[i-1] != "*" and result[i-1] != "s" and expression[i-1] != "^" and expression[i-1] != "o":
            result = result + "*t"
        elif i != 0 and expression[i] == "s" and expression[i-1] != "(" and expression[i-1] != "/"and expression[i-1] != "" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and result[i-1] != "*" and result[i-1] != "s" and expression[i-1] != "^" and expression[i-1] != "o":
            result = result + "*s"
        elif i != 0 and expression[i] == "c" and expression[i-1] != "(" and expression[i-1] != "/"and expression[i-1] != "" and expression[i-1] != "*" and expression[i-1] != "+" and expression[i-1] != "-" and result[i-1] != "*" and result[i-1] != "s" and expression[i-1] != "^" and expression[i-1] != "e" and expression[i-1] != "s":
            result = result + "*c"
        else:
            result = result + expression[i]
    if evalAt == "infinity":
        evalAt = "oo"
        expression = str((limit(parse_expr(result), x, evalAt)))
        
        expression = str(latex(parse_expr(expression)))
        
        original = str(latex(parse_expr(result)))
        original = str(r"\lim_{x \to \infty } ") + original
    else:
        expression = str((limit(parse_expr(result), x, int(evalAt)))) 
        expression = str(latex(parse_expr(expression)))
        
        original = str(latex(parse_expr(result)))
        original = str(r"\lim_{x \to " + str(evalAt) + "}") + original
    print()
    
    
    
    return render_template("limits.html", expression = expression, original = original)
    


if __name__ == '__main__':
    deriv.run(debug = True, port=5001)


