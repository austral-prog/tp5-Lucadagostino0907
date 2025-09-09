# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    
    descriminante= (b ** 2 - 4 * a * c) 
    if descriminante > 0: 
        r1= (-b + descriminante**0.5)/(2 * a)
        r2= (-b - descriminante**0.5)/(2 * a)

        if r1 == 0:
            r1 = ""

        if r2 == 0:
            r2 = ""

        return f"({r1}, {r2})"

    if descriminante == 0: 
        r= -b / (2*a)
        return f"({r})"
    else: 

        return "( )"

def value_y(a, b, c, x):
    
    y = a *(x ** 2) + b * x + c

    return y

def to_string(a, b, c):
    
    result= ""

    if a != 0:

        A = f"{a} * X^2"
        result = A
    
    if a==0:
        result = ""

    if b != 0: 

        B = f"{b} * X"

        if result == "": 

            result = B

        else: 
             result = f'{result} + {B}'

    if c != 0: 

        C = c

        if c == "":
                result = f"{result}"
        
        else: 

            if result != "":

                result = f"{result} + {c}"
            else:
                result = C
        return f"f(x) = {result}"  


def derivation(a, b, c):
    

    if a==0 and b == 0: 
        return "f'(x) = 0"

    elif a==0:

        return f"f'(x) = {b}"

    elif b == 0:
        A = 2*a
        return f"f'(x) = {A} * X"
    else: 
        A = 2*a

        return f"f'(x) = {A} * X + {b}"