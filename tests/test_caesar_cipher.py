from caesar_cipher.caesar_cipher import *

def test_encrypt_shift() : 
    actual = encrypt('zain' , -9)
    expected = 'qrze'
    assert expected == actual

def test_decrypt_shift() : 
    actual = decrypt('fdriqrze' , 17)
    expected = 'omarzain'
    assert expected == actual

def test_encrypt2() : 
    actual = encrypt('emnv' , 7)
    expected = 'ltuc'
    assert expected == actual

def test_break_code():
    actual = 'it was the best of times it was the worst of times'
    expected = break_code('Sd gkc dro locd yp dswoc sd gkc dro gybcd yp dswoc')
    assert expected == actual