from tkinter import *
from tkinter import messagebox
from const import *


def click_gate(*args):
    global deck_closed
    view_text(list_gates[len(nums)-2], list_gates_card[len(nums)-2])
    num = symbols.index(list_gates_card[len(nums)-2][-1])
    l_count[num] += 1
    list_aces[num].grid(row=num, column=l_count[num])
    deck_closed = 0
    c.focus_set()


def click(*args):
    global l_count, list_aces, cards, deck_closed, nums
    if deck_closed:
        return
    card_text = cards.pop()
    num = symbols.index(card_text[-1])

    view_text(pile, card_text)

    l_count[num] -= 1
    list_aces[num].grid(row=num, column=l_count[num])

    if all(number not in l_count for number in nums):
        deck_closed = 1
        list_gates[len(nums)-1].bind('<Button-1>', click_gate)
        list_gates[len(nums) - 1].bind('<Return>', click_gate)
        list_gates[len(nums)-1].focus_set()
        nums.append(nums[-1]-1)

    if l_count[num] == 0:
        deck_closed = 1
        print(f"Ace of {card_text[-1]} wins!")

        mb = messagebox.askyesno('Game over!', f'Ace of {card_text[-1]} has won this game!\nDo you want to play again?')
        if mb:
            mb2 = messagebox.showerror('ERROR', 'Я ебал еще и это реализовывать)')
            if mb2:
                root.destroy()
        else:
            root.destroy()


root = Tk()
root.configure(background='forest green')

#root.geometry('1440x690')


for i in range(4):
    list_aces.append(Canvas(height=120, width=186.6, bg='white', highlightbackground="black", highlightthickness=1))
    list_aces[i].grid(row=i, column=6, padx=5, pady=5)

    view_text(list_aces[i], 'A' + symbols[i])


for i in range(5):
    list_gates.append(Canvas(height=120, width=186.6, bg='white', highlightbackground="black", highlightthickness=1))
    list_gates[i].grid(row=4, column=5 - i, padx=5, pady=25)
    get_back(list_gates[i])

deck_frame = Canvas(height=130, width=195, bg='forest green', highlightbackground="forest green", highlightthickness=0)
deck_frame.grid(row=4, column=0, padx=15)

for i in range(4, 1, -2):

    Canvas(deck_frame, height=120, width=186.6, bg='white', highlightbackground="black", highlightthickness=1) \
        .place(x=i, y=i)
c = Canvas(deck_frame, height=120, width=186.6, bg='white', highlightbackground="black", highlightthickness=1)
c.place(x=0, y=0)

get_back(c)
c.focus_set()
c.bind('<Button-1>', click)
c.bind('<Return>', click)
pile = Canvas(height=120, width=186.6, bg='forest green', highlightbackground="forest green", highlightthickness=1)
pile.grid(row=4, column=6, padx=15, pady=25)

root.geometry('600x600')







root.mainloop()
