"""
    Funkcija akrs akceptē trīs argumentus - skaiļus viens, divi un trīs, 
    aprēķina to kubu starpību un atgriež to.
    Pārbaudiet funkcijas darbību ar dažādiem argumentiem, ievadot nepieciešamās
    vērtības un parādot skaitli ar pieciem simboliem aiz komata.

    Argumenti:
        viens {int vai float} -- pirmais skaitlis
        divi {int vai float} -- otrais skaitlis
        tris {int vai float} -- trešais skaitlis
    Atgriež:
        int vai float -- argumentu kubu starpību
 """

 def akrs(viens,divi,tris):
   starpiba=1**5-2**5-3**5
   return starpiba

  pirmais=int(input("ievadi pirmo skaitli: "))
  otrais=int(input("ievadi otro skaitli: "))
  tresais=int(input("ievadi treso skaitli "))

  aka=akrs(pirmais,otrais)

  print("{0:.5f}".format(aka))