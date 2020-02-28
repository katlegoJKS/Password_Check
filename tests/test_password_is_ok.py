from password_checker.password_checker import Password_check

password = 'aaAAA$$$$1'
pass_checker = Password_check(password)

length = len(password)

def test_special_case():
    assert pass_checker.special_case() == True

def test_length():
    assert length > 8

def test_if_empty():
    assert password != []