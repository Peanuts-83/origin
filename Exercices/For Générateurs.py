def intervalle(nbr_bas, nbr_haut):
    """
    yield (générateur simple) remplace __next__ pour la gestion du comportement 
    de l'itérateur 'for'.
    yield est toujours dans une fonction et renvoie forcément 
    une valeur.
    """
    while nbr_bas < nbr_haut:
        yield nbr_bas           # remplace la methode __next__ par yield(générateur)
        nbr_bas += 1
    if nbr_bas == nbr_haut:
        while nbr_bas > 0:
            nbr_bas -= 1
            yield nbr_bas
            

# >>> i=intervalle(5,20)
# >>> for n in i:        ()
# ...     print(n):
# ...     if n < 3:
# ...             i.close()       # close()(coroutine) interrompt la boucle

def intervalle2(nbr_bas, nbr_haut):
    """
    intervalle2 accepte une valeur_recue pour sauter une partie
    de l'itération.
    """
    while nbr_bas < nbr_haut:
        valeur_recue = (yield nbr_bas)
        if valeur_recue is not None:
            nbr_bas = valeur_recue
        nbr_bas += 1

# >>> i=intervalle2(5,25)
# >>> for n in i:
# ...     if n == 15:
# ...             i.send(20)  # envoi de valeur_recue par fonction send()(coroutine)
# ...     print(n, end=" ")
# ... 
# 5 6 7 8 9 10 11 12 13 14 21
# 15 22 23 24 >>>