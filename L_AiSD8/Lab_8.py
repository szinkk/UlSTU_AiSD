# Животные делятся на спокойных и буйных. Буйные могут стоять только через одну клетку или больше.
# У животных есть рейтинг впечатлений. Найти такое расположение клеток, чтобы животные с максимальным рейтингом
# стояли ближе к началу.
# Требуется для свого варианта второй части л.р. №6 написать объектно-ориентированную реализацию


from itertools import permutations
import random as r
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class Zoopark:

    def __init__(self, main):
        self.first_click = True

        self.main = main
        self.main_label = Label(main, text="\nЖивотные делятся на спокойных и буйных.\nБуйные могут стоять только "
                                           "через одну клетку или "
                                           "больше.\nУ животных есть рейтинг впечатлений. Найти такое расположение "
                                           "клеток,\nчтобы животные "
                                           "стояли в "
                                           "порядке убывания рейтинга впечатлений.")

        self.label = Label(text="\nВведите кол-во животных в зоопарке:")
        self.entry = ttk.Entry(width=30, justify='center')

        self.main_button = ttk.Button(text='Вывести', command=self.result)

        self.main_label.pack()
        self.label.pack()
        self.entry.pack()
        self.main_button.pack(expand=True)

    def result(self):
        self.cells = []
        self.output = []
        self.personality = ["Буйный", "Спокойный"]
        self.permutation = []
        self.flag_warning = True

        try:
            self.k = int(self.entry.get())

            if self.k < 1:
                messagebox.showwarning(title='Ошибка', message='Введите натуральное число.')
                self.flag_warning = False

            if self.flag_warning:
                self.cells_permutations()

                if self.first_click:
                    self.result_window()
                    self.first_click = False
                else:
                    self.output_window.destroy()
                    self.result_window()

        except ValueError:
            messagebox.showwarning(title="Ошибка", message="Введите число.")

    def differences(self, x):
        flag = True

        for j in range(len(x) - 2):
            if (x[j][1] == x[j + 1][1] == "Буйный") or (x[j + 1][1] == x[j + 2][1] == "Буйный"):
                flag = False
                break

        if flag:
            self.permutation += [[*x]]

    def cells_permutations(self):

        for i in range(1, self.k + 1):
            if [x[1] for x in self.cells].count("Буйный") < (self.k // 2):
                self.cells.append([r.randint(10, 100), r.choice(self.personality), i])
            else:
                self.cells.append([r.randint(10, 100), "Спокойный", i])

        for i in permutations(self.cells, len(self.cells)):
            self.differences(i)

        if self.permutation:
            for h in max(self.permutation):
                self.output += [h]

    def result_window(self):
        self.output_window = Toplevel()
        self.output_window.title("Вывод")
        self.output_window.geometry('320x480')
        self.output_window.resizable(False, False)

        self.label_zoo_1 = Label(self.output_window, text="Клетки с животными\n Рейтинг | Характер | Клетка")
        self.label_zoo_2 = Label(self.output_window, text="Оптимальное расположение животных в клетке\n Рейтинг | Характер | Клетка")

        self.output_list_1 = Listbox(self.output_window, height=len(self.cells))
        for i in self.cells:
            self.output_list_1.insert('end', i)

        self.output_list_2 = Listbox(self.output_window, height=len(self.output))
        for i in self.output:
            self.output_list_2.insert('end', i)

        self.label_zoo_1.pack()
        self.output_list_1.pack(side="top", fill="both", expand=1)

        self.label_zoo_2.pack()
        self.output_list_2.pack(side="bottom", fill="both", expand=1)


root = Tk()
root.title('Лабораторная № 8')
root.geometry('720x240')
root.resizable(False, False)

Zoopark(root)

root.mainloop()
