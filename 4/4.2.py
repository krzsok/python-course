def board(nb,nb2):
    
    
    try:
        width = int(nb)
        heigth = int(nb2)
        
        T = ""
        for i in range(heigth):
            for j in range(width):
                T+="+---+"
            T+="\n"
            for j in range(width):
                T+="|   |"
            
            T+="\n"
        for j in range(width):
                T+="+---+"
    
    
    
        return (T)
    
    except ValueError:
      print("invalid number")


def ruler(nb):
    
    
    try:
        number = int(nb)
        T = "|"
        for i in range(number):
            T+=("....|")
        T+=("\n")
        for i in range(number + 1):
            if i <= 9 :
                T += str(i)
                T +=("    ")
            elif (i > 9 and i <= 99) :
                T += str(i)
                T +=("   ")
            elif (i > 99) :
                T += str(i)
                T +=("  ")
        return(T)
        
    except ValueError:
        print("Invalid number")
        
