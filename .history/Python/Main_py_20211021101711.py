from Sub_py import emailProcess, print_Mess


def main():
	emails = ["hello.vi@gmail.com", "Package@yahoo.com", "Test@gmail.dev"]
	for email in emails:
     	name, email_domain = emailProcess(email)
		print_Mess(username, email_domain)

if __name__ == "__main__":
     main()
