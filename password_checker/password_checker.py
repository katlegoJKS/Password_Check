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

        # length = len(self.password)

        result = lowercase and uppercase and special_case and numbers

        if result:
            print("Password meets all necessary requirements.")
            return True

        elif not lowercase:
            print("Password must have atleast one lowercase letter.")
            return False

        elif not uppercase:
            print("Password must have atleast one uppercase letter.")
            return False

        elif not numbers:
            print("Password must have atleast one digit/number.")
            return False

        elif not special_case:
            print("Password must have atleast one special character (i.e $, # etc...).")
        else:
            pass


c = Password_check('Katmat$992')
print(c.password_is_valid())