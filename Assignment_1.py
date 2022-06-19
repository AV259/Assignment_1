def Validate_Username(username):
    if username[0].isalpha()=='False':
        return False
    elif username.find('@')==-1:
        return False
    i = username.find('@')
    elif username.find('.')==i+1:
        return False
    else:
        return True

def Validate_Password(pwd):
    length = len(pwd)
    low_ch = [c for c in pwd if c.islower()]
    high_ch = [u for u in pwd if u.isupper()]
    digit = [d for d in pwd if d.isdigit()]
    spc_ch = [s for s in pwd if s.isalpha=='False' and s.isdigit=='False']
    if (length>5 and length<16) and (len(spc_ch)>0) and (len(digit)>0) and
    (len(high_ch)>0) and (len(low_ch)>0):
        return True
    else:
        return False

def input_username():
    username = input('Enter Username : ')
    return username
def input_password():
    pwd = input('Create a password : ')
    return pwd

    
def Register():
    l=[]
    username=input_username()
    l.append(username)
    pwd=input_password()
    l.append(pwd)
    if Validate_Username(username)=='False':
        print('Invalid Username , Enter again ')
        username=input_username()
        break
    elif Validate_Password(pwd)=='False':
        print('Invalid Password , Create again ')
        pwd=input_password()
        break
    else:
        Account_Details = open('Info.txt',a)
        Account_Details.writelines(l)
        Account_Details.close()
        print('You have successfully registered ')

def Login(username,pwd):
    Account_Details = open('Info.txt',r)
    data = Account_Details.readlines()
    if username in data and pwd in data:
        print('You have successfully Logged In ')
    else:
        print('You will have to register first')
        Register()
    Account_Details.close()

def Forget_Pwd(username):
    Account_Details = open('Info.txt',r)
    data = Account_Details.readlines()
    ind=-1
    for i in range(len(data)):
        if data[i]==username:
            ind=i
            break
    if ind=-1:
        return 0 
    else:
        return (data[ind+1])
           
def main():
    print('Enter 1 to Register and 2 for Login and 3 for Forget Password /n')
    username='',pwd=''
    Account_Details = open('Info.txt',r)
    Account_Details.close()
    ch = int(input('Enter your choice : ')
    if ch==1:
        Register()
    elif ch==2:
        Login(username,pwd)
    else:
        pwd = Forget_Pwd(username)
        if pwd==0:
            print('Register first ! ')
        else:
            print('Your Password is : ',pwd)
if __name__=='__main__':
    main()
    

