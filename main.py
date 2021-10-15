import math


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
    print("5. Subsecventa max nr. patrate perfecte")
    print("6. Subsecventa max nr. prime")
    print("7. Subsecventa max nr. cu semne alternante")
    print("8. Subsecventa max nr. crescatoare")
    print("9. Subsecventa max nr. palindrom")
    print("10. Subsecventa max de nr. div cu k")
    print("11. Subsecventa max nr. neprime")
    print("12. Subsecventa max de nr. care au același număr de biți de 1 în reprezentarea binară")

    print("x. Iesire")


def este_patrat_perfect(n):
    k=int(math.sqrt(n))
    if(k==n/k):
        return True;
    return False;


def sir_patrat_perfect(l):
    '''
    Algoritmul determina daca toate numerele din lista sunt patrate perfecte
    :param l: lista de numere intregi
    :return: True daca toate nr sun patrate perfecte, fase in caz contrar
    '''
    for x in l:
        if este_patrat_perfect(x) == False:
            return False
    return True

def get_longest_all_perfect_squares(l):
    '''
    Algoritmul stabileste una din cele mai lungi secvente de numere patrate perfecte dintr-un sir
    :param l: lista denumere intregi
    :return: una din cele mai lungi secvente de numere patrate perfecte dintr-un sir
    '''
    subsecventa_max=[]
    lungime_max_subsecventa=0
    for i in range(len(l)):
        for j in range(i,len(l)):
            if sir_patrat_perfect(l[i:j+1]) and len(l[i:j+1]) > lungime_max_subsecventa:
                subsecventa_max = l[i:j+1]
                lungime_max_subsecventa = len(l[i:j+1])
    return subsecventa_max


def test_get_longest_all_perfect_squares():
    assert get_longest_all_perfect_squares([2,36,49,3,4,16,25]) == [4,16,25]
    assert get_longest_all_perfect_squares([36,49,4,3,7,4,16]) == [36,49,4]


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
            if concatenare_lista_are_cif_cresc(l[i:j+1]) and len(l[i:j+1]) > lungime_max_subsecventa:
                subsecventa_max = l[i:j + 1]
                lungime_max_subsecventa = len(l[i:j + 1])
    return subsecventa_max


def test_get_longest_concat_digits_asc():
    assert get_longest_concat_digits_asc([1 ,2 ,3 ,2 ,5 ,6, 7]) == [2, 5, 6, 7]
    assert get_longest_concat_digits_asc([1 ,2 ,3 ,4 ,8 ,6 ,7 ,8]) == [1, 2, 3, 4, 8]


def este_prim(n):
    if(n<2):
        return False
    if(n==2):
        return True
    if(n%2==0):
        return False
    for i in range(3,n//2+1,2):
        if n%i == 0:
            return False
    return True


def este_sir_prim(l):
    '''
    stabileste daca o lista este prim
    '''
    for x in l:
        if este_prim(x) == False:
            return False
    return True


def get_longest_all_primes(l):
    '''
    stabileste una din cele mai lungi secvente de numere prime dintr-o lista
    :param l: lista de numere intregi
    :return: una din cele mai lungi secvente de numere prime dintr-o lista
    '''
    subsecventa_max=[]
    for i in range(len(l)):
        for j in range(i, len(l)):
            if este_sir_prim(l[i:j+1]) and len(l[i:j+1]) > len(subsecventa_max):
                subsecventa_max = l[i:j + 1]
    return subsecventa_max


def test_get_longest_all_primes():
    assert get_longest_all_primes([2,3,5,4,7,11]) == [2,3,5]
    assert get_longest_all_primes([2, 3, 5, 4, 7, 11, 2, 2]) == [7,11,2,2]


def este_sir_alternant(l):
    '''
    stabileste daca o lista are semnele elementelor alternante
    :param l: lista de numere intregi
    :return: True daca lista are semnele elementelor alternante, False in caz contrar
    '''
    for i in range(1,len(l)):
        if l[i] < 0 and l[i-1] < 0:
            return False
        if l[i] >=0 and l[i-1] > 0:
            return False
    return True

def get_longest_alternating_signs(l):
    '''
    stabileste una din cele mai lungi secvente de numere cu semne alternante dintr-o lista
    :param l: lista de numere intregi
    :return: una din cele mai lungi secvente de numere cu semne alternante dintr-o lista
    '''
    subsecventa_max = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if este_sir_alternant(l[i:j + 1]) and len(l[i:j + 1]) > len(subsecventa_max):
                subsecventa_max = l[i:j + 1]
    return subsecventa_max


def test_get_longest_alternating_signs():
    assert get_longest_alternating_signs([-1,2,-3,4,5,-6]) == [-1,2,-3,4]
    assert get_longest_alternating_signs([1,-2,3,3,-4,5,-6]) == [3, -4, 5, -6]


def sir_crescator(l):
    '''
    verifica daca un sir are toate elementele crescatoare
    '''
    for i in range(1,len(l)):
        if l[i]<l[i-1]:
            return False
    return True


def get_longest_sorted_asc(l):
    '''
    stabileste una din cele mai lungi secvente crescatoare de numere din lista
    :param l: lista de numere intregi
    :return: una din cele mai lungi secvente crescatoare de numere din lista
    '''
    subsecventa_max = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if sir_crescator(l[i:j + 1]) and len(l[i:j + 1]) > len(subsecventa_max):
                subsecventa_max = l[i:j + 1]
    return subsecventa_max


def test_get_longest_sorted_asc():
    assert get_longest_sorted_asc([1,2,7,6,5,4]) == [1,2,7]
    assert get_longest_sorted_asc([3,2,5,4,5,6]) == [4,5,6]


def invers(n):
    k=0;
    while n:
        k=k*10 + n%10
        n = n//10
    return k

def palindrom(n):
    return n == invers(n)

def sir_cu_numere_palindrom(l):
    for x in l:
        if palindrom(x) == False:
            return False
    return True


def get_longest_all_palindromes(l):
    '''
    stabileste una din cele mai lungi secvente de palindroame din lista
    :param l: lista de numere intregi
    :return: una din cele mai lungi secvente de palindroame din lista
    '''
    subsecventa_max = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if sir_cu_numere_palindrom(l[i:j + 1]) and len(l[i:j + 1]) > len(subsecventa_max):
                subsecventa_max = l[i:j + 1]
    return subsecventa_max


def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([121,232,56,3443]) == [121,232]
    assert get_longest_all_palindromes([121,232,56,3443,2,676]) == [3443,2,676]


def sir_div_cu_k(l,k):
    for x in l:
        if x%k != 0:
            return False
    return True


def get_longest_div_k(l,k):
    '''
    stabileste una din cele mai lungi secvente de numere divizibile cu k dintr-o lista
    :param l: lista de numere intregi
    :return: una din cele mai lungi secvente de numere divizibile cu k dintr-o lista
    '''
    subsecventa_max = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if sir_div_cu_k(l[i:j + 1],k) and len(l[i:j + 1]) > len(subsecventa_max):
                subsecventa_max = l[i:j + 1]
    return subsecventa_max

def este_sir_neprim(l):
    '''
    stabileste daca o lista are toate elementele neprime
    '''
    for x in l:
        if este_prim(x) == True:
            return False
    return True



def  get_longest_all_not_prime(l):
    '''
    stabileste una din cele mai lungi secvente de numere prime dintr-o lista
    :param l: lista de numere intregi
    :return: una din cele mai lungi secvente de numere prime dintr-o lista
    '''
    subsecventa_max=[]
    for i in range(len(l)):
        for j in range(i, len(l)):
            if este_sir_neprim(l[i:j+1]) and len(l[i:j+1]) > len(subsecventa_max):
                subsecventa_max = l[i:j + 1]
    return subsecventa_max


def suma_sir_este_prima(l):
    '''
    verifica daca suma elementelor unei liste este nr primm
    '''
    s=0
    for x in l:
        s=s+x
    return este_prim(s)


def get_longest_sum_is_prime(l):
    '''
    stabileste una din cele mai lungi secvente de numere a carui suma este nr prim
    :param l: lista de numere intregi
    :return: una din cele mai lungi secvente de numere a carui suma este nr prim
    '''
    subsecventa_max=[]
    for i in range(len(l)):
        for j in range(i, len(l)):
            if suma_sir_este_prima(l[i:j+1]) and len(l[i:j+1]) > len(subsecventa_max):
                subsecventa_max = l[i:j + 1]
    return subsecventa_max


def prod_elem_sir_impar(l):
    p=1
    for x in l:
        p=p*x
    if x%2 == 1:
        return True
    return False


def get_longest_product_is_odd(l):
    '''
        stabileste una din cele mai lungi secvente de numere a carui produs este impar
        :param l: lista de numere intregi
        :return: una din cele mai lungi secvente de numere a carui produs este impar
        '''
    subsecventa_max = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if prod_elem_sir_impar(l[i:j + 1]) and len(l[i:j + 1]) > len(subsecventa_max):
                subsecventa_max = l[i:j + 1]
    return subsecventa_max


def toate_elem_pare(l):
    "verifica daca o lista are toate elem pare"
    for x in l:
        if x%2 == 1:
            return False
    return True


def get_longest_all_even(l):
    '''
            stabileste una din cele mai lungi secvente de numere a carui produs este impar
            :param l: lista de numere intregi
            :return: una din cele mai lungi secvente de numere a carui produs este impar
            '''
    subsecventa_max = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if toate_elem_pare(l[i:j + 1]) and len(l[i:j + 1]) > len(subsecventa_max):
                subsecventa_max = l[i:j + 1]
    return subsecventa_max


def baza_10_in_baza_2(n):
    p=1
    n_baza_2=0
    while n:
        n_baza_2=n_baza_2 + n%2 * p
        p=p * 10
        n=n//2
    return n_baza_2


def nr_de_1_in_baza_2(n):
    k=baza_10_in_baza_2(n)
    c=0
    while k:
        if k%10 == 1:
            c = c+1
        k= k//10
    return c


def elem_sir_au_nr_egal_de_1_in_baza_2(l):
    '''algoritmul stabileste daca elementele unui sir au acelasi numar de 1 in reprezentarea binara'''
    primul_elem= nr_de_1_in_baza_2(l[0])
    for i in range (1, len(l)):
        if nr_de_1_in_baza_2(l[i]) != primul_elem:
            return False
    return True


def  get_longest_same_bit_counts(l):
    '''
    stabileste una din cele mai lungi secvente de numere a carui produs este impar
    :param l: lista de numere intregi
    :return: una din cele mai lungi secvente de numere a carui produs este impar
    '''
    subsecventa_max = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if elem_sir_au_nr_egal_de_1_in_baza_2(l[i:j + 1]) and len(l[i:j + 1]) > len(subsecventa_max):
                subsecventa_max = l[i:j + 1]
    return subsecventa_max


def nr_div(n):
    c=0
    for i in range(1,n+1):
        if n%i == 0:
            c= c+1
    return c

def elem_sir_au_acelasi_nr_div(l):
    primul_elem= nr_div(l[0])
    for i in range(1,len(l)):
        if nr_div(l[i]) != primul_elem:
            return False
    return True

def get_longest_same_div_count(l):
    '''
    stabileste una din cele mai lungi secvente de numere cu acelasi nr de div
    :param l: lista de numere intregi
    :return: una din cele mai lungi secvente de numere cu acelasi nr de div
    '''
    subsecventa_max = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if elem_sir_au_acelasi_nr_div(l[i:j + 1]) and len(l[i:j + 1]) > len(subsecventa_max):
                subsecventa_max = l[i:j + 1]
    return subsecventa_max


def are_toate_cif_prime(n):
    while n:
        if este_prim(n%10) == False:
            return False
        n=n//10

    return True

def sir_cu_toate_nr_cu_cif_prime(l):
    for x in l:
        if are_toate_cif_prime(x) == False:
            return False
    return True

def get_longest_prime_digits(l):
    '''
        stabileste una din cele mai lungi secvente de numere ce au doar cifre prime
        :param l: lista de numere intregi
        :return: una din cele mai lungi secvente de numere ce au doar cifre prime
        '''
    subsecventa_max = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if sir_cu_toate_nr_cu_cif_prime(l[i:j + 1]) and len(l[i:j + 1]) > len(subsecventa_max):
                subsecventa_max = l[i:j + 1]
    return subsecventa_max

def scrierea_lui_n_ca_x_la_k(n,k):
    i=1
    while i**k<=n:
        if i**k==n:
            return True
        i=i+1
    return False


def meniu():
    test_get_longest_arithmetic_progression()
    test_get_longest_all_even()
    test_get_longest_concat_digits_asc()
    test_get_longest_all_perfect_squares()
    test_get_longest_all_primes()
    test_get_longest_alternating_signs()
    test_get_longest_sorted_asc()
    test_get_longest_all_palindromes()
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
        elif optiune == '5':
            print(get_longest_all_perfect_squares(l))
        elif optiune =='6':
            print(get_longest_all_primes(l))
        elif optiune =='7':
            print(get_longest_alternating_signs(l))
        elif optiune == '8':
            print(get_longest_sorted_asc(l))
        elif optiune == '9':
            print(get_longest_all_palindromes(l))
        elif optiune == '10':
            k=int(input("Dati un nr.:"))
            print(get_longest_div_k(l,k))
        elif optiune =='11':
            print(get_longest_all_not_prime(l))
        elif optiune == '12':
            print(get_longest_same_bit_counts(l))
        elif optiune == 'x':
            break
        else:
            print("Optiune inexistenta. Reincercati :(")

meniu()



