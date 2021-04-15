
if __name__ == "__main__":

    filename = 'students.csv'
    filename = open("students.csv", "r+")     # mode lecture/écriture
    rows = filename.readlines()
  
    print(f'\nLe fichier brut contient {len(rows)} lignes')
    liste=[]
    Teacher=[0,0,0,0,0,0]
    Alumni=[0,0,0,0,0,0]
    Student=[0,0,0,0,0,0]
    
    for i in range (len(rows)):
        temp ="".join(rows[i])
        liste.append(temp.split(","))
        
        if liste[i][4]=="Master Un":
            if (liste[i][5]=="Teacher\n"):
                Teacher[0]=Teacher[0]+1
            elif (liste[i][5]=="Student\n"):
                Student[0]=Student[0]+1
            elif (liste[i][5]=="Alumni\n"):
                Alumni[0]=Alumni[0]+1
                
        elif liste[i][4]=="Master Deux":
            if (liste[i][5]=="Teacher\n"):
                Teacher[1]=Teacher[1]+1
            elif (liste[i][5]=="Student\n"):
                Student[1]=Student[1]+1
            elif (liste[i][5]=="Alumni\n"):
                Alumni[1]=Alumni[1]+1
        
        elif liste[i][4]=="Master Trois":
            if (liste[i][5]=="Teacher\n"):
                Teacher[2]=Teacher[2]+1
            elif (liste[i][5]=="Student\n"):
                Student[2]=Student[2]+1
            elif (liste[i][5]=="Alumni\n"):
                Alumni[2]=Alumni[2]+1
                
        elif liste[i][4]=="Master Quatre":
            if (liste[i][5]=="Teacher\n"):
                Teacher[3]=Teacher[3]+1
            elif (liste[i][5]=="Student\n"):
                Student[3]=Student[3]+1
            elif (liste[i][5]=="Alumni\n"):
                Alumni[3]=Alumni[3]+1
                
        elif liste[i][4]=="Master Cinq":
            if (liste[i][5]=="Teacher\n"):
                Teacher[4]=Teacher[4]+1
            elif (liste[i][5]=="Student\n"):
                Student[4]=Student[4]+1
            elif (liste[i][5]=="Alumni\n"):
                Alumni[4]=Alumni[4]+1
                
        elif liste[i][4]=="Master Six":
            if (liste[i][5]=="Teacher\n"):
                Teacher[5]=Teacher[5]+1
            elif (liste[i][5]=="Student\n"):
                Student[5]=Student[5]+1
            elif (liste[i][5]=="Alumni\n"):
                Alumni[5]=Alumni[5]+1
                
    dictionnaireUn={"Student":Student[0],"Teacher":Teacher[0],"Alumni":Alumni[0]}
    dictionnaireDeux={"Student":Student[1],"Teacher":Teacher[1],"Alumni":Alumni[1]}
    dictionnaireTrois={"Student":Student[2],"Teacher":Teacher[2],"Alumni":Alumni[2]}
    dictionnaireQuatre={"Student":Student[3],"Teacher":Teacher[3],"Alumni":Alumni[3]}
    dictionnaireCinq={"Student":Student[4],"Teacher":Teacher[4],"Alumni":Alumni[4]}
    dictionnaireSix={"Student":Student[5],"Teacher":Teacher[5],"Alumni":Alumni[5]}

    dict={"Master Un":dictionnaireUn,
          "Master Deux":dictionnaireDeux,
          "Master Trois":dictionnaireTrois,
          "Master Quatre":dictionnaireQuatre,
          "Master Cinq":dictionnaireCinq,
          "Master Six":dictionnaireSix}
    
    import json

    with open('data.json', 'w') as fp:
        json.dump(dict, fp)

    with open('data.json', 'r') as fp:
        data = json.load(fp)
    print(f'\nFichier `degree_count.json` enregistré !')
