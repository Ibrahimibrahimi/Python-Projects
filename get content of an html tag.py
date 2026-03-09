import essentiels
essentiels.clearTerminal()

# html code 
html = "<b id='p' hidden class='p'>This is a text </b>"

# get tag name 
tagName = html[html.index("<")+1:html.index(">")]
tag = tagName.split(" ")[0]
# get content of tag (only for double closed tags)
if f"</{tag}>" in html :content = html[html.index("<" + tagName + ">")+len("<" + tagName + ">"):html.index("</")]
else : content = "No content (single closing tag)"

# show results

# get attributes 
# slice start : <tag , end : >
# get all attributes & values
attributes = html[html.index("<"+tag)+len("<" + tag ):html.index(">")].split(" ")

# this function take full expression of attribute ("class='container'") and if this expression is valued attri ,
# => it return [attr_name,attr_val] , else it return just attr_name
def attribute_getInfos(text):
    if "=" in text : is_val_attr = True
    else : is_val_attr = False

    if is_val_attr :
        attr_name = text.replace('"','').split("=")[0]
        attr_val = text.replace('"','').replace("'","").split("=")[1]
        return [attr_name,attr_val]
    else :
        attr_name = text.replace('"','').split("=")[0]
        return [attr_name]


print("TagName : ",tag,"\nContent:",content)
print("Attributes : ")

# print all attributes and there values 
for z in attributes :
    if z != "": # avoid empty values 
        if len(attribute_getInfos(z)) == 1: print("\t- ",attribute_getInfos(z)[0])
        else : print("\t- ",attribute_getInfos(z)[0],":",attribute_getInfos(z)[1],";")
    else :
        pass