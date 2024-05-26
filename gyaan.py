from math import sqrt,cbrt

class Basic:
    def add(a,b):
        return (a+b)
    def sub(a,b):
        return (a-b)
    def mul(a,b):
        return (a*b)
    def div(a,b):
        return (a/b)
    
class Sq_Cb:
    def square_rt(a):
        return sqrt(a)
    def cube_rt(a):
        return cbrt(a)
    def sq_cb(type, a):
        if type == "sq":
            return (a**2)
        if type == "cb":
            return (a**3)
    def expo(a,ex):
        return (a**ex)
    
    def percentage(P,A):
        percentage = (A/P)*100
        return percentage

class Commercial:
    def profit_loss(sp, cp):
        if sp > cp:
            p_l = sp-cp
            msg = "Profit"
        if sp < cp:
            p_l = sp-cp
            msg = "Loss"
        return f"You had a {msg} of {p_l}"
    
    def p_l_pecntge(p_l, cap):
        percentage =  (p_l/cap)*100
        return percentage
    
    def interest(P,rate,T):
        Interest = (P*rate*T)/100
            
    def A_by_Percen(P, percen):
        amt = (percen*P)/100
