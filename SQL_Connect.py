import pyodbc 
import datetime
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=LDW6ZSC2\SQL2012;PORT=1433;DATABASE=MyWork;UID=sa;PWD=myP@ssword')
cursor = cnxn.cursor()
       
myid=1
myname='sid'
selectQuery  = "select * from mywork.dbo.test_emp"
#Insertquery= "insert into mywork.dbo.test_emp(id,name) values ( 1,sid)'
#insertquerywithparams = "insert test_emp(id, name) values (?,?)",myid,myname)"
#cursor.execute ("insert into films (descp) values (?)",exp)
#cursor.execute(selectQuery)

#cursor.execute("insert into test_emp(id, name) values (1,'sid')")
cursor.execute("insert into test_emp (id,name) values (?,?)",myid,myname)


   
#
cursor.commit()

cursor.execute(selectQuery)
for row in cursor:
    print('row = %r' % (row,))
    



