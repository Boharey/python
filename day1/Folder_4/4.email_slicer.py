email: str = input("enter your email : ")
index: int = email.index("@")
# //utsav@gmail.com
username: str = email[:index]
domain: str = email[index+1:]

print(f"username : {username}")
print(f"domain : {domain}")