a = input("Value a")
b = input("Value b")

a_input = int(a)
b_input = int(b)

if a_int > b_int and a_int != b_int:
    print("Value a is bigger than Value b")
elif a_int == b_input:
    print("Value a same as Value b")
else:
    print("Value b is bigger than Value b")


Jahr = input("Jahr")
Jahr_int = int(Jahr)

if Jahr_int >= 1928 and Jahr_int <= 1945:
    print("Generation Silent")
elif Jahr_int >= 1946 and Jahr_int <= 1964:
    print("Generation Boomer")

else:
    print("Error!")


t = "Temperatur: "
w = "Wetter?"
t_int = int(t)

if t > 0 and t > 10 and w != "Regen":
    print("Trag eine Jacke")
elif w == "Regen":
    print("Nimm einen Schirm mit!")
elif t > 11 and t < 20 and w != "Regen" and w != "windig":
    print("Fahr mit dem Auto")
elif t > 20 and t < 30 and w != "Sonne" and w != "warm":
    print("Trage kurze Sachen")
else:
    ("Ende!")
