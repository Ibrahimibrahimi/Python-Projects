import os 
def clearTerminal():os.system("cls")

def ListToStr(l,separator=""):
    r = ""
    for i in l:
        r += i + separator
    if separator == "":return r
    else : return r[:-1]
