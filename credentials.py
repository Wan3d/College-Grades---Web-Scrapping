import os
from dotenv import load_dotenv

# Load entorn variables
load_dotenv()

# Load data and URL's
usernameID = os.getenv("usernameID")
password = os.getenv("password")
urlCollege = os.getenv("urlCollege")
urlGrades = os.getenv("urlGrades")
gmailUser = os.getenv("gmailUser")
gmailReceiver = os.getenv("gmailReceiver")
gmailPassword = os.getenv("gmailPassword")
