#Gavin Brady
#Oct 24 2023
#Finds derivative of polynomials using power rule

def powerRule(func):
    termsList = func.split(" + ")#splits function into list of all terms
    
    derivative = '' 
    
    for term in termsList:#goes term by term through list
        
        if term.find('x^') > 0:#if term has coefficient and exponent, finds new coefficient and power
            coeff = int(term[:term.find('x')]) * int(term[(term.find('^')+1):])
            power = int(term[(term.find('^')+1):]) - 1
            
        elif term.find('x^') == 0: #solves if term has no coefficient
            coeff = int(term[(term.find('^')+1):])
            power = int(term[(term.find('^')+1):]) - 1
            
        elif term.find("^") == -1: #solves if no power
            if term.find('x') == 0: #solves if term has no power and no coefficient
                coeff = 1
                power = 0
            if term.find('x') > 0: #solves if term has no power but has coefficient
                coeff = int(term[:term.find('x')])
                power = 0
            if term.find('x') == -1: #solves if term is constant
                coeff = 0
                power = 0
                
        #puts differentiated term together
        diffTerm = f"{coeff}x^{power}"

        if diffTerm == "0x^0":
            diffTerm = ''
        elif diffTerm.find('x^0') != -1:
            diffTerm = diffTerm[:diffTerm.find('x^0')]
        elif diffTerm.find('x^1') != -1:
            diffTerm = diffTerm[:diffTerm.find('^1')]

        if termsList.index(term) == 0 or diffTerm == '': #adds with no " + " before in case of first term, or does not add at all in case of blank term
            derivative += diffTerm
        else: #adds term with " + " prefacing
            derivative += f" + {diffTerm}"

    return(derivative)

def productRule(func):
    derivative=''
    factorsList = func.split(' * ')
    factorsList_noPARENTHESIS = []
    for factor in factorsList:
        factor = factor[1:(factor.find(')'))]
        
        factorsList_noPARENTHESIS.insert(len(factorsList_noPARENTHESIS),factor)
        
    derivative = f"(({powerRule(factorsList_noPARENTHESIS[0])}) * ({factorsList_noPARENTHESIS[1]})) + (({factorsList_noPARENTHESIS[0]}) * ({powerRule(factorsList_noPARENTHESIS[1])}))" 
    return(derivative)


if __name__ == "__main__":
    while True:
        function = input("Enter function, f(x) = ")
        if function.find('*') != -1: 
            print(f"The derivative, f'(x) = {productRule(function)}")
        else:
            print(f"The derivative, f'(x) = {powerRule(function)}")
