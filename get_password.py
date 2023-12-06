# get_password.py

import getpass

# Get username and password
CHUMBA_USERNAME = input("Enter your Chumba Casino username: ")
CHUMBA_PASSWORD = getpass.getpass("Enter your Chumba Casino password: ")

# Write the variables to the .env file
with open(".env", "w") as env_file:
    env_file.write(f"CHUMBA_USERNAME={CHUMBA_USERNAME}\n")
    env_file.write(f"CHUMBA_PASSWORD={CHUMBA_PASSWORD}\n")

print(".env file created successfully.")
