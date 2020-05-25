from cryptography.fernet import Fernet
import os
import time
#password maneger def
def maneger():
  print("_________________________")
  print("what you want to do?")
  print("1-add an account")
  print("2-list all your accounts")
  print("3-remove account")
  print("_________________________")
  ask1 = input("your choise:")
  if ask1 == "1":
    acd_new()
  elif ask1 == "2":
    listacc()
  elif ask1 == "3":
    remacc()
#add an account
def acd_new():
  defdir = r"C:\Users\Public\OnePass\Accounts"
  path = os.path.join(defdir, username2)
  os.chdir(path)
  file = open("key.key", "rb")
  key = file.read()
  file.close()
  f = Fernet(key)
  folder = "passes"
  path = os.path.join(defdir, username2, folder)
  lisst = os.listdir()
  if folder in lisst:
    os.chdir(path)
    accuser = input("account username:")
    whereacc = input("where account is from:")
    accpass = input("account password:")
    filename21 = whereacc + " - " + accuser
    file13 = open(filename21, "wb")
    passen = accpass.encode()
    done_password1 = f.encrypt(passen)
    file13.write(done_password1)
    file13.close()
    print("password added")
    time.sleep(3)
    maneger()
  else:
    os.mkdir(path)
    acd_new()
#list accounts
def listacc():
  defdir = r"C:\Users\Public\OnePass\Accounts"
  path = os.path.join(defdir, username2)
  os.chdir(path)
  file = open("key.key", "rb")
  key = file.read()
  file.close()
  f = Fernet(key)
  folder = "passes"
  path = os.path.join(defdir, username2, folder)
  os.chdir(path)
  list = os.listdir()
  print("_________________________")
  for acc in list:
    file21 = open(acc, "rb")
    passw = file21.read()
    decript = f.decrypt(passw)
    mes1 = decript.decode()
    account2 = acc
    account1 = account2 + " - " + mes1
    print(account1)
  print("app - username - password")
  print("_________________________")
  time.sleep(3)
  maneger()
#remove account
def remacc():
  defdir = r"C:\Users\Public\OnePass\Accounts"
  path1 = os.path.join(defdir, username2)
  os.chdir(path1)
  file = open("key.key", "rb")
  key = file.read()
  file.close()
  f = Fernet(key)
  print("to remove account copy account name and where its from and paste when its asked")
  time.sleep(5)
  folder = "passes"
  path = os.path.join(defdir, username2, folder)
  os.chdir(path)
  lst = os.listdir()
  print("____________________________")
  for account in lst:
    print(account)
  print("____________________________")
  time.sleep(3)
  removable = input("paste which account you want to remove:")
  os.remove(removable)
  print("account removed")



#signup def
def signup():
  username = input("username:")
  password = input("password:")
  defdir = r"C:\Users\Public\OnePass\Accounts"
  path = os.path.join(defdir, username)
  os.mkdir(path)
  os.chdir(path)
  key = Fernet.generate_key()
  file = open("key.key", "wb")
  file.write(key)
  file.close()
  ecrpass = password.encode()
  f = Fernet(key)
  done_password = f.encrypt(ecrpass)
  userfile = open(username + ".key", "wb")
  userfile.write(done_password)
  userfile.close()
  time.sleep(5)
  ask = input("1-go to login page, 2-exit")
  if ask == "1":
    login()
  elif ask == "2":
    exit()
#login def
def login():
  global username2
  global password2
  username2 = input("username:")
  password2 = input("password:")
  defdir = r"C:\Users\Public\OnePass\Accounts"
  path = os.path.join(defdir, username2)
  os.chdir(path)
  list = os.listdir()
  username1 = username2 + ".key"
  if username1 in list:
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    f = Fernet(key)
    file1 = open(username1, "rb")
    passw = file1.read()
    decry = f.decrypt(passw)
    done_pass = decry.decode()
    if done_pass == password2:
      print("good to go ")
      time.sleep(2)
      maneger()
    else:
      print("passwords do not match ")
  else:
    print("user not found")
  
#account system
account = input("do you have an account? y/n:")
if account == "y":
  login()
elif account == "n":
  signup()


