def nombreMystere(y):
    #On récupère chaque chiffre des unités, dizaines et centaines
    c=y//100
    d=(y-c*100)//10
    u=(y-c*100-d*10)//1

    #On teste les différentes conditions :
    
    #On comprends vite que le chiffre des dizaines sera forcément 4 d'après la conditions 5
    if (d!=4):
        return False
    if (c+d+u>10):
        return False
    if (c==0):
        if(u!=2):
            return False
        if (((d+u)%2)==0):
            return False
        if ((d==1)or (d==7)or(u==1) or(u==7)):
            return False
        else: 
            return True
    
    elif (u==3):
            if (((d+c)%2)==0):
                return False
            if ((d==1)or(d==7)or(u==1)or(u==7)or(c==1)or(c==7)):
                    return False
            else :
                return True
          
ok=False
mystery_number=10
while ((ok==False) and (mystery_number<901)):  #On voit rapidement que tous les nombres >900 ne peuvent pas vérifier les conditons 2 et 3 en même temps
    if (nombreMystere(mystery_number)==True):
        print("le chiffre mystère est :",mystery_number)
    y=y+1

