lowest = 0
for i in range (1, 6): 
    cislo = int(input("Zadej " + str(i) + ". číslo: "))
    if lowest == 0:
        lowest = cislo
    elif cislo < lowest:
        lowest = cislo
print ("Nejmenší číslo je číslo", lowest, ".")

    

