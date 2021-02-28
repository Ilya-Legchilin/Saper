from tkinter import *
from PIL import ImageTk
import random
from tkinter import messagebox as mb
import winsound


root = Tk()
root['bg'] = '#C0C0C0'
#root.iconbitmap('pic.ico')
root.geometry('172x218')
root.title('')

mainmenu = Menu(root)
root.config(menu=mainmenu)
root.resizable(width=False, height=False)

time_records = ['123 сек', '234 сек', '345 сек']
name_records = ['asd', 'zxc', 'dfg']

cells = [None]*81
game_is_started = 0
waiting_for_smile = 0
lost = 0
win = 0
number_of_opened_cells = 0
now = 0


bomb_image = ImageTk.PhotoImage(file="bomb.png")
opened_image = ImageTk.PhotoImage(file="opened.bmp")
one_image = ImageTk.PhotoImage(file="one.bmp")
two_image = ImageTk.PhotoImage(file="two.bmp")
three_image = ImageTk.PhotoImage(file="three.bmp")
four_image = ImageTk.PhotoImage(file="four.bmp")
five_image = ImageTk.PhotoImage(file="five.bmp")
six_image = ImageTk.PhotoImage(file="six.bmp")
seven_image = ImageTk.PhotoImage(file="seven.bmp")
eight_image = ImageTk.PhotoImage(file="eight.bmp")

dead_smile = ImageTk.PhotoImage(file="dead_smile.png")
glasses_smile = ImageTk.PhotoImage(file="glasses.png")

def generate_bombs():
    a = [None]*10
    for i in range(10):
        a[i] = random.randint(0, 80)
    return a


def start_new_game():
    global game_is_started
    game_is_started = 1
    update_timer()


def lose_game():
    global lost
    lost = 1
    for i in range(81):
        open_cell(cells[i])
    global waiting_for_smile
    waiting_for_smile = 1
    #print('game is lost')
    smile_btn.configure(image=dead_smile)
    #answer = mb.showinfo(message="Убит!")
    winsound.PlaySound('mario.wav', winsound.SND_FILENAME)
    

def open_cell(button):
    if button.active:
        button.active = False
        global number_of_opened_cells
        number_of_opened_cells += 1
        if button.mine:
            button.btn.configure(image=bomb_image)
            button.btn['state'] = 'disabled'
            if not lost:
                lose_game()
        else:
            if button.neighbours == 0:
                button.btn['state'] = 'disabled'
                button.btn.configure(image=opened_image)
                i = button.number
                if i == 0:
                    open_cell(cells[1])
                    open_cell(cells[9])
                    open_cell(cells[10])
                elif i == 8:
                    open_cell(cells[7])
                    open_cell(cells[16])
                    open_cell(cells[17])
                elif i == 80:
                    open_cell(cells[79])
                    open_cell(cells[70])
                    open_cell(cells[71])
                elif i == 72:
                    open_cell(cells[63])
                    open_cell(cells[64])
                    open_cell(cells[73])
                elif i > 0 and i < 8:
                    open_cell(cells[i-1])
                    open_cell(cells[i+1])
                    open_cell(cells[i+9])
                    open_cell(cells[i+8])
                    open_cell(cells[i+10])
                elif i > 72 and i < 80:
                    open_cell(cells[i-1])
                    open_cell(cells[i+1])
                    open_cell(cells[i-9])
                    open_cell(cells[i-8])
                    open_cell(cells[i-10])
                elif i % 9 == 0:
                    open_cell(cells[i+1])
                    open_cell(cells[i+9])
                    open_cell(cells[i-9])
                    open_cell(cells[i-8])
                    open_cell(cells[i+10])
                elif (i+1) % 9 == 0:
                    open_cell(cells[i-1])
                    open_cell(cells[i+9])
                    open_cell(cells[i-9])
                    open_cell(cells[i+8])
                    open_cell(cells[i-10])
                else:
                    open_cell(cells[i+1])
                    open_cell(cells[i-1])
                    open_cell(cells[i-9])
                    open_cell(cells[i+9])
                    open_cell(cells[i-10])
                    open_cell(cells[i-8])
                    open_cell(cells[i+10])
                    open_cell(cells[i+8])      
            else:
                button.btn['state'] = 'disabled'
                if button.neighbours == 1:
                    button.btn.configure(image=one_image)
                if button.neighbours == 2:
                    button.btn.configure(image=two_image)
                if button.neighbours == 3:
                    button.btn.configure(image=three_image)
                if button.neighbours == 4:
                    button.btn.configure(image=four_image)
                if button.neighbours == 5:
                    button.btn.configure(image=five_image)
                if button.neighbours == 6:
                    button.btn.configure(image=six_image)
                if button.neighbours == 7:
                    button.btn.configure(image=seven_image)
                if button.neighbours == 8:
                    button.btn.configure(image=seven_image)
            if number_of_opened_cells == 71 and not lost:
                #print('MUSIC')
                global win
                win = 1
                global waiting_for_smile
                waiting_for_smile = 1
                smile_btn.configure(image=glasses_smile)
                answer = mb.showinfo(message="Победа!")
                root.after(3000, quit_game)
                winsound.PlaySound('music.wav', winsound.SND_FILENAME)
                
            


def field_click(event, button):
    if game_is_started:
        if button.active:
            open_cell(button)
    else:
        start_new_game()
        if button.active:
            open_cell(button)


def change_to_beginner():
    pass


def change_to_amateur():
    pass


def change_to_professional():
    pass


def open_special():
    pass


def open_tags():
    pass


def color_settings():
    pass


def sound_settings():
    pass


def list_of_champions():
    window_champions = Toplevel(root)
    window_champions.geometry('250x130')
    window_champions['bg'] ='#F0F0F0'
    window_champions.title('Чемпионы')
    window_champions.focus_force()
    window_champions.resizable(width=False, height=False)
    
    frame1 = Frame(window_champions)
    frame1.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.12)
    
    frame2 = Frame(window_champions)
    frame2.place(relx=0.05, rely=0.35, relwidth=0.9, relheight=0.12)
    
    frame3 = Frame(window_champions)
    frame3.place(relx=0.05, rely=0.5, relwidth=0.9, relheight=0.12)
    
    l1 = Label(frame1, text="Новичок:            ")
    l2 = Label(frame2, text="Любитель:          ")
    l3 = Label(frame3, text="Профессионал: ")
    l1.pack(side=LEFT)
    l2.pack(side=LEFT)
    l3.pack(side=LEFT)
    
    time1 = Label(frame1, text=time_records[0])
    time2 = Label(frame2, text=time_records[1])
    time3 = Label(frame3, text=time_records[2])
    time1.pack(side=LEFT)
    time2.pack(side=LEFT)
    time3.pack(side=LEFT)
    
    name1 = Label(frame1, text=name_records[0])
    name2 = Label(frame2, text=name_records[1])
    name3 = Label(frame3, text=name_records[2])
    name1.pack(side=RIGHT)
    name2.pack(side=RIGHT)
    name3.pack(side=RIGHT)
    
    def reset_results():

        time_records = ['999 сек', '999 сек', '999 сек']
        name_records = ['Аноним', 'Аноним', 'Аноним']
        
        name1.configure(text=name_records[0])
        name2.configure(text=name_records[1])
        name3.configure(text=name_records[2])
        
        time1.configure(text=time_records[0])
        time2.configure(text=time_records[1])
        time3.configure(text=time_records[2])
        
    
    frame_bottom = Frame(window_champions)
    frame_bottom.place(relx=0.15, rely=0.7, relwidth=0.9, relheight=0.15)
    
    reset_btn = Button(frame_bottom, text='Cброс результатов', width=15, height=3, command=reset_results)
    reset_btn.pack(side=LEFT)
    
    ok_btn = Button(frame_bottom, text='OК', width=5, height=3, command=window_champions.destroy)
    ok_btn.pack()
    
    
def quit_game():
    root.destroy()
    
    
def smile_clicked(event):
    print('smile clicked, waiting_for_smile ', waiting_for_smile)
    if waiting_for_smile:
        quit_game()
    
    
gamemenu = Menu(mainmenu, tearoff=0)
helpmenu = Menu(mainmenu, tearoff=0)

gamemenu.add_command(label="Новая игра                  F2", command=start_new_game)
gamemenu.add_separator()
gamemenu.add_command(label="Новичок", command=change_to_beginner)
gamemenu.add_command(label="Любитель", command=change_to_amateur)
gamemenu.add_command(label="Профессионал", command=change_to_professional)
gamemenu.add_command(label="Особые...", command=open_special)
gamemenu.add_separator()
gamemenu.add_command(label="Метки (?)", command=open_tags)
gamemenu.add_command(label="Цвет", command=color_settings)
gamemenu.add_command(label="Звук", command=sound_settings)
gamemenu.add_separator()
gamemenu.add_command(label="Чемпионы...", command=list_of_champions)
gamemenu.add_separator()
gamemenu.add_command(label="Выход", command=quit_game)

helpmenu.add_command(label="Вызов справки                   F1")
helpmenu.add_command(label="Предметный указатель...")
helpmenu.add_command(label="Пользование справкой")
helpmenu.add_separator()
helpmenu.add_command(label="О программе")

mainmenu.add_cascade(label="Игра",
                     menu=gamemenu)
mainmenu.add_cascade(label='Справка', menu=helpmenu)

frame_top = Frame(root)
frame_top.place(relwidth=1, relheight=0.17)
mines_counter = LabelFrame(frame_top)
mines_counter.pack(side=LEFT, padx=5, pady=5)
l1 = Label(mines_counter, text='010', font=("Magneto", "18"))
l1.pack()

timer = LabelFrame(frame_top)
timer.pack(side=RIGHT, padx=5, pady=5)
l2 = Label(timer, text='000', font=("Magneto", "18"))
l2.pack(side=RIGHT)


def update_timer():
    winsound.Beep(500, 100)
    global now 
    now += 1
    if now < 10:
        text = '00' + str(now)
    elif now < 100:
        text = '0' + str(now)
    elif now < 1000:
        text = str(now)
    else:
        text = '0'
        now = 0
    l2.configure(text=text)
    if not lost and not win:
        l2.after(1000, update_timer)
    

image = ImageTk.PhotoImage(file="smile.png")
smile_btn = Button(frame_top, image=image)
smile_btn.pack()
smile_btn.bind('<Button-1>', smile_clicked)

square_image =ImageTk.PhotoImage(file="square.png")

fields = [None]*9
h = 0.17


class Cell():
    def __init__(self, number, btn, mine):
        self.number = number
        self.btn = btn
        self.flag = False
        self.mine = mine
        self.neighbours = 0
        self.active = True
        
    def __str__(self):
        text = "Кнопка номер " + str(self.number)
        return text
        
      
j = 0

list_of_bombs = generate_bombs()
for i in range(9):
    fields[i] = Frame(root)
    fields[i].place(rely=h, relwidth=1, relheight=0.1)
    h = h + 0.092
    for k in range(9):
        if j in list_of_bombs:
            b = 1
        else:
            b = 0
        temp = Cell(j, Button(fields[i], image=square_image), b)
        temp.btn.pack(side=LEFT)
        cells[j] = temp
        j += 1


flag_image =ImageTk.PhotoImage(file="flag.jpg")


def set_flag(event, button):
    if button.active:
        if button.flag:
            button.flag = False
            button.btn.configure(image=square_image)
        else:
            button.flag = True
            button.btn.configure(image=flag_image)


for i in range(81):
    but = cells[i]
    but.btn.bind('<Button-1>', field_click)
    but.btn.bind('<Button-3>', lambda e, but=but: set_flag(e, but))
    count_of_bombs = 0
    if i == 0:
        count_of_bombs = cells[1].mine + cells[9].mine + cells[10].mine
    elif i == 8:
        count_of_bombs = cells[7].mine + cells[16].mine + cells[17].mine
    elif i == 80:
        count_of_bombs = cells[79].mine + cells[70].mine + cells[71].mine
    elif i == 72:
        count_of_bombs = cells[73].mine + cells[63].mine + cells[64].mine
    elif i > 0 and i < 8:
        count_of_bombs = cells[i-1].mine + cells[i+1].mine + cells[i+9].mine + \
        cells[i+8].mine + cells[i+10].mine
    elif i > 72 and i < 80:
        count_of_bombs = cells[i-1].mine + cells[i+1].mine + cells[i-9].mine + \
        cells[i-10].mine + cells[i-8].mine
    elif i % 9 == 0:
        count_of_bombs = cells[i+1].mine + cells[i-9].mine + cells[i+9].mine + \
        cells[i-8].mine + cells[i+10].mine
    elif (i+1) % 9 == 0:
        count_of_bombs = cells[i-1].mine + cells[i-9].mine + cells[i+9].mine + \
        cells[i-10].mine + cells[i+8].mine
    else:
        count_of_bombs = cells[i-1].mine + cells[i+1].mine + cells[i-9].mine + \
        + cells[i-8].mine + + cells[i-10].mine + cells[i+9].mine + cells[i+10].mine + cells[i+8].mine
    cells[i].neighbours = count_of_bombs
    
    but.btn.bind('<Button-1>', lambda e, but=but: field_click(e, but))
    but.btn.bind('<Button-3>', lambda e, but=but: set_flag(e, but))   


root.mainloop()