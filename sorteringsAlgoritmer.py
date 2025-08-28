import random, tests

#def bogoSort(items):
#    # Kopier den liste, vi har modtaget som parameter, så vi ikke ændrer den originale
#    items = items.copy()
#    isSorted = None # Boolean til markering af, om listen er sorteret
#    attempts = 0 # Tællevariabel til at holde styr på antal af forsøg
#    while not isSorted:
#        attempts += 1
#        if attempts > len(items) * 5000: # Check for at stoppe tendensen mod uendeligt
#            print('Giver op på grund af for mange forsøg ({}) og bruger TimSort'.format(attempts))
#            items.sort()
#            return items
#        random.shuffle(items) # Bland alle elementer helt tilfældigt
#        isSorted = True # Vi går ud fra at listen tilfældigvis er sorteret,
#        # ...og prøver i denne løkke at bevise det modsatte
#        for index in range(len(items)-1):
#            if items[index] > items[index+1]:
#                isSorted = False
#                break # Bryd løkken hvis et eneste element er forkert sorteret
#    print('Sorteret efter {} forsøg'.format(attempts))
#    return items

#bubbleSort sortringsalgoritme
def bubbleSort(items):
    #Kopier den liste, vi modtager som parameter, for ikke at ændrer originale
    items = items.copy()

    # 'for' lykke som køre i antallet af enheder
    # i vores data (items)
    for i in range(len(items)):

        #sørge for vi ikke
        #ender med at dobbelt tjekke allerede sorteret data
        for j in range (1, len(items)-i):

            # 'if' sætning til samligning af data (items index j )
            # ser om indexet er mindre en det forige, samt gør den at vi
            # ikke har brug for et tjek i slutningen af et loop med at se
            # på tal vi allerede har tjekket
            # dette spare lidt resourcer
            # DOG tjekkere vi stadig elementer som kunne være
            # sorteret bare ikke den sidste værdi
            if items[j] < items[j-1]:
                items[j], items[j-1] = items[j-1], items[j]

    #giver den sorteret data tilbage
    return items




#insertSort sorteringsalgoritme
def insertSort(items):
    #Kopier den liste, vi modtager som parameter, for ikke at ændrer originale
    items = items.copy()

    #algoritmen køre i længden af den usorteret liste
    for i in range(len(items)):

        #holder styr på elementet vi sortere for at spare ressourcer
        for j in range(i):

            #samligner elementer
            if items[i] <= items[j]:

                #placere element det rigtige sted
                items[i], items[j] = items[j], items[i]
    return(items)






#mergeSort sorteringsalgoritme
def mergeSort(items):
    items = items.copy()

    middle = len(items)//2

    L = items[:middle]
    R = items[middle:]

    if len(L) > 1:
        L = mergeSort(L)
    if len(R) > 1:
        R = mergeSort(R)

    items = []
    while len(L)>0 and len(R)>0:
        if L[0] >= R[0]:
            items.append(R.pop(0))
        else:
            items.append(L.pop(0))
    else:
        if len(L) == 0:
            items.extend(R)
        else:
            items.extend(L)

    return items




if __name__ == '__main__':
    ## Skriv navnet på den algoritme, der skal testes
    algorithm = mergeSort

    passedTest = True
    for i in range(10):
        l = list(range(0, 10))
        lb = l.copy()
        random.shuffle(lb)
        ls = lb.copy()
        if not tests.sortsCorrectly(ls, algorithm):
            passedTest = False
            break

    if passedTest:
        print('Succes! Algoritmen sorterer korrekt.')
    else:
        print('Fejl! Algoritmen kan ikke sortere.')

    print('blandet: ', lb)
    print('sorteret:', algorithm(ls))
