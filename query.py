import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()

mycursor.execute('select studentid , firstname, class from ineuron.fsds')

for i in mycursor:
    print(i)

git config --global user.email "manpreet.singh@praxis.ac.in"