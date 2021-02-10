#https://www.hackerrank.com/challenges/python-print/problem

if __name__ == '__main__':
    n = int(input())
    contador = 0
    for i in range(n):
        i += 1
        contador -= contador
        # print(str(i))
        print(str(i), end='')