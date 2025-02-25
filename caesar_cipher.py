

# 'key' is the amount to shift a character down the alphabet
def caesar_encrypt(pt, key):
    ct = ""
    ct_c = ""
    for pt_c in pt:
        if 65 <= ord(pt_c) <= 90: # lowercase letter
            ord_a = 65
            ct_c = chr((ord(pt_c) - ord_a + key) % 26 + ord_a)
        elif 97 <= ord(pt_c) <= 122: # uppercase letter
            ord_A = 97
            ct_c = chr((ord(pt_c) - ord_A + key) % 26 + ord_A)
        else:
            ct_c = " "
        ct = ct + ct_c
    return ct

def caesar_decrypt(ct, key):
    return caesar_encrypt(ct, -key)

def caesar_crack(ct):
    for i in range(26):
        print(caesar_decrypt(ct,i))
