styles = [

]
import os,random
colors = []
# font size 
for i in range(800):
    styles.append(".f-size-" + str(i) + "{ font-size : " + str(i) + "px;}"                " \n")
# bgcolors 

print("agendé")
with open("styles.css","w") as style :
    for io in styles:
        style.write(io)
    for i in range(5000):
        color = f"{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}" #.zfill(6)[::-1]
        if color in colors or color*2 in color :
            pass
        else :
            style.write(".bg-" + color +  "{background-color : #" + color+ "}\n")
            style.write(".bg-" + color + color +  "{background-color : #" + color + color+ "}\n")
            colors.append(color)
            colors.append(color*2)
            
        print("........",i,"passed")
        os.system("cls")
print("agendé")

# show variable memory occupation in bytes 
import sys
print(sys.getsizeof(colors))