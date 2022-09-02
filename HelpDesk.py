from socket import gethostname, gethostbyname
from os import environ
from psutil import cpu_percent, virtual_memory, disk_usage
import tkinter as tk
import pyautogui
import yaml


with open("configs/config.yml", "r", encoding="utf-8") as file_descriptor:
    config = yaml.load(file_descriptor, Loader=yaml.Loader)

app_window_width = config["window_width"]
app_window_height = config["window_height"]
app_pos_x = config["app_x_pos"]
app_pos_y = config["app_y_pos"]

screen_number = config['screen_number']

h_title = config['h_title']
h_l_title = config['h_l_title']
h_lbl1 = config['h_lbl1']
h_lbl1_number = config['h_lbl1_number']
h_lbl2 = config['h_lbl2']
h_lbl2_number = config['h_lbl2_number']
h_lbl3 = config['h_lbl3']
h_lbl3_number = config['h_lbl3_number']
h_l_title2 = config['h_l_title2']
h_lbl4 = config['h_lbl4']
h_lbl4_number = config['h_lbl4_number']

print(app_window_width, app_window_height,app_pos_x,app_pos_y,screen_number,
      h_title,h_l_title,h_lbl1,h_lbl1_number,h_lbl2,h_lbl2_number,h_lbl3,
      h_lbl3_number,h_l_title2,h_lbl4,h_lbl4_number, sep='\n')
n = 1
default_var = None


def get_sys_load():
    lbl1.config(text=f"IP-адрес: {gethostbyname(gethostname())}")
    lbl2.config(text=f"Имя компьютера: {gethostname()}")
    lbl3.config(text=f"Имя пользователя: {environ.get('USERNAME')}")
    lbl4.config(text=f"Загрузка ЦП: {cpu_percent()}")
    lbl5.config(text=f"Загрузка памяти: {virtual_memory()[2]}")
    lbl6.config(text=f"Загрузка Диска C: {disk_usage('C:')[3]}")
    app.after(500, get_sys_load)


def shot():
    global n
    screen = pyautogui.screenshot(rf"C:\Users\{environ.get('USERNAME')}\Documents\screen_{n}.png")
    screen_label.config(text=f"Скриншот {n} сохранен в папке Документы")
    n += 1


app = tk.Tk()
app.geometry(f'{app_window_width}x{app_window_height}+{app_pos_x}+{app_pos_y}')
app.title('HelpDesk v.0.0.2')
app.configure(background='gray')
app.attributes('-alpha', 0.8)
app.lift()
app.attributes('-topmost',True)
app.after_idle(app.attributes,'-topmost',True)
app.iconbitmap('help.ico')

app.after(500, get_sys_load)

lbl1 = tk.Label(app, text=f"IP-адрес: {default_var}", font=('Helvetica', 12), fg='#88e400', background='gray')
lbl2 = tk.Label(app, text=f"Имя компьютера: {default_var}", font=('Helvetica', 12), fg='#88e400', background='gray')
lbl3 = tk.Label(app, text=f"Имя пользователя: {default_var}", font=('Helvetica', 12), fg='#88e400', background='gray')
lbl4 = tk.Label(app, text=f"Загрузка ЦП: {default_var}", font=('Helvetica', 12), fg='#88e400', background='gray')
lbl5 = tk.Label(app, text=f"Загрузка памяти: {default_var}", font=('Helvetica', 12), fg='#88e400', background='gray')
lbl6 = tk.Label(app, text=f"Загрузка Диска C: {default_var}", font=('Helvetica', 12), fg='#88e400', background='gray')
lbl1.pack()
lbl2.pack()
lbl3.pack()
lbl4.pack()
lbl5.pack()
lbl6.pack()

screen_button = tk.Button(app, text='Сделать скриншот!', font=('Courier', 10), fg='#7cd000', background='#5d5d5d', command=shot)
screen_button.pack(pady=10)

screen_label = tk.Label(app, text="", fg='#7cd000', background='#5d5d5d')
screen_label.pack()

help_lbl = tk.Label(app, text="Техподдержка", font=('Helvetica', 14), fg='#7cd000', background='gray')
help_lbl1 = tk.Label(app, text="По вопросам 1С:\nРоман\t#959\nАндрей\t#953\nМихаил\t#954", font=('Helvetica', 11), fg='#7cd000', background='gray')
help_lbl2 = tk.Label(app, text="Системный администратор:\nДмитрий\t#950", font=('Helvetica', 11), fg='#7cd000', background='gray')
help_lbl.pack(pady=5)
help_lbl1.pack()
help_lbl2.pack()

app.mainloop()
