"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.
    :param card: str - given card.
    :return: int - value of a given card. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    """
    if card == 'A':
        return 1
    if card == 'K' or card == 'Q' or card == 'J':
        return 10
    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.
    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :return: higher value card - str. Tuple of both cards if they are of equal value.
    """
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    if value_of_card(card_one) < value_of_card(card_two):
        return card_two
    return (card_one, card_two)


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.
    :param card_one, card_two: str - card dealt. 'J', 'Q', 'K' = 10;
           'A' = 11 (if already in hand); numerical value otherwise.
    :return: int - value of the upcoming ace card (either 1 or 11).
    """
    card_one = ace_in_hand_value(card_one)
    card_two = ace_in_hand_value(card_two)
    if value_of_card(card_one) + value_of_card(card_two) > 10:
        return 1
    return 11


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.
    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 11; numerical value otherwise.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """
    card_one = ace_in_hand_value(card_one)
    card_two = ace_in_hand_value(card_two)
    return (value_of_card(card_one) + value_of_card(card_two)) == 21


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.
    :param card_one, card_two: str - cards dealt.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """
    card_one = ace_in_hand_value(card_one)
    card_two = ace_in_hand_value(card_two)
    return (value_of_card(card_one) + value_of_card(card_two)) % 2 == 0


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """
    if card_one == 'A' and card_two == 'A':
        return False
    if value_of_card(card_one) + value_of_card(card_two) > 11:
        return False
    return True


def ace_in_hand_value(card):
    if card == 'A':
        return 11
    return card