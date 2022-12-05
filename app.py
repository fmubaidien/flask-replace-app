str="to Amazon Amazon Deloitte to Oracle be replaced Google"

words=["Google", "Microsoft", "Amazon" ,"Deloitte", "Oracle"]

for i in words:
    if i in str:
        str=str.replace(i, i+'©')

print(str)