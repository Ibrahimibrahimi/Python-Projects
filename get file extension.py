from essentiels import clearTerminal
clearTerminal()
filename = "index.html.pdf"

filename = filename[::-1]
ext = filename[:filename.index(".")].lower() # get extension name
ext = ext[::-1]

# print(ext)
exts = {
    "txt":"text file",
    "pdf":"document pdf",
    "img":"image",
    "jpg":"image",
    "svg":"image",
    "html":"page web"
}
if ext in exts :Type = exts[ext] 
else : Type = "Inconnue"
print("file type : ",Type)