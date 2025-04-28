def is_sorted(liste):
    # Repeat this for all pairs (a,b) in liste
    index = 0
    while index < len(liste) - 1:
        #print(f'{index}, {index + 1}')
        a = liste[index]
        b = liste[index + 1]
        if b < a:
            return False
        index = index + 1

    return True
