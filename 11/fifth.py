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
    
#Bogosort � niestabilny, trywialny w dzia�aniu algorytm sortowania o bardzo du�ej z�o�ono�ci obliczeniowej, oparty na metodzie pr�b i b��d�w.

#Dzia�anie algorytmu polega na ci�g�ym losowym ustawianiu sortowanych element�w i sprawdzaniu czy po wymieszaniu elementy s� posortowane. #Operacje mieszania powtarzane s� a� do posortowania element�w. Aby posortowa� tali� kart tym algorytmem nale�y wyrzuci� tali� w powietrze, #pozbiera� z pod�ogi i sprawdzi� czy karty u�o�y�y si� w oczekiwany porz�dek. Czynno�� powtarzamy a� do uzyskania oczekiwanego efektu.

#�rednia z�o�ono�� obliczeniowa wynosi O((n-1)!) . W przypadku pesymistycznym sortowanie b�dzie trwa� w niesko�czono��. Zaj�to�� pami�ci #wynosi O(n).

