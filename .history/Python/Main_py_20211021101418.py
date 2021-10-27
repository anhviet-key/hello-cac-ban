from Sub_py import emailProcess, print_Mess


def main():
	emails = ["hello.vi@gmail.com", "Package@yahoo.com", "Test@gmail.dev"]
	for email in emails:
     	use_name, email_domain = emailProcess(email)

if __name__ == "__main__":
     main()
