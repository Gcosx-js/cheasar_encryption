import time
import os
import random

def encrypt(text, eded):
    t = ""
    for i, enc in enumerate(text):
        t += chr(ord(enc) + eded)
    return t

def decrypt(text, eded):
    t = ""
    for i, dec in enumerate(text):
        t += chr(ord(dec) - eded)
    return t
def encrypt_2(pt, eded):
    ct = ""
    for i, xk in enumerate(pt):
        sifrele = ord(eded[i % len(eded)])
        c_c = chr((ord(xk) + sifrele) % 256)
        ct += c_c
    return ct

def decrypt_2(ct, eded):
    pt = ""
    for i, xk in enumerate(ct):
        sifrele = ord(eded[i % len(eded)])
        pc = chr((ord(xk) - sifrele + 256) % 256)
        pt += pc
    return pt
while True:
    os.system('cls')
    user = int(input("""
                1 - Decrypt\n
                2 - Encrypt\n
                3 - Çıx\n
                Seçim : """))

    if user == 1:
        print("Bu proses üçün sizin Şifrələmə nömrəniz lazımdır.")
        eded = str(input("Şifrələmə nömrəsi : "))
        text = str(input("Decrypt olunacaq mətn : "))
        try:
            done = decrypt(text,int(eded))
            
            print("Decrypt olunmuş mətn : {}".format(decrypt_2(done,eded.upper())))
            time.sleep(8)
            continue
        except:
            print("Bu nömre Decrpyt oluna bilmez!")
    elif user == 2:
        eded = random.randint(1,50)
        print("Sizin şifrələmə nömrəniz : {}".format(eded))
        text = str(input("Encrypt olunacaq mətn : "))
        done = encrypt(text,int(eded))
        print("Encrypt olunmuş mətn : {}".format((encrypt_2(done,str(eded).upper()))))
        time.sleep(8)
        continue
    elif user == 3:
        break
