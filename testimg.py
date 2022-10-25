#a와 b를 비교해서 늘어난 훼손 내용을 확인하는 함수 -> 추가된 내역만 리스트로 반환
def check(a, b):
    a.sort()
    b.sort()
    c = b
    for i in range(len(a)):
        if a[i] in b:
            c.remove(a[i])
    return c

#추가된 훼손 내용과 횟수를 확인하는 함수
def ncheck(c):
    d = []
    for i in range(len(b)):
        if b[i] not in d:
            d.append(b[i])
        else:
            continue
    for j in range(len(d)):
        print('%s가 %d회 감지되었습니다.' % (b[j], b.count(b[j])))

a = ['notch', 'spot', 'wornout', 'wornout']
b = ['notch', 'notch', 'spot', 'wornout', 'wornout', 'wornout', 'wornout']

if (a is None) or (b is None):
    print('정보가 없습니다.')
else:
    if len(a) == len(b):
        print('정상입니다. 반납해주세요.')
    elif len(a) < len(b):
        dams = check(a, b)
        ncheck(dams)
        print('창구를 확인해주세요.')
    else:
        print('오류입니다. 직원을 불러주세요.')