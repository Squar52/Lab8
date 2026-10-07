from array import *
import random

a = int(input("Введіть a: "))
b = int(input("Введіть b: "))

masiv = array('i', [])

for i in range(8):
    x = random.randint(a, b)
    masiv.append(x)

print("Початковий масив:", masiv)

new_masiv = array('i', [])

for x in masiv:
    if x not in new_masiv:
        new_masiv.append(x)

print("Масив без повторень:", new_masiv)