# Your code goes here

if __name__ == "__main__":

    filename = 'students.csv'

    # Ecrivez une fonction permettant de récupérer toutes les lignes
    # du fichier CSV dans une list() `data`
    rows = # TODO
    print(f'\nLe fichier brut contient {len(rows)} lignes')

    # Les étudiants ont chacun un diplôme qui leur est attribué
    # La variable `degrees` contient la liste des diplômes
    degrees = # TODO
    print(f'\nLe fichier contient {len(degrees)} diplômes uniques')

    # Donnez, dans un dict, pour chaque diplôme le nombre d'étudiant
    # par catégorie d'utilisateur (student, alumni, ...)
    #
    #   - Master Un -> Student : 123
    #               -> Alumni : 456
    #               -> ...
    #   - Master Deux -> ...
    #
    users_per_degree = # TODO

    # Enregistrez le dictionnaire dans un nouveau fichier `degree_count.json`
    # TODO
    print(f'\nFichier `degree_count.json` enregistré !')