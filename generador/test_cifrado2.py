from cifradofuncional import encrypt
import pytest
# def test_encriptado():
#     messageCrypt=crypt("hola",1)
#     assert messageCrypt.encrypt()=="ipmb"
@pytest.mark.parametrize(
    "input_a,input_b,expected",
    [
        ("hola",1,"ipmb"),
        ("abc",2,"cde"),
        ("abc",4,"efg"),

    ]
)
def test2(input_a,input_b,expected):
    
    assert encrypt(input_a,input_b)==expected
    
    
   
