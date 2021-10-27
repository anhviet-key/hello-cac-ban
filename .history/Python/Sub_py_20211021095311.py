def emailProcess(email):
     user_name=email[0:email.index("@")]
     email_domain=email[email.index("@")+1:]
     print(f"Username is {user_name}")

def main():
     email=input(f"Please enter your Email: ").strip()
     print(f"Hello, {email}")
     emailProcess(email)

if __name__ == "__main__":
     main()
     
