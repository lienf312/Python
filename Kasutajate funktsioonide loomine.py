# # (4) 2
def seasonInput()->str:
    """Aastaja leidmine
    Tagastab aastaaja nime
    :rtype: str tagastab aastaaja nime
    """
    k = int(input("Sisesta kuu number: "))
    while true:
        if k in range(1, 13):
            break
        else:
            k = int(input("Sisesta kuu number: "))
    return season(k)

#5
def season(kuu:int)->str:
    elif kuu in [9,10,11]:
        return "Sügis"
    else:
        return "Tundmatu kuu"

def bank(aeur:float, years:int)->float:
    for i in range(years):
        aeur = aeur * 1.10
        return round(aeur, 2)

#6
def is_prime(number:float)->bool:
    """
    Kontrollib, kas number on algarv.
    Funktsioon tagastab True, kui number on algarv, vastasel juhul False.
    :param int n: kontrollitav arv
    :return: True, kui arv algarv, False vastasel juhul
    :rtype: bool
    """
    if 0 <= number <= 1001:
        if number in [1, 0]:
        for i in range(1,number):
            if number % i == 0:
                return False
    return True

#7
from datetime import datetime

def date(day, month, year):
    try:
        # Пытаемся создать объект даты
        datetime(year, month, day)
        return True
    except ValueError:
        # Если дата некорректная, будет выброшено исключение
        return False

# 8
def XOR_cipher(text, key):
    encrypted = ''.join(chr(ord(c) ^ key) for c in text)
    return encrypted

def XOR_uncipher(encrypted_text, key):
    decrypted = ''.join(chr(ord(c) ^ key) for c in encrypted_text)
    return decrypted

