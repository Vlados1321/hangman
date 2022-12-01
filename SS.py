import os

abc26 = '''ABCDEFGHIJKLMNOPQRSTUVWXYZ'''


# мысли для улучшения / вывод решения / добавить колькулятор не только для 10 сс
# на данный момент мы способны переводи в и из до 36ричной системы, 1-10 + A-Z
def _10_n(int10, ssn):  # int10 -> int     ssn -> int
    tc_ = []
    a, b, ost = int10, ssn, 0
    while True:
        if a < b:
            tc_.append(a)
            break
        tc_.append(a % b)
        a = a // b

    for i in range(len(tc_)):
        tc_[i] = str(tc_[i])
    tc_ = tc_[::-1]
    if ssn <= 10:
        return ''.join(tc_)
    else:  # В случае если ssn больше обычной десятичной
        # к этому моменту мы имеем что то на подобие [1, 12, 3, 18, 25]
        tc_ = "/".join(tc_)
        for i in range(10, 36):
            tc_ = tc_.replace(str(i), abc26[i - 10])
        tc_ = tc_.replace("/", "")
        return tc_


def _n_10(n, ss_n):  # n -> str      ss_n -> int
    tc_ = []
    n = "|".join(list(n))  # n = '1|f|2' # разделяем элементы
    for i in range(10, 36):  # разшифровка из ABC в 10, 11 и 12
        n = n.replace(abc26[i - 10], str(i))
    n = n.split("|")  # n = ['1', '15', '2']
    for i in range(len(n)):
        n[i] = int(n[i])
    sumn = 0  # n = [1, 15, 2]
    for i in range(len(n)):
        sumn = sumn + (n[i] * ss_n ** (len(n) - i - 1))
    return sumn


def stp(s):  # x -> int\str
    s = str(s)
    step = '⁰¹²³⁴⁵⁶⁷⁸⁹'
    tc = ''
    for i in s:
        tc += step[int(i)]
    # tc = '²³'
    return tc


def ss_d(ss):  # ss -> int\str
    ss = str(ss)
    sss = '₀₁₂₃₄₅₆₇₈₉'
    tc = ''
    for i in ss:
        tc += sss[int(i)]
    # tc = '₂₃'
    return tc


def gdz(ii, ssi, ssn):  # ii -> str   ssi -> int   ssn -> int
    # входящие данные уже проверенны таккак они исходом из go()
    tc_ = []
    print(f'{ii}{ss_d(ssi)} -> n{ss_d(ssn)}')
    if ssi == 10:
        ii = int(ii)
        a, b = ii, ssn
        while True:  # из 10 в n (ss) пока без перевода в ABC
            if a // b < b:
                print(f'{a} : {b} = {a // b}'.ljust(20), f'<---^->{a % b} - ост')
                tc_.append(a % b)
                tc_.append(a // b)
                break
            print(f'{a} : {b} = {a // b}'.ljust(20), f'    |->{a % b} - ост')
            tc_.append(a % b)
            a = a // b
        tc_ = tc_[::-1]
        if len(tc_) > 1:  # убираем лишний перый нуль
            if tc_[0] == 0:
                tc_ = tc_[1:]

        print("МЫ имеем:", *tc_)
        # tc_ имеет вид [2, 15, 1]
        for i in range(len(tc_)):
            tc_[i] = str(tc_[i])
        tc_ = "|".join(tc_)  # '1|15|2'
        for i in tc_.split('|'):
            if int(i) >= 10:
                print("Заменяем: ", end='')
            break
        isp = ''
        for i in tc_.split('|'):  # проходим по списку из ['1', '15', '2']
            if (i not in isp) and int(i) >= 10:
                print(f'{i}={abc26[int(i) - 10]}', end=' ')
                isp += i

        for i in range(10, 36): # переводим цифры более 9 в буквы
            tc_ = tc_.replace(str(i), abc26[i - 10])
        tc_ = "".join(tc_.split('|'))
        # tc_ имеет вид 1F2
        print('\n', tc_, ss_d(ssn),sep='')
    else:  # tc_ - пустой список -------------------------------------------
        tc_, b = ii, ssi  # сначало переведём в 10 сс
        isp = ''
        for i in range(len(tc_)):
            print(f'{tc_[i]}{stp(len(tc_) - i - 1)}', end='')
        print()
        if not tc_.isdigit():
            print("Заменяем: ", end='')
        for i in tc_:  # tc_ имеет вид '1f1' str
            if (i not in isp) and not i.isdigit():
                print(f'{i}={abc26.index(i) + 10}', end=' ')
                isp += i
        # теперь реально переводим их в числа
        tc_ = list(tc_)
        for i in range(len(tc_)):  # tc_ ['1', 'F', '2']
            if not tc_[i].isdigit():
                tc_[i] = abc26.index(tc_[i]) + 10
        print()
        for i in range(len(tc_)):  # создае́м выражение
            print(f'{tc_[i]}{stp(len(tc_) - i - 1)}', end="")
        print(" -> ", end="")
        txt = ''
        for i in range(len(tc_)):
            txt += f"{tc_[i]} • {ssi}{stp(len(tc_) - i - 1)} + "
        txt = txt[:-2]  # '1 • 16² + 15 • 16¹ + 2 • 16⁰'
        txt += '='
        sumtxt = 0
        for i in range(len(tc_)):  # подщитывает решение
            sumtxt += (int(tc_[i]) * ssi ** (len(tc_) - 1 - i))
        print(f'{txt} {sumtxt}{ss_d(10)}')
        # 1¹5⁰ -> 1 • 16¹ + 5 • 16⁰ = 21₁₀
        # sumtxt = 21
        if ssn != 10:
            ii = sumtxt  # 21.10
            a, b, tc_ = ii, ssn, []
            while True:  # из 10 в n (ss) пока без перевода в ABC
                if a // b < b:
                    print(f'{a} : {b} = {a // b}'.ljust(20), f'<---^->{a % b} - ост')
                    tc_.append(a % b)
                    tc_.append(a // b)
                    break
                print(f'{a} : {b} = {a // b}'.ljust(20), f'    |->{a % b} - ост')
                tc_.append(a % b)
                a = a // b
            tc_ = tc_[::-1]  # tc_ = list[int]
            print("МЫ имеем:", *tc_)
            for i in range(len(tc_)):
                tc_[i] = str(tc_[i])
            #print(f'{"".join(tc_)}{ss_d(ssn)}') скоро уберём
            for j in tc_:
                if len(j)==2:
                    isp = ''
                    print('Заменим:', end=' ')
                    for i in range(len(tc_)):
                        if int(tc_[i]) > 9:
                            print(f'{tc_[i]}={abc26[int(tc_[i]) - 10]}', end=' ')
                            tc_[i] = abc26[int(tc_[i])-10]
                    if tc_[0] == '0': # убираем первый нуль
                        tc_ = tc_[1:]
                    print('\n', *tc_, ss_d(ssn),sep='')



# gdz(input('ЧИСЛО:').upper(), int(input("из: ")), int(input("в: ")))  # int(input('ИЗ: ')), int(input('В:')))


def go():
    ss = input("ИЗ В: ").split()
    if len(ss) != 2:
        print("     ТОЛЬКО ДВА ЗНАЧЕНИЯ\n     через пробел")
        go()
    if not ((''.join(ss)).isdigit()):  # пока не учёл возможность
        print("     СС ТОЛЬКО ИЗ ЧИСЕЛ")
        go()
    ss0, ss1 = int(ss[0]), int(ss[1])
    if (ss0 > 36 or ss0 <= 1) or (ss1 > 36 or ss1 <= 1):
        print("    такой сс пока ещё не придумали")
        go()
    if ss[0] == ss[1]:
        print("     В ЭТОМ НЕТ СМЫСЛА")
        go()

    int_n = input("число: ").upper().strip()  # int_n -> str   int имеет вид '1F2'
    # время для проверки
    if len(int_n) == 0:
        print("     а про число забыли?")
        go()
    for i in int_n:
        if i not in "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            print("ЧИСЛО МОЖЕТ СОСТОЯТЬ ТОЛЬКО ИЗ ГРЕЧЕСКОГО АЛФАВИТА И ЧИСЕЛ после еденицы")
            go()
    n = '|'.join(list(int_n))  # n имеет вид '1|F|2
    for i in range(10, 36):  # разшифровка из ABC в 10, 11 и 12
        n = n.replace(abc26[i - 10], str(i))
    n = n.split('|')  # n имеет вид ['1', '15', '2']
    for i in n:
        if int(i) >= int(ss[0]):
            print(f"В ПОСЛЕДОВАТЕЛЬНОСТИ НАЙДЕНЫ ЧИЛА НЕ ПРИСУСТВУЮЩИЕ В {ss[0]}-ичной системе")
            go()
    # ss -> list[str, str]     int_n -> str
    # когда мы убедились, что с входящими данными всё ок переходим к основной части
    #os.system('clear') # for android
    print(_10_n(_n_10(int_n, ss0), ss1))
    print("РЕШЕНИЕ ~")
    gdz(int_n.upper(), int(ss0), int(ss1))


while True:
    go()
    #input('нажми энтр')  # for android
    #os.system('clear')  # for android
    # input('нажми энтр')  # для мобильных устройств
    # os.system('clear')  # для мобильных устройств
