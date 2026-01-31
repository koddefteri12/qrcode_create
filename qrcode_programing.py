import qrcode
from colorama import *
init(autoreset=True)

url=input("Link veya kısa metin giriniz:  ")

img = qrcode.make(url).save("qr.png")

print(Fore.GREEN+"Başarılı şekilde kaydedildi")