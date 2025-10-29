import os
from dotenv import load_dotenv

# Load entorn variables
load_dotenv(dotenv_path='.venv/.env')

# Load data and URL's
usernameID = os.getenv("usernameID")
password = os.getenv("password")
urlCollege = os.getenv("urlCollege")
urlGrades = os.getenv("urlGrades")
gmailUser = os.getenv("gmailUser")
gmailReceiver = os.getenv("gmailReceiver")
gmailPassword = os.getenv("gmailPassword")
chatID = os.getenv("chatID")
tokenBot = os.getenv("tokenBot")