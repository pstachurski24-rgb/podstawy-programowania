
def hide(card_number):
    if len(card_number) != 16 or not card_number.isdigit():
        return "Invalid card number"

    return card_number[:2] + "*" * 10 + card_number[-4:]
