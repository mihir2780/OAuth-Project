import threading

def redirected(username, access_token, scopes, duration): # logic of redirecting user to the third party application
    print("Welcome to the third-party application.")
    print(f"You are logged in as: {username}")
    print(f"Your access token is: {access_token}")
    print("You have limited access based on your authorization.")
    
    timer = threading.Timer(duration, lambda: print("\nSession has expired due to token expiry. Try again.") or exit()) 
    # to exit the app based on token expiry 
    timer.start()

    try: # demonstrating scenario about user getting limited access for updating emailid or profile on
        while True:
            print("\n1. To update your email ID, press 1 ") # demonstration of the limited scopes access
            print("2. To update your profile, press 2 ")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == '1' and 'email' in scopes:
                email = input("Enter an email id: ")
                print(f"Email ID {email} updated successfully.") # just taking the user input and not storing anywhere. this is just demo
            elif choice == '2' and 'profile' in scopes:
                profile = input("Enter your profile detail: ")
                print(f"Profile details {profile} updated successfully.")
            elif choice == '3':
                print("Exiting application...")
                break
            else:
                print("Invalid option or insufficient permissions.")
    finally:
        timer.cancel()  # Timer is stopped if the user exits
