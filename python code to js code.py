import os
os.system("cls") # clear terminal 

#      ####  ####  ####   
#      #  #  #  #  #   # 
#      #  #  #  #  # #    
#####  ####  ####  #        
def ToJsFor(code):
    # variable name : "i"
    # range : "50"

    # js = '' # javascript code
    rang = list(
        code[code.index("range(")+6:code.index(")")].split(","))
    if len(rang) == 1 : # one argument (start=0,end,step=1)
        arguments = [0,rang[0],"++"]
    elif len(rang) == 2: # two arguments (start,end,step=1)
        arguments = [rang[0],rang[1],"++"]
    elif len(rang) == 3 : # three arguments (start,end,step)
        "50,12,15"
        if rang[2] == "1" :# to make "++" inplace of "+=1"
            arguments = [rang[0],rang[1],"++"]
        else :
            arguments = [rang[0],rang[1],"+="+rang[2]]
        
    variable_name = code[code.index("for") + 4:code.index("in")]
    start = arguments[0]
    end = arguments[1]
    step = arguments[2]
    js = f"""for (var {variable_name}={start} ;{variable_name} < {end};{variable_name}{step})"""
    return f"python : {code} \njs : {js}"

my_Python_Loop = "for color in range(1,12,11)"
print(ToJsFor(my_Python_Loop))
print("-"*70) # nice separator "-"
def ToJsFunction(code):
    code = code.replace("def ","") # remove keyword => code = "d()" function name + (a)
    "d(a)"
    fun_name = code[:code.index("(")] # name of function 
    # print(fun_name)
    parameters = list(code[code.index("(")+1:code.index(")")].split(",")) # get list of parameters 

    # print(parameters)
    pars = ""
    for i in parameters :
        pars += i + ","
    pars = pars[:-1] # remove last comma 
    js = f"function {fun_name}({pars})" + "{}"

    return f"python : {code}\njs : {js}"

print(ToJsFunction("def myFunction(name,start,end):"))

