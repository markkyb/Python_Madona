"""
Uzrakstiet programmu Python, lai aprēķinātu cilindra tilpumu un virsmas laukumu.

Piezīme: Cilindrs ir viena no visvienkāršākajām izliektajām ģeometriskajām 
formām, virsma, ko veido punkti fiksētā attālumā no noteiktās taisnes, 
cilindra ass..

Piezīme:
Ievaddati: Pamata rādiuss un cilindra augstums
Izvaddati: Cilindra virsmas laukums un tilpums 
"""

from math import pi
r=float(input("Ievadi pamata radiusu: "))
O=float(input("Ievadi augstumu: "))


V= r*O
P=2*pi*r*O
S=pi*r**2
J=2*S+P
print("Tilpums ir:",V,"Cilindra virsmas laukums:", J)