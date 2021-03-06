import matplotlib.pyplot as plt
import numpy as np


def ex1():
    """ Make currency dynamics. """
    cy = []
    date = []
    d = 1
    with open("file1.txt") as f:
        for item in f:
            date.append(d)
            item = float(item)
            cy.append(item)
            d += 1
    plt.plot(date, cy)
    plt.xlabel('Дни')
    plt.ylabel('Курс валюты')
    plt.title('Курс валюты США')
    plt.show()


def ex2():
    """ Make multiple currency dynamics. """
    cur1 = []
    cur2 = []
    cur3 = []
    date = []
    d = 1
    with open('file2.txt') as _file:
        for item in _file:
            date.append(d)
            a, b, c = item.split()
            cur1.append(float(a))
            cur2.append(float(b))
            cur3.append(float(c))
            d += 1
    plt.plot(date, cur1, date, cur2, date, cur3)
    plt.xlabel('Дни')
    plt.ylabel('Курс валюты')
    plt.title('Сравнение курса доллара, йены, евро ')
    plt.show()


def ex3():
    """ Improve currency dynamics. """
    cur1 = []
    cur2 = []
    cur3 = []
    date = []
    d = 1
    with open('file2.txt') as f:
        for item in f:
            date.append(d)
            a, b, c = item.split()
            cur1.append(float(a))
            cur2.append(float(b))
            cur3.append(float(c))
            d += 1

    plt.plot(date, cur1, date, cur2, date, cur3)
    plt.xlabel('Дни')
    plt.ylabel('Курс  валюты')
    plt.title('Сравнение курса  валюты доллара, йены, евро')
    plt.grid(True)
    plt.show()


def ex4():
    """ One more improve currency dynamics. """
    cur1 = []
    cur2 = []
    cur3 = []
    date = []
    d = 1
    with open('file2.txt') as f:
        for item in f:
            date.append(d)
            a, b, c = item.split()
            cur1.append(float(a))
            cur2.append(float(b))
            cur3.append(float(c))
            d += 1

    # subplot 1
    plt.subplot(221)
    plt.plot(date, cur1)
    plt.xlabel('Дни')
    plt.ylabel('Курс  валюты')
    plt.title('Курс валюты доллар')
    plt.grid(True)

    # subplot 2
    plt.subplot(222)
    plt.plot(date, cur2, 'g')
    plt.xlabel('Дни')
    plt.ylabel('Курс  валюты')
    plt.title('Курс валюты евро')
    plt.grid(True)

    # subplot 3
    plt.subplot(223)
    plt.plot(date, cur3, 'r')
    plt.xlabel('Дни')
    plt.ylabel('Курс  валюты')
    plt.title('Курс валюты йена')
    plt.grid(True)
    plt.show()


def ex8():
    """ Makes signatures. """
    cur1 = []
    cur2 = []
    cur3 = []
    date = []
    d = 1
    with open('file2.txt') as f:
        for item in f:
            date.append(d)
            a, b, c = item.split()
            cur1.append(float(a))
            cur2.append(float(b))
            cur3.append(float(c))
            d += 1

    # subplot 1
    plt.subplot(221)
    plt.plot(date, cur1, label='Доллар США')
    plt.xlabel('Дни')
    plt.ylabel('Курс  валюты')
    plt.title('Данные ЦБ РФ')
    plt.legend(loc='best')
    plt.grid(True)

    # subplot 2
    plt.subplot(222)
    plt.plot(date, cur2, 'g', label='Евро')
    plt.xlabel('Дни')
    plt.ylabel('Курс  валюты')
    plt.title('Данные ЦБ РФ')
    plt.legend(loc='best')
    plt.grid(True)

    # subplot 3
    plt.subplot(223)
    plt.plot(date, cur3, 'r', label='Йена')
    plt.xlabel('Дни')
    plt.ylabel('Курс  валюты')
    plt.title('Данные ЦБ РФ')
    plt.grid(True)
    plt.legend(loc='best')
    plt.show()


def ex9():
    """ Scatter plot. """
    cur1 = []
    cur2 = []
    cur3 = []
    date = []
    d = 1
    with open('file2.txt') as f:
        for line in f:
            date.append(d)
            a, b, c = line.split()
            cur1.append(float(a))
            cur2.append(float(b))
            cur3.append(float(c))
            d += 1

    # subplot 1
    plt.subplot(221)
    plt.plot(date, cur1)
    plt.xlabel('Дни')
    plt.ylabel('Курс  валюты')
    plt.title('Курс валюты доллар')
    plt.grid(True)

    # subplot 2
    plt.subplot(222)
    plt.plot(date, cur2, color='green', marker='o', linestyle=':')
    plt.xlabel('Дни')
    plt.ylabel('Курс  валюты')
    plt.title('Курс валюты евро')
    plt.grid(True)

    # subplot 3
    plt.subplot(223)
    plt.plot(date, cur3, color='red', marker='D', linestyle='--')
    plt.xlabel('Дни')
    plt.ylabel('Курс  валюты')
    plt.title('Курс валюты йена')
    plt.grid(True)
    plt.show()


def ex11():
    """ Make bar chart. """
    objects = ('янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек')
    y_pos = np.arange(len(objects))

    performance = []
    with open('file3.txt') as _file:
        for line in _file:
            performance.append(float(line))

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Рубли')
    plt.title('Курс доллара за 2018 год')

    plt.show()


def ex12():
    """ Make diagram. """
    data = [1036.4, 1500]
    plt.figure(num=1, figsize=(6, 6))
    plt.axes(aspect=1)
    plt.title('Объем сделок по покупке долларов США \n и евро за рубли на 17.01.2017', size=14)
    plt.pie(data, labels=('Доллары', 'Евро'))
    plt.show()


def main():
    num = int(input('Введите номер задачи: '))
    if num == 1:
        ex1()
    if num == 2:
        ex2()
    if num == 3:
        ex3()
    if num == 4:
        ex4()
    if num == 8:
        ex8()
    if num == 9:
        ex9()
    if num == 11:
        ex11()
    if num == 12:
        ex12()


if __name__ == "__main__":
    main()
