import random

f0_count, f1_count, f2_count, f3_count = 6, 6, 6, 6
l_count = [f0_count, f1_count, f2_count, f3_count]

symbols = ['♦', '♥', '♣', '♠']
cards = [str(i) + j for i in [*range(6, 11), 'J', 'Q', 'K'] for j in symbols]
random.shuffle(cards)

list_aces = []
list_gates = []
list_gates_card = [cards.pop() for _ in range(5)]

nums = [6]
deck_closed = 0


def get_back(card):
    for i in range(1, 38 + 1):
        card.create_line(0, 8 * i, 8 * i, 0, fill='red')


def view_text(card, text):
    card.config(bg='white', highlightbackground="black", highlightthickness=1)
    card.delete('all')
    if text[-1] in symbols[:2]:
        color = 'red'
    else:
        color = 'black'
    card.create_text(20, 95, text=text[:-1], fill=color, font="Verdana 16", anchor="e", angle=90)
    card.create_text(90, 45, text=text[-1], fill=color, font="Verdana 32", anchor="e", angle=90)
    card.create_text(166, 15, text=text[:-1], fill=color, font="Verdana 16", anchor="e", angle=90)
