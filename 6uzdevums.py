"""
Uzrakstiet Python programmu, lai iegūtu 
starpību starp ievadīto skaitli un 17.
Ja skaitlis ir lielāks par 17, iegūstiet absolūtās vērtības starpības dubultu..

"""

sk1=int(input("Ievadi pirmo skaitli "))
sk2=int(17)

starpība=sk1-sk2

if starpība > 17:
    absv=int(starpība*starpība)
    print(absv)
else:
    print(starpība)