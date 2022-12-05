str="to Amazon Amazon Deloitte to Oracle be replaced Google"

def string_replace(str):
    words=["Google", "Microsoft", "Amazon" ,"Deloitte", "Oracle"]

    for i in words:
        str=str.replace(i, i+'©')
    return str

print(string_replace(str))