import os 
os.system("cls") # clear terminal 
n = 1000
n = str(n)
s = ""
l = len(n) # length of number 
if l > 9 :
    s = "B"
    n = n[::-1] # reverse it 
    n = n.replace(n[:6],"") # remove last 6 numbers 
    n = n[::-1]
elif l > 6 :
    s = "M"
    n = n[::-1]
    n = n.replace(n[:3],"") # remove last 3 numbers  
    n = n[::-1]
elif l > 3:
    s = "K"
    n = n[::-1]
    n = n.replace(n[:3],"") # remove last 3 numbers  
    n = n[::-1]

print(n,s)