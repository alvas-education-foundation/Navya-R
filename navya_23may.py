Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print('****************************************************************************')
print('##############Enter Valid Username and Password###############\n')
print('****************************************************************************\n')

count=0
while count<3: #counts for 3 attempts
    
    username=input('Enter your username:')
    password=input('Enter your password:')
#print('****************************************************************************\n')

    if username=='Micheal'and password=='e3$WT89x':
        #preinput data
        print('\nYou Have Sucessfully Loggedin!!\n ')
        break
    #Terminates if correct
    else:
        count+=1
        print('\ninvalid username/password\n')
        

        if count==3:
            # waits for 3 attemps after that prog terminates
            print('\nToo many attempts!!! Your account as been locked\n ')
print('****************************************************************************\n')
