# C คือ clubs ดอกจิก 
# D คือ Diamond หลามตัด
# H คือ hearts หัวใจ
# S คือ Spade โพธิ์ดำ
deck = ['9H', '3D', '4S', 'AD', 'KD', '8S', 'QS', '10C', '7H', '8D', '4C', '2C', '10S', '7S', '2S', '4H', 'JD', '10H', 'AC', '5C', '6D', '2H', 'JH', 'JC', 'JS', '6S', '3C', '2D', '4D', '6C', 'AH', '8H', 'QH', '9S', '8C', '10D', '3H', '3S', '7C', 'QC', 'KS', '6H', 'KH', '9C', 'AS', 'QD', '7D', 'KC', '5D', '5S', '5H', '9D']

suit_piority = {
    'C': 1,
    'D': 2,
    'H': 3,
    'S': 4
}

value_piority = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13
}

def details(card):
    suit = suit_piority.get(card[-1])
    value = value_piority.get(card[:-1])
    return suit, value

deck.sort(key=details)
print(*deck)
