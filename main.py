def citire_lista():
    l = []
    n = int(input("Dati nr. de elemente:"))
    for i in range(n):
        l.append(int(input("l[" + str(i) + "]=")))
    return l


def print_menu():
    print("1. Citire lista")
    print("2. Subsecventa max nr. pare")
    print("3. Subsecventa max nr. in progresie aritmetica")
    print("4. Subsecventa max nr. concatenate au cif crescatoare")
    print("x. Iesire")


def toate_pare(l):
    '''
    Algoritmul determina daca toate numerel din lista sunt pare
    :param l: lista de numere intregi
    :return: True doar daca toate numerele din lista sunt pare, False in caz contrar
    '''
    for x in l:
        if x % 2 == 1:
            return False
    return True


def get_longest_all_even(l):
    '''
    Functia determina una din cele mai lungi secvente de numere pare din lista
    :param l: lista de numere intregi
    :return: Una din cele mai lungi subsecvente de numere pare din lista
    '''
    subsecventa_max = []
    lungime_max_subsecventa = 0
    for i in range(len(l)):
        for j in range(i, len(l)):
            if toate_pare(l[i:j + 1]) and len(l[i:j + 1]) > lungime_max_subsecventa:
                subsecventa_max = l[i:j + 1]
                lungime_max_subsecventa = len(l[i:j + 1])
    return subsecventa_max


def test_get_longest_all_even():
    assert get_longest_all_even([1, 2, 4, 6, 7, 8, 10, 11, 7]) == [2, 4, 6]
    assert get_longest_all_even([2, 2, 2, 3, 4, 7, 7]) == [2, 2, 2]
    assert get_longest_all_even([3, 4, 6, 7, 4, 2, 10]) == [4, 2, 10]


def progresie_aritmetica(l):
    '''
    Algoritmul verifica daca o lista are elemntele in progresie aritmetica
    :param l: lista de numere intregi
    :return: True daca lista are elemntele in progresie aritmetica, False in caz contrar
    '''
    if len(l)<3:
        return True
    for i in range(2 , len(l)):
        if l[i]-l[i-1] != l[1]-l[0]:
            return False
    return True

def get_longest_arithmetic_progression(l):
    '''
    Algoritmul stabileste una din cele mai lungi secvente de numere in progresie aritmeticfa din lista
    :param l: lista de nr. intregi
    :return: na din cele mai lungi secvente de numere in progresie aritmeticfa din lista
    '''
    subsecventa_max = []
    lungime_max_subsecventa = 0
    for i in range(len(l)):
        for j in range(i, len(l)):
            if progresie_aritmetica(l[i:j+1]) and len(l[i:j+1]) > lungime_max_subsecventa:
                subsecventa_max= l[i:j+1]
                lungime_max_subsecventa = len(l[i:j + 1])
    return subsecventa_max


def test_get_longest_arithmetic_progression():
    assert get_longest_arithmetic_progression([1, 2, 3, 6, 5, 8]) == [1, 2, 3]
    assert get_longest_arithmetic_progression([2, 8, 2, 5, 8]) == [2, 5, 8]
    assert get_longest_arithmetic_progression([1, 2, 6, 7, 8, 10, 11]) == [6, 7, 8]

def cifre_cresc(n):
    u=n%10
    n=n/10
    while(n):
        if u<n%10:
            return False
        u=n%10
        n=n/10
    return True

def nr_cif(n):
    p=0
    while(n):
        p=p+1
        n=n//10
    return p

def concatenare_lista_are_cif_cresc(l):
    '''
    Algoritmul stabileste daca concatenarea numerelor dintr-o lista are cifrele in ord cresc
    :param l: lista de nr intregi
    :return: True daca se respecta conditia, false in caz contrar
    '''
    k=l[0]
    for i in range(1,len(l)):
        k=k * pow(10,nr_cif(l[i])) + l[i]
    return cifre_cresc(k)

def get_longest_concat_digits_asc(l):
    '''
    Algoritmul stabileste una din cele mai lungi secvente dintr-o lista in care concatenarea numerelor are cifrele in ordine crescatoare
    :param l: lista de nr intregi
    :return:cea mai lunga secventa in care concatenarea numerelor are cifrele in ordine crescatoare
    '''
    subsecventa_max = []
    lungime_max_subsecventa = 0
    for i in range(len(l)):
        for j in range(i, len(l)):
            if concatenare_lista_are_cif_cresc(l[i:j+1]) and len(l[i:j]) > lungime_max_subsecventa:
                subsecventa_max = l[i:j + 1]
                lungime_max_subsecventa = len(l[i:j + 1])
    return subsecventa_max



def test_get_longest_concat_digits_asc():
    assert get_longest_concat_digits_asc([1 ,2 ,3 ,2 ,5 ,6, 7]) == [2, 5, 6, 7]
    assert get_longest_concat_digits_asc([1 ,2 ,3 ,4 ,8 ,6 ,7 ,8]) == [1, 2, 3, 4, 8]

def meniu():
    test_get_longest_arithmetic_progression()
    test_get_longest_all_even()
    test_get_longest_concat_digits_asc
    l=[]
    while True:
        print_menu()
        optiune=input("Dati optiunea: ")
        if optiune == "1":
            l=citire_lista()
        elif optiune == "2":
            print(get_longest_all_even(l))
        elif optiune == '3':
            print(get_longest_arithmetic_progression(l))
        elif optiune == '4':
            print(get_longest_concat_digits_asc(l))
        elif optiune == 'x':
            break
        else:
            print("Optiune inexistenta. Reincercati :(")


meniu()

