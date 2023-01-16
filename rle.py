# переделал вывод из строки в список тьюплов потому что может возникнуть
#  путаница c декодированием например ряда одинадцати едениц
# ( это ещё ладно, на нормализации можно выехать), и идущей сразу за ней
#  одной двойки.

def zip(inc:str) -> list:    
    out = []
    tmp = 1
    for i in range(len(inc)):
        try:
            if inc[i+1] == inc[i]:
                tmp += 1
            else:
                out.append((tmp,f'{inc[i]}'))
                tmp = 1
        except IndexError:
            out.append((tmp,f'{inc[i]}'))

    return out


def extract(inc: list) -> str:
    out, to_int = "", ""
    tmp = 1
    for i in inc:
        out += i[0]*i[1]
    return out


test_cases = [
    ["111112222334445", [(5,"1"),(4,"2"),(2,"3"),(3,"4"),(1,"5")]],
    ["AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE", [(6,"A"),(1,"F"),(2,"D"),(7,"C"),
    (1,"A"),(17,"E")]],
    ["AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEEq", [(6,"A"),(1,"F"),(2,"D"),(7,"C"),
    (1,"A"), (17,"E"), (1, "q")]],
    ['123',[(1,'1'),(1,'2'),(1,'3')]],
    ['qt3',[(1,'q'),(1,'t'),(1,'3')]]
]


def main():
    for i in test_cases:
        assert zip(i[0]) == i[1]
        assert extract(zip(i[0])) == i[0]

        
if __name__ == "__main__":
    main()