import random

def is_sorted(lst):
    if len(lst) == 2:
        return sorted(lst) == lst    
    for x in range(0, (len(lst) - 1)):
        if lst[x] > lst[x+1]:
            return False
    return True
    
    
def BogoSort(list) :
  while (True):
    if is_sorted(list):
        return list
    else:  
        random.shuffle(list)
    
#Bogosort – niestabilny, trywialny w dzia³aniu algorytm sortowania o bardzo du¿ej z³o¿onoœci obliczeniowej, oparty na metodzie prób i b³êdów.

#Dzia³anie algorytmu polega na ci¹g³ym losowym ustawianiu sortowanych elementów i sprawdzaniu czy po wymieszaniu elementy s¹ posortowane. #Operacje mieszania powtarzane s¹ a¿ do posortowania elementów. Aby posortowaæ taliê kart tym algorytmem nale¿y wyrzuciæ taliê w powietrze, #pozbieraæ z pod³ogi i sprawdziæ czy karty u³o¿y³y siê w oczekiwany porz¹dek. Czynnoœæ powtarzamy a¿ do uzyskania oczekiwanego efektu.

#Œrednia z³o¿onoœæ obliczeniowa wynosi O((n-1)!) . W przypadku pesymistycznym sortowanie bêdzie trwaæ w nieskoñczonoœæ. Zajêtoœæ pamiêci #wynosi O(n).

