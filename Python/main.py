
# integer int()
x = 12
y = 5

# float-point numbers float()
pi = 3.14
tau = 6.28

# str()
uvod = "Moje ime je "
ime = "Luka"

# bool()
bool1 = True
bool2 = False

# nicelna vrednost
nicelnaVrednost = None



#print(uvod + ime + " in star sem " + str(29))
#print(x / y)
#print(bool2)


starost = int(input("Koliksna je tvoja starost?"))
starost = starost + 1
#
# print(starost)

# print("Vpisi dve stevili, ki ju zelis sesteti. ")
# prvo = int(input("Vpisi prvo stevilo: "))
# drugo = int(input("Vpisi drugo stevilo: "))
#
# print("Tvoj sestevek je: " + str(prvo + drugo))

if starost > 18:
    print("povej masten vic")
elif starost > 17:
    print("najstniki")
elif starost == 15:
    print("bodi tiho")
else:
    print("povej baby vic")

feedback = input("mi podas feedback na moj vic")

if feedback == ("DA").lower():
    print("je bilo smesno")
else:
    print("hvala za pozornost")

