print("CALCULATRICE SIMPLE")
a = float(input("Premier nombre: "))
b = float(input ("Deuxieme nombre : "))
print("1 Addition")
print("2Soustraction")
print("3 Multiplication")
print("4 Division")
choix = input ("Choisir une opération: ")
if choix == "1":
    print("Résultat:", a + b)
elif choix == "2":
     print("Résultat:", a - b)
elif choix == "3":
     print ("Résultat:", a * b)
elif choix == "4": 
     if b != 0 :
        print("Résultat:", a / b)
     else:
         print("Division impossible")
else : 
         print("Choix invalide")