def emailProcess(email):
     user_name=email[0:email.index("@")]
     email_domain=email[email.index("@")+1:]
     # print(f"Username is {user_name}")
     # print(f"Domain is {email_domain}")
     return [user_name, email_domain]

def main():
     email=input(f"Please enter your Email: ").strip()
     print(f"Hello, {email}")
     user_name, email_domain=emailProcess(email)
     
def print():
    print(f"Username is {user_name}")
    print(f"Domain is {email_domain}")

if __name__ == "__main__":
     main()
     
