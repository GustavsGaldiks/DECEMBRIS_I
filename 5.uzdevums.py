import time

def sveiki(vards):
    stunda = int(time.strftime("%H"))

    if 5 <= stunda < 10:
        return f"Labrīt, {vards}!"
    elif 10 <= stunda < 18:
        return f"Labdien, {vards}!"
    elif 18 <= stunda < 24:
        return f"Labvakar, {vards}!"
    else:
        return f"sveiki, {vards}!"

def cilveks():
    vards = input("Ievadi savu vārdu: ")
    return vards.capitalize()

vards1 = cilveks()
sveiki = sveiki(vards1)
print(sveiki)