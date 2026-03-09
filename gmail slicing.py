from essentiels import clearTerminal
from essentiels import ListToStr
clearTerminal()
email = "ibrahim.id-wahman.06@google.com"

# get username of Email
username = email[:email.index("@")]
print(username)

# get Email proxy  domains 
domain = email[email.index("@")+1:].split(".")
print(domain)

infos = {
    "username ":username,
    "domains":domain
}

print("username :",infos["username "])
print("domains :",ListToStr(domain," "))