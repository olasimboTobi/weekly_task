import re

def email_parser(email):
    collect = ['username','domain']
    pattern =re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    confirm = pattern.search(email)
    if confirm:
        sep = re.split('@',email)
        result = {key:value for (key,value) in zip(collect, sep)}
        

    print(result)

email_parser("Elias@decadev.com")

  

