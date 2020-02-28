import re

class Password_check(object):

    def __init__(self,password):
        self.password = str(password)

    def lowercase(self):
        lowercase = any(c.islower() for c in self.password)
        return lowercase

    def uppercase(self):
        uppercase = any(c.isupper() for c in self.password)
        return uppercase

    def special_case(self):
        special_sym = "$ @ # %"
        special_sym = any(c in special_sym for c in self.password)
        return special_sym

    def numbers(self):
        numbers_digit = any(c.isdigit for c in self.password)
        return numbers_digit

    def password_is_valid(self):
        lowercase = self.lowercase()
        uppercase = self.uppercase()
        numbers = self.numbers()
        special_case = self.special_case()

        #length = len(self.password)

        result = lowercase and uppercase and special_case and numbers

        if result:

            print("Password meets necessary requirements.")
            return True

        elif not len(self.password) == 0:
            raise Exception("Password must exist")
            return False

        elif not lowercase:
            raise Exception("Password must have atleast one lowercase letter.")
            return False

        elif not uppercase:
            raise Exception("Password must have atleast one uppercase letter.")
            return False

        elif not numbers:
            raise Exception("Password must have atleast one digit/number.")
            return False

        elif not special_case:
            raise Exception("Password must have atleast one special character (i.e $, # etc...).")
        else:
            pass
    
    def pasword_is_ok(self):
        length_error = len(self.password)
        num_digit_error = re.search(r"[0-9]",self.password) is None
        uppercase_error = re.search(r"[A-Z]",self.password) is None
        lowercase_error = re.search(r"[a-z]",self.password) is None
        specialcase_error = re.search(r"[\W]",self.password) is None
        password_is_ok = not (length_error and num_digit_error and uppercase_error) or (specialcase_error and lowercase_error)
        return{
            'password_is_ok':password_is_ok,
            'length_error':length_error,
            'num_digit_error':num_digit_error,
            'lowercase_error':lowercase_error,
            'uppercase_error':uppercase_error,
            'specialcase_error':specialcase_error,
        }
 
c = Password_check('dddd$D12')
print(c.password_is_valid())
# print(c.password_is_ok())
