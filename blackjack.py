from tkinter import *
import random
import time

play = 0
com_hand = []
player_hand = []
p_score = 0
c_score = 0
deck = ['A H', '2 H', '3 H', '4 H', '5 H', '6 H', '7 H', '8 H', '9 H', '10 H', 'J H', 'Q H', 'K H',
         'A D', '2 D', '3 D', '4 D', '5 D', '6 D', '7 D', '8 D', '9 D', '10 D', 'J D', 'Q D', 'K D',
         'A S', '2 S', '3 S', '4 S', '5 S', '6 S', '7 S', '8 S', '9 S', '10 S', 'J S', 'Q S', 'K S',
         'A C', '2 C', '3 C', '4 C', '5 C', '6 C', '7 C', '8 C', '9 C', '10 C', 'J C', 'Q C', 'K C',]

#resets the deck and hands
def reset():
    global player_hand
    global com_hand
    global deck
    global win
    global xpointp
    global xpointc
    global p_score
    global c_score
    c_score = 0
    p_score = 0
    com_hand = []
    player_hand = []
    deck = ['A H', '2 H', '3 H', '4 H', '5 H', '6 H', '7 H', '8 H', '9 H', '10 H', 'J H', 'Q H', 'K H',
         'A D', '2 D', '3 D', '4 D', '5 D', '6 D', '7 D', '8 D', '9 D', '10 D', 'J D', 'Q D', 'K D',
         'A S', '2 S', '3 S', '4 S', '5 S', '6 S', '7 S', '8 S', '9 S', '10 S', 'J S', 'Q S', 'K S',
         'A C', '2 C', '3 C', '4 C', '5 C', '6 C', '7 C', '8 C', '9 C', '10 C', 'J C', 'Q C', 'K C',]

    win = Tk()
    win.attributes("-topmost", 1)
    win.title("Blackjack")
    win.geometry("1000x600")

    a = Label( win, text = "Dealer Hand", font = ("Courier"))
    a.place( x = 20, y = 20 )
    b = Label( win, text = "Player Hand", font = ("Courier"))
    b.place( x = 20, y = 100 )
    d = Label( win, text = deck[1], font = ("Courier"))
    playerscore = Label( win, text = "Score: " + str(p_score), font = ("Courier"))
    playerscore.place( x = 200, y = 100 )
    comscore = Label( win, text = "Score: " + str(p_score), font = ("Courier"))
    comscore.place( x = 200, y = 20 )

    xpointp = 20
    xpointc = 20
    


#deals a card to a specified hand from the deck and removes it from the deck
def deal( H ):
    global deck
    x = random.randint(0, (len(deck) - 1))
    global d
    d = Label( win, text = deck[x], font = ("Courier" ))
    H.append(deck[x])
    deck.remove(deck[x])
    return H



#calculates the value of a hand
def scoreHand( hand ):
    score = 0

    #appends aces to the end to make my scoring logic work
    hold = []
    for e in hand:
        if e[0] == 'A':
            hold.append(e)
            hand.remove(e)
    hand.extend(hold)

    #checks the value of each card and adds to the score
    for e in hand:

        if e[0] == '1':
            score += 10
        elif e[0] == 'J':
            score += 10
        elif e[0] == 'Q':
            score += 10
        elif e[0] == 'K':
            score += 10
        #changes ace value based on the current score
        elif e[0] == 'A':
            if score + 11 > 21:
                score += 1
            else:
                score += 11
        else:
            score += int(e[0])
            
    return score

def showScorep():
    global p_score
    global player_hand
    p_score = scoreHand( player_hand )
    playerscore = Label( win, text = "Score: " + str(p_score), font = ("Courier"))
    playerscore.place( x = 200, y = 100 )

def showScorec():
    global c_score
    global com_hand
    c_score = scoreHand( com_hand )
    playerscore = Label( win, text = "Score: " + str(c_score), font = ("Courier"))
    playerscore.place( x = 200, y = 20 )

def comFunc():
    global com_hand
    global xpointc
    global c_score
    com_hand = deal( com_hand )
    d.place( x = xpointc, y = 60 )
    xpointc += 50
    showScorec()


def playFunc():
    global player_hand
    global xpointp
    global p_score
    player_hand = deal( player_hand )
    d.place( x = xpointp, y = 140 )
    xpointp += 50
    showScorep()
    if p_score > 21:
        endGame()

def checkWin():
    global p_score
    global c_score
    if p_score > 21:
        end = Label( win, text = "You busted with " + str(p_score) +". Dealer wins.", font = ("Courier"))
    elif c_score > 21:
        end = Label( win, text = "Dealer busts.  You win!", font = ("Courier"))
    elif p_score > c_score:
        end = Label( win, text = "Your " + str(p_score) + " beats the dealer's " + str(c_score) + ". You win! ", font = ("Courier"))
    elif c_score > p_score:
        end = Label( win, text = "The dealer's " + str(c_score) + " beats your " + str(p_score) + ". You lose!", font = ("Courier"))
    elif c_score == p_score:
        end = Label( win, text = "Your value matches the dealer's.  Tie.", font = ("Courier"))
    end.place( x = 400, y = 450 )

def endGame():
    global c_score
    global p_score
    while c_score < 17 and p_score <= 21:
        comFunc()
    checkWin()

def leaveProgram():
    win.destroy()
    quit()

while play != 2:
    reset()
    playFunc()
    comFunc()
    playFunc()
    comFunc()

    hit = Button( win, text = "Hit", command = playFunc )
    hit.place( x = 520, y = 500 )

    stay = Button( win, text = "Stay", command = endGame )
    stay.place( x = 480, y = 500 )

    abort = Button( win, text = "Exit", command = leaveProgram )
    abort.place( x = 800, y = 0 )


    mainloop()
