##def Setpassword(password=''):
##    assert type(password)==str,'Password must be a string'
##    
##    if password=='':
##        password=input('Type your password here:')
##        if len(password)<=8:
##            print('Password must be at least 8 characters')
##            Setpassword()
##            
##        if not password.isalnum():
##            print('Password must have numbers and letters.')
##            Setpassword()
##    
##        if password.islower():
##            print('Must have upper and lowercase letters')
##            Setpassword()
##            
##        if password.isupper():
##            print('Must have upper and lowercase letters')
##            Setpassword()
##        else:
##            print('Your password is set')
##
##    else:
##        enter=input('Enter your password here:')
##        if enter==password:
##            print("You're in!")
##        else:
##            print("Try again")
##            print(enter)

class Diary(object):
    'A Personal Diary'

    def __init__(self,name):
        'This is the contructor'
        assert type(name)==str and len(name)>=2, 'name must be a string with at least 2 characters'
        self.__name=name
        self.__d={}

    def getName(self):
        'Gives you the name on the diary'
        return self.__name

    def setName(self, new_name):
        'Changes the name of the diary'
        assert type(new_name)==str and len(new_name)>=2, 'new_name must be a string with at least 2 characters'
        self.__name=new_name
        print(f"Your diary's name has been changed to {self.__name}.")

    def __text__(self):
        'the inner workings on the entry'
        date=input("What is today's date?(mm/dd/yy):")
        if len(date)==8:
            print('Date is set!')
        else:
            print('Please use the mm/dd/yy format')
            self.newEntry()
        text=input('Write your entry here:')
        print(f'Signed {self.__name}')
        final=text +' '+ f'Signed {self.__name}'
        self.__d={date : final}

    def showEntry(self,date):
        'Shows the entry of the date of your choosing'
        print(self.__d[date])

    def __getitem__(self, item):
        'Makes Diary() subscriptable.'
        return self.__d[item]

    def newEntry(self):
        'creates a new entry'
            self.__text__()
            

    def __repr__(self):
        return f"Diary('{self.__name}')"

    def __str__(self):
        return f"This Diary belongs to {self.__name}."
    

    
    

    
    

    
                


    
