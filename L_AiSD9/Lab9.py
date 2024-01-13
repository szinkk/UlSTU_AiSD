import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def open_file():
    try:
        text = open(r"checkers_user_file.txt", "r+")
        return text
    except FileNotFoundError:
        text = open(r"checkers_user_file.txt", "w")
        text.close()
        text = open(r"checkers_user_file.txt", "r+")
        return text


def dismiss(win):
    win.grab_release()
    win.destroy()


class AuthorizationWindow:
    def __init__(self, main):
        self.first_click = True
        self.main = main
        self.users = {}
        self.hide_flag = True

        button_style = ttk.Style()
        button_style.configure("my.TButton", font="Arial 12")

        self.label = Label(text="Для игры введите ваш логин и пароль", font="Arial 15 bold")
        self.label_login = Label(text="Логин", font="Arial 15")
        self.label_password = Label(text="Пароль", font="Arial 15")
        self.entry_login = ttk.Entry(width=30, justify="center")
        self.entry_password = ttk.Entry(width=30, justify="center", show="*")
        self.button_auth = ttk.Button(text="Авторизироваться", style="my.TButton", command=lambda: self.authorization())
        self.button_reg = ttk.Button(text="Зарегистрироваться", style="my.TButton", command=lambda: self.registrate())
        self.button_hide = ttk.Button(text="-", command=lambda: self.hide_password(self.entry_password, self.button_hide))

        self.label.place(x=350, y=25)
        self.label_login.place(x=500, y=55)
        self.entry_login.place(x=435, y=85)
        self.label_password.place(x=495, y=105)
        self.entry_password.place(x=435, y=135)
        self.button_hide.place(x=602, y=135, width=20, height=20)
        self.button_auth.place(x=440, y=165, width=180)
        self.button_reg.place(x=440, y=195, width=180)

    def hide_password(self, password_mask, hide_text):
        if self.hide_flag:
            password_mask.config(show="")
            hide_text.config(text="*")
        else:
            password_mask.config(show="*")
            hide_text.config(text="-")
        self.hide_flag = not self.hide_flag

    def authorization(self):
        login = self.entry_login.get()
        password = self.entry_password.get()

        if len(login) == 0 and len(password) == 0:
            messagebox.showwarning(title="Ошибка", message="Введите логин и пароль")

        elif len(login) == 0 and len(password) != 0:
            messagebox.showwarning(title="Ошибка", message="Введите логин")

        elif len(login) != 0 and len(password) == 0:
            messagebox.showwarning(title="Ошибка", message="Введите пароль")

        else:
            file = open_file()
            a = file.readline()[:-1].split(" ")

            while True:
                if a != [""]:
                    self.users[a[0]] = a[1]
                    a = file.readline()[:-1].split(" ")
                else:
                    break

            flag_reg = False
            flag_password = True
            for i in self.users.items():
                login_check, password_check = i
                if login == login_check and password == password_check:
                    flag_reg = True
                    break
                elif login == login_check and password != password:
                    flag_password = False

            if flag_reg:
                for widget in self.main.winfo_children():
                    widget.destroy()

                Label(self.main, text="Вы успешно авторизовались!", font="Arial 16 bold").place(x=375, y=160)
                button = ttk.Button(self.main, text="Играть", style="my.TButton", command=self.drawing)
                button.place(x=490, y=340)

            elif not flag_password:
                messagebox.showwarning(title="Ошибка", message="Неверный пароль")
            else:
                messagebox.showwarning(title="Ошибка", message="Такого аккаунта не существует")

    def registrate(self):
        reg_window = Toplevel()
        reg_window.title("Регистрация")
        reg_window.geometry("1080x520-90-95")
        reg_window.resizable(False, False)
        reg_window.protocol("WM_DELETE_WINDOW", lambda: dismiss(reg_window))
        reg_window.grab_set()

        label = Label(reg_window, text="Для регистрации введите ваш логин и пароль", font="Arial 15 bold")
        label_login = Label(reg_window, text="Логин", font="Arial 15")
        label_password = Label(reg_window, text="Пароль", font="Arial 15")
        entry_login = ttk.Entry(reg_window, width=30, justify="center")
        entry_password = ttk.Entry(reg_window, width=30, justify="center", show="*")
        button_reg = ttk.Button(reg_window, text="Зарегистрироваться", style="my.TButton", command=lambda: registr())
        button_hide = ttk.Button(reg_window, text="-", command=lambda: self.hide_password(entry_password, button_hide))

        label.place(x=350, y=25)
        label_login.place(x=500, y=55)
        entry_login.place(x=435, y=85)
        label_password.place(x=495, y=105)
        entry_password.place(x=435, y=135)
        button_hide.place(x=602, y=135, width=20, height=20)
        button_reg.place(x=440, y=165, width=180)

        def registr():
            login = entry_login.get()
            password = entry_password.get()

            if len(login) == 0 and len(password) == 0:
                messagebox.showwarning(title="Ошибка", message="Введите логин и пароль")

            elif len(login) == 0 and len(password) != 0:
                messagebox.showwarning(title="Ошибка", message="Введите логин")

            elif len(login) != 0 and len(password) == 0:
                messagebox.showwarning(title="Ошибка", message="Введите пароль")

            else:
                file = open_file()
                temp = file.readline()[:-1].split(" ")

                while True:
                    if temp != [""]:
                        self.users[temp[0]] = temp[1]
                        temp = file.readline()[:-1].split(" ")
                    else:
                        break

                flag_reg = False

                for i in self.users.items():
                    l, p = i
                    if login == l:
                        flag_reg = True

                if not flag_reg:
                    file = open_file()
                    file.seek(0, os.SEEK_END)
                    file.write(f'{login} {password}\n')
                    file.close()

                    for widget in reg_window.winfo_children():
                        widget.destroy()

                    Label(reg_window, text=f"Вы успешно зарегистрировались\nВаш логин: {login}\nВаш пароль: {password}",
                          font="Arial 15 ").place(x=370, y=150)
                    reg_window.after(3000, lambda: (reg_window.destroy(), reg_window.grab_release()))
                else:
                    messagebox.showwarning(title="Ошибка", message="Такой аккаунт уже существует")

    def drawing(self):
        self.main.title("80-Поддавки")
        self.main.geometry("800x640+100+100")

        cell_sz = 80
        row = 8
        col = 10

        deck = Canvas(self.main, width=cell_sz * col, height=cell_sz * row)
        cell_colors = ["#FFDDBB", "#552B00"]
        color_index = 0

        for rows in range(row):
            for cols in range(col):
                x1, y1 = cols * cell_sz, rows * cell_sz
                x2, y2 = cols * cell_sz + cell_sz, rows * cell_sz + cell_sz
                deck.create_rectangle(x1, y1, x2, y2, fill=cell_colors[color_index])
                color_index = not color_index
            color_index = not color_index

        deck.pack()


root = Tk()
root.title("Авторизация")
root.geometry("1080x520-100-100")
root.resizable(False, False)

AuthorizationWindow(root)

root.mainloop()
