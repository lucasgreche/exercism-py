verses = {0: "first", 1: "second", 2: "third", 3: "fourth", 4: "fifth", 5: "sixth", 6: "seventh", 7: "eighth", 8: "ninth", 9: "tenth", 10: "eleventh", 11: "twelfth"}
gifts = ['a Partridge in a Pear Tree.', 'two Turtle Doves', 'three French Hens', 'four Calling Birds', 'five Gold Rings', 'six Geese-a-Laying', 'seven Swans-a-Swimming', 'eight Maids-a-Milking', 'nine Ladies Dancing', 'ten Lords-a-Leaping', 'eleven Pipers Piping', 'twelve Drummers Drumming']

def recite(start_verse, end_verse):
    return [contruction(i) for i in range(start_verse-1,end_verse)]

def contruction(verse):
    header = f'On the {verses.get(verse)} day of Christmas my true love gave to me: '
    tails = ', '.join(gifts[verse:0:-1])
    if verse == 0:
        return header + gifts[0]
    return header + tails + ', and ' + gifts[0] 