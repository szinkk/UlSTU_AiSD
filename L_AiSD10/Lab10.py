import random
from tkinter import *
from tkinter import ttk


def dismiss(win):
    win.grab_release()
    win.destroy()


class TicTacToe:
    def __init__(self, main):
        self.count = 0
        self.turn = None
        self.flag = None
        self.free = None
        self.main = main
        self.account = {}
        self.moves = None
        self.buttons = None
        self.next_move = None
        self.first_click = True
        self.first_move = None

        self.games()

    def games(self):

        self.turn = 1
        self.flag = False
        self.moves = [None] * 9
        self.free = list(range(9))

        for widget in self.main.winfo_children():
            widget.destroy()

        self.main.title("Крестики Нолики")
        self.main.geometry("480x240+300+200")
        self.main.resizable(False, False)

        start_label = Label(self.main, text="Добро пожаловать в игру Крестики Нолики\n"
                                            "Вы хотите ходить первым или вторым")
        button_first = ttk.Button(self.main, text="Первым",  command=lambda: choice("1"))
        button_after = ttk.Button(self.main, text="Вторым", command=lambda: choice("2"))

        start_label.place(x=125, y=50)
        button_first.place(x=80, y=120)
        button_after.place(x=320, y=120)

        self.buttons = [Button(self.main, width=3, height=1, font="Arial 40 bold",
                               command=lambda x=i: push(x)) for i in range(9)]

        def choice(gamer):
            if gamer == "1":
                self.first_move = True
            else:
                self.first_move = False

            self.main.geometry("310x320+550+45")

            row = 1
            col = 0
            for i in range(9):
                self.buttons[i].grid(row=row, column=col)
                col += 1
                if col == 3:
                    row += 1
                    col = 0

            if not self.first_move:
                self.next_move = random.choice((0, 2, 6, 8))
                self.moves[self.next_move] = "O"
                self.buttons[self.next_move].config(text="O", state="disabled")
                self.free.remove(self.next_move)

        def results(result):
            window = Toplevel()
            window.geometry("240x240+660+320")
            window.grab_set()
            if result == 1:
                Label(window, text="Вы выиграли", font="Arial 20").place(x=35, y=50)
                ttk.Button(window, text="Заново", command=lambda: self.games()).place(x=85, y=120)
            elif result == -1:
                Label(window, text="Вы проиграли", font="Arial 20").place(x=30, y=50)
                ttk.Button(window, text="Заново", command=lambda: self.games()).place(x=85, y=120)
            else:
                Label(window, text="Ничья", font="Arial 20").place(x=80, y=50)
                ttk.Button(window, text="Заново", command=lambda: self.games()).place(x=85, y=120)

        def motion(x, number):
            flag = True
            next_move = -1
            # Строки
            for i in range(0, 9, 3):
                if self.moves[i] == x and self.moves[i + 1] == x and self.moves[i + 2] is None:
                    next_move = i + 2
                elif self.moves[i] == x and self.moves[i + 2] == x and self.moves[i + 1] is None:
                    next_move = i + 1
                elif self.moves[i + 1] == x and self.moves[i + 2] == x and self.moves[i] is None:
                    next_move = i
            # Столбцы
            for i in range(3):
                if self.moves[i] == x and self.moves[i + 3] == x and self.moves[i + 6] is None:
                    next_move = i + 6
                elif self.moves[i] == x and self.moves[i + 6] == x and self.moves[i + 3] is None:
                    next_move = i + 3
                elif self.moves[i + 3] == x and self.moves[i + 6] == x and self.moves[i] is None:
                    next_move = i
            # Главная диагональ
            if self.moves[0] == x and self.moves[4] == x and self.moves[8] is None:
                next_move = 8
            if self.moves[0] == x and self.moves[8] == x and self.moves[4] is None:
                next_move = 4
            if self.moves[4] == x and self.moves[8] == x and self.moves[0] is None:
                next_move = 0
            # Побочная диагональ
            if self.moves[2] == x and self.moves[4] == x and self.moves[6] is None:
                next_move = 6
            if self.moves[2] == x and self.moves[6] == x and self.moves[4] is None:
                next_move = 4
            if self.moves[4] == x and self.moves[6] == x and self.moves[2] is None:
                next_move = 2

            if next_move == -1:
                next_move = 8 - number
                flag = False
            return next_move, flag

        def win(x):
            if (self.moves[0] == x and self.moves[1] == x and self.moves[2] == x) or \
                    (self.moves[3] == x and self.moves[4] == x and self.moves[5] == x) or \
                    (self.moves[6] == x and self.moves[7] == x and self.moves[8] == x) or \
                    (self.moves[0] == x and self.moves[3] == x and self.moves[6] == x) or \
                    (self.moves[1] == x and self.moves[4] == x and self.moves[7] == x) or \
                    (self.moves[2] == x and self.moves[5] == x and self.moves[8] == x) or \
                    (self.moves[0] == x and self.moves[4] == x and self.moves[8] == x) or \
                    (self.moves[2] == x and self.moves[4] == x and self.moves[6] == x):
                return True

        def next_step(number):
            x, flag = motion("O", number)
            if flag:
                self.next_move = x
            else:
                self.next_move = motion("X", number)[0]

        def push(number):
            self.moves[number] = "X"
            self.buttons[number].config(text="X", state="disabled")
            self.free.remove(number)

            # Первый ход
            if self.turn == 1:
                if number == 4:
                    if self.first_move:
                        self.next_move = random.choice((0, 2, 6, 8))
                    else:
                        self.next_move = 8 - self.next_move

                else:
                    if self.first_move and number % 2 == 0:
                        self.next_move = 4
                    else:
                        self.next_move = random.choice((0, 2, 6, 8))
            # Второй ход
            elif self.turn == 2:
                if self.first_move and self.moves[4] != "X":
                    corners = [i for i in range(9) if self.moves[i] == "X"]
                    if abs(corners[0] - corners[1]) == 8 or abs(corners[0] - corners[1]) == 4:
                        self.next_move = random.choice((1, 3, 5, 7))
                    else:
                        next_step(number)
                else:
                    next_step(number)
            # Третий ход
            elif self.turn == 3:
                # Бот продолжение трёх углов
                if not self.first_move:
                    if not motion("O", number)[1] and not motion("X", number)[1]:
                        try:
                            self.next_move = random.choice([x for x in self.free if x != 4 and x % 2 == 0])
                        except IndexError:
                            x, flag = motion("O", number)
                            if flag:
                                self.next_move = x
                    else:
                        next_step(number)
                else:
                    next_step(number)
            # Четвёртый и пятый ход
            else:
                next_step(number)
            # Если клетка для нолика занята
            if self.next_move not in self.free:
                try:
                    corners = [x for x in self.free if x != 4 and x % 2 == 0]
                    if len(corners) > 0:
                        self.next_move = random.choice(corners)
                    else:
                        self.next_move = random.choice(self.free)
                except IndexError:
                    pass

            self.moves[self.next_move] = "O"
            self.buttons[self.next_move].config(text="O", state="disabled")

            if win("X"):
                self.result = 1
                results(self.result)
            elif win("O"):
                self.result = -1
                results(self.result)
            else:
                if len(self.free) > 1:
                    self.free.remove(self.next_move)
                else:
                    self.result = 0
                    results(self.result)
                self.turn += 1


root = Tk()
TicTacToe(root)
root.mainloop()
