def emailProcess(email):
     useremail[0:email.index("@")]
     

def main():
     email=input(f"Please enter your Email: ").strip()
     print(f"Hello, {email}")

if __name__ == "__main__":
     main()