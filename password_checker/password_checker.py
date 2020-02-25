class Password_check:
    
    def __init__(self):
        pass

    def password_is_valid(self,password):

        number = ['0','1','2','3','4','5','6','7','8','9']
        letter_lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','s','o','p','q','r','s','t','u','v','w','x','y','z']
        letter_uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        special_cases = ['{','}','%','&','*','_','$']
        result = True

        if len(password) < 8:
            result = False

        if not any(char.isdigit() for char in password):
            result = False

        if not any(char.isupper() for char in password):
            result = False

        if not any(char.islower() for char in password):
            result = False

        if not any(char in special_cases for char in password):
            result = False
        if result:
            return result


p = Password_check()
p.password_is_valid('')

def main():
    password = 'Kat$mss12'

    if (p.password_is_valid(password)):
        print("password is valid")
    else:
        print("password is invalid")

if __name__ == "__main__":
    main()