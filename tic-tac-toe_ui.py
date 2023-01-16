"""крестики - нолики

game_over - в случае победного сценария

reset_shortcuts - подфункция, восстанавливает хоткеи при перезапуске партии
( esc)

pressed0..8 - ход игрока. вызывается в случае нажатия клавиши; запрещает
повторное нажатие этой кнопки

pressed_o - ход компьютера.

reset - основная функция перезапуска партии.
"""

__author__ = "anton6733@gmail.com"
__version__ = 0.5

import random
import tkinter

core = tkinter.Tk()
core.title(f'tic-tac-toe {str(__version__)}')
core.minsize(width=300, height=325)
core.maxsize(width=300, height=325)


fg_,bg_="black","white"
buttons = {
    6: tkinter.Button(text='<num 7>?', relief='raised', borderwidth=5,
    foreground=fg_,background=bg_),
    7: tkinter.Button(text='<num 8>?', relief='raised', borderwidth=5,
    foreground=fg_,background=bg_),
    8: tkinter.Button(text='<num 9>?', relief='raised', borderwidth=5,
    foreground=fg_,background=bg_),

    3: tkinter.Button(text='<num 4>?', relief='raised', borderwidth=5,
    foreground=fg_,background=bg_),
    4: tkinter.Button(text='<num 5>?', relief='raised', borderwidth=5,
    foreground=fg_,background=bg_),
    5: tkinter.Button(text='<num 6>?', relief='raised', borderwidth=5,
    foreground=fg_,background=bg_),

    0: tkinter.Button(text='<num 1>?', relief='raised', borderwidth=5,
    foreground=fg_,background=bg_),
    1: tkinter.Button(text='<num 2>?', relief='raised', borderwidth=5,
    foreground=fg_,background=bg_),
    2: tkinter.Button(text='<num 3>?', relief='raised', borderwidth=5,
    foreground=fg_,background=bg_),
    
    9: tkinter.Button(text='reset<Escape>', relief='raised', borderwidth=5,
    foreground=fg_,background=bg_)
}
for i in range(3):
    core.rowconfigure(i, weight=2, minsize=100)
    core.columnconfigure(i, weight=2, minsize=100)
core.columnconfigure(3, weight=1)


def game_over(win:set) -> None:
    """блокируем ввод и выделяем выиграшный узор"""
    buttons[0].unbind('<ButtonRelease-1>')
    buttons[1].unbind('<ButtonRelease-1>')
    buttons[2].unbind('<ButtonRelease-1>')
    buttons[3].unbind('<ButtonRelease-1>')
    buttons[4].unbind('<ButtonRelease-1>')
    buttons[5].unbind('<ButtonRelease-1>')
    buttons[6].unbind('<ButtonRelease-1>')
    buttons[7].unbind('<ButtonRelease-1>')
    buttons[8].unbind('<ButtonRelease-1>')
    buttons[6].unbind_all('7')
    buttons[7].unbind_all('8')
    buttons[8].unbind_all('9')
    buttons[3].unbind_all('4')
    buttons[4].unbind_all('5')
    buttons[5].unbind_all('6')
    buttons[0].unbind_all('1')
    buttons[1].unbind_all('2')
    buttons[2].unbind_all('3')
    for i in win:
        buttons[i].config(background="blue",foreground="white")


def reset_shortcuts():
    buttons[0].bind('<ButtonRelease-1>', pressed0)
    buttons[1].bind('<ButtonRelease-1>', pressed1)
    buttons[2].bind('<ButtonRelease-1>', pressed2)
    buttons[3].bind('<ButtonRelease-1>', pressed3)
    buttons[4].bind('<ButtonRelease-1>', pressed4)
    buttons[5].bind('<ButtonRelease-1>', pressed5)
    buttons[6].bind('<ButtonRelease-1>', pressed6)
    buttons[7].bind('<ButtonRelease-1>', pressed7)
    buttons[8].bind('<ButtonRelease-1>', pressed8)
    buttons[6].bind_all('7', pressed6)
    buttons[7].bind_all('8', pressed7)
    buttons[8].bind_all('9', pressed8)
    buttons[3].bind_all('4', pressed3)
    buttons[4].bind_all('5', pressed4)
    buttons[5].bind_all('6', pressed5)
    buttons[0].bind_all('1', pressed0)
    buttons[1].bind_all('2', pressed1)
    buttons[2].bind_all('3', pressed2)
    buttons[9].bind_all('<Escape>', reset)
    buttons[9].bind('<ButtonRelease-1>', reset)


buttons[0].grid(row=2, column=0, sticky="NSWE")
buttons[1].grid(row=2, column=1, sticky="NSWE")
buttons[2].grid(row=2, column=2, sticky="NSWE")
buttons[3].grid(row=1, column=0, sticky="NSWE")
buttons[4].grid(row=1, column=1, sticky="NSWE")
buttons[5].grid(row=1, column=2, sticky="NSWE")
buttons[6].grid(row=0, column=0, sticky="NSWE")
buttons[7].grid(row=0, column=1, sticky="NSWE")
buttons[8].grid(row=0, column=2, sticky="NSWE")
buttons[9].grid(row=3, column=0, sticky="NSWE", columnspan=3)
core.geometry('300x300')


def pressed0(event) -> None:
    global buttons
    mask = 0
    buttons[mask].unbind_all('<ButtonRelease-1>')
    buttons[mask].unbind_all(f'{mask+1}')
    global possible_steps
    try:
        possible_steps.remove(0)
    except KeyError:
        pass
    buttons[mask].config(text='X')
    x_cases.add(mask)
    if x_cases in win_cases:
        game_over(x_cases)
        return
    for i in win_cases:
        if x_cases.issuperset(i):
            game_over(i)
            return
    
    if possible_steps == set():
        reset_shortcuts()
    else:
        pressed_o()
    
    pass


def pressed1(event) -> None:
    global buttons
    mask = 1
    buttons[mask].unbind_all('<ButtonRelease-1>')
    buttons[mask].unbind_all(f'{mask+1}')
    global possible_steps
    try:
        possible_steps.remove(1)
    except KeyError:
        pass
    buttons[mask].config(text='X')
    if x_cases in win_cases:
        game_over(x_cases)
        return
    for i in win_cases:
        if x_cases.issuperset(i):
            game_over(i)
            return
    x_cases.add(mask)
    
    if possible_steps == set():
        reset_shortcuts()
    else:
        pressed_o()
    
    pass


def pressed2(event) -> None:
    global buttons
    mask = 2
    buttons[mask].unbind_all('<ButtonRelease-1>')
    buttons[mask].unbind_all(f'{mask+1}')
    global possible_steps
    try:
        possible_steps.remove(2)
    except KeyError:
        pass
    buttons[mask].config(text='X')
    x_cases.add(mask)
    if x_cases in win_cases:
        game_over(x_cases)
        return
    for i in win_cases:
        if x_cases.issuperset(i):
            game_over(i)
            return
    
    if possible_steps == set():
        reset_shortcuts()
    else:
        pressed_o()
    return


def pressed3(event) -> None:
    global buttons
    mask = 3
    buttons[mask].unbind_all('<ButtonRelease-1>')
    buttons[mask].unbind_all(f'{mask+1}')
    global possible_steps
    try:
        possible_steps.remove(3)
    except KeyError:
        pass
    buttons[mask].config(text='X')
    x_cases.add(mask)
    if x_cases in win_cases:
        game_over(x_cases)
        return
    for i in win_cases:
        if x_cases.issuperset(i):
            game_over(i)
            return
    if possible_steps == set():
        reset_shortcuts()
    else:
        pressed_o()
    return


def pressed4(event) -> None:
    global buttons
    mask = 4
    buttons[mask].unbind_all('<ButtonRelease-1>')
    buttons[mask].unbind_all(f'{mask+1}')
    global possible_steps
    try:
        possible_steps.remove(4)
    except KeyError:
        pass
    buttons[mask].config(text='X')
    x_cases.add(mask)
    for i in win_cases:
        if x_cases.issuperset(i):
            game_over(i)
            return
    if x_cases in win_cases:
        game_over(x_cases)
        return
    if possible_steps == set():
        reset_shortcuts()
    else:
        pressed_o()
    return


def pressed5(event) -> None:
    global buttons
    mask = 5
    buttons[mask].unbind_all('<ButtonRelease-1>')
    buttons[mask].unbind_all(f'{mask+1}')
    global possible_steps
    try:
        possible_steps.remove(5)
    except KeyError:
        pass
    buttons[mask].config(text='X')
    x_cases.add(mask)
    for i in win_cases:
        if x_cases.issuperset(i):
            game_over(i)
            return
    if x_cases in win_cases:
        game_over(x_cases)
        return
    if possible_steps == set():
        reset_shortcuts()
    else:
        pressed_o()
    return


def pressed6(event) -> None:
    global buttons
    mask = 6
    buttons[mask].unbind_all('<ButtonRelease-1>')
    buttons[mask].unbind_all(f'{mask+1}')
    global possible_steps
    try:
        possible_steps.remove(6)
    except KeyError:
        pass
    buttons[mask].config(text='X')
    x_cases.add(mask)
    for i in win_cases:
        if x_cases.issuperset(i):
            game_over(i)
            return
    if x_cases in win_cases:
        game_over(x_cases)
        return
    if possible_steps == set():
        reset_shortcuts()
    else:
        pressed_o()
    return


def pressed7(event) -> None:
    global buttons,x_cases
    mask = 7
    buttons[mask].unbind_all('<ButtonRelease-1>')
    buttons[mask].unbind_all(f'{mask+1}')
    global possible_steps
    try:
        possible_steps.remove(7)
    except KeyError:
        pass
    buttons[mask].config(text='X')
    x_cases.add(mask)
    if x_cases in win_cases:
        game_over(x_cases)
        return
    for i in win_cases:
        if x_cases.issuperset(i):
            game_over(i)
            return
    if x_cases in win_cases:
        print(x_cases)
    if possible_steps == set():
        reset_shortcuts()
    else:
        pressed_o()
    return


def pressed8(event) -> None:
    global buttons
    mask = 8
    buttons[mask].unbind_all('<ButtonRelease-1>')
    buttons[mask].unbind_all(f'{mask+1}')
    global possible_steps
    try:
        possible_steps.remove(8)
    except KeyError:
        pass
    buttons[mask].config(text='X')
    x_cases.add(mask)
    
    if x_cases in win_cases:
        game_over(x_cases)
    for i in win_cases:
        if x_cases.issuperset(i):
            game_over(i)
            return
    if possible_steps == set():
        reset_shortcuts()
    else:
        pressed_o()
    return

def pressed_o():
    global possible_steps,buttons,o_cases
    q=random.choice(list(possible_steps))
    buttons[q].config(text="O")
    buttons[q].unbind_all('<ButtonRelease-1>')
    buttons[q].unbind_all(f'{q+1}')
    o_cases.add(q)
    if o_cases in win_cases:
        game_over(o_cases)
    for i in win_cases:
        if o_cases.issuperset(i):
            game_over(i)
    possible_steps.remove(q)


def reset(event) -> None:
    global possible_steps,x_cases,o_cases
    x_cases,o_cases=set(),set()
    possible_steps = set(range(9))
    for i in possible_steps:
        buttons[i].config(text = f"<num {i+1}>?")
        buttons[i].config(foreground="black")
        buttons[i].config(background="white")
    # buttons[0].config(text="<num 1>?")
    # buttons[1].config(text="<num 2>?")
    # buttons[2].config(text="<num 3>?")
    # buttons[3].config(text="<num 4>?")
    # buttons[4].config(text="<num 5>?")
    # buttons[5].config(text="<num 6>?")
    # buttons[6].config(text="<num 7>?")
    # buttons[7].config(text="<num 8>?")
    # buttons[8].config(text="<num 9>?")
    reset_shortcuts()

reset_shortcuts()

win_cases = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7},
            {2, 5, 8}, {0, 4, 8}, {2, 4, 6}]

possible_steps = set(range(9))
x_cases = set()
o_cases = set()


core.mainloop()
