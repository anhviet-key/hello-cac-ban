from Sub_py import emailProcess, print_Mess


def main():
	emails = ['hello.vi@gmail.com', 'Package@yahoo.com', 'Test@gmail.dev']
	for email in emails:
     	user_name, emaildomain = emailProcess(email)
		print_Mess(user_name, email_domain)

if __name__ == "__main__":
     main()
