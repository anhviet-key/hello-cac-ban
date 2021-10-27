def emailProcess(email):
    user_name = email[0:email.index("@")]
    email_domain = email[email.index("@")+1:]
    return [user_name, email_domain]


def print_Mess(user_name, email_domain):
    print(f"Email_User: {user_name} \nEmail_Domain: {email_domain}")

def main():
    email = input(f"Please enter your Email: ").strip()
    # print(f"Hello, {email}")
    user_name, email_domain = emailProcess(email)
    print_Mess(user_name, email_domain)


if __name__ == "__main__":
    main()
