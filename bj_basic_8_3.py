#3

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

a = input()
ret = 0

for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            ret += dial.index(i) + 3


#4

cro_str = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

a = input()

for i in cro_str:
    a = a.replace(i, '*')

print(len(a))


# 5

w_num = int(input())

group_word = 0

for i in range(w_num):  # 한번 등장했던 문자가 두번 등장하는 수를 알아내는 방법
    word = input()
    error = 0
    for index in range(len(word) - 1):
        if word[index] != word[index + 1]:
            new_word = word[index + 1:]
            if new_word.count(word[index]) > 0:
                error += 1

    if error == 0:
        group_word += 1

print(group_word)



