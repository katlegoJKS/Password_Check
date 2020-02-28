from password_checker.password_checker import Password_check

password = 'Katmat$992'
pass_checker = Password_check(password)

def test_lowercase():
    assert pass_checker.lowercase() == True

def test_uppercase():
    assert pass_checker.uppercase() == True
    
def test_numbers():
    assert pass_checker.numbers() == True

def test_password_is_valid():
    assert pass_checker.password_is_valid() == True

def test_special_case():
    assert pass_checker.special_case() == True
