cards = {
    "A":10,
    "K":10,
    "Q":10,
    "J":10,
    "T":10,
    "9":9,
    "8":8,
    "7":7,
    "6":6,
    "5":5,
    "4":4,
    "3":3,
    "2":2,
    "1":1
}

def f(player1,player2):
    player1_points = 0
    player2_points = 0

    for card in player1:
        player1_points += cards.get(card)

    for card in player2:
        player2_points += cards.get(card)

    if player1_points > player2_points:
        return True
    elif player1_points <= player2_points:
        return False

