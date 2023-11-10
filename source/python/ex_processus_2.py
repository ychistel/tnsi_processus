nb_ligne = 0
with open("test.txt", mode='a') as f:
    while nb_ligne < 1:
        f.write("Le bloc notes utilise peu de ressources!\n")
        nb_ligne += 1