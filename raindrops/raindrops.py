def convert(number):
    l1 = [[3, 'Pling'], [5,'Plang'], [7, 'Plong']]
    l2 = [j for i, j in l1 if number % i == 0]
    return str(number) if not l2 else ''.join(l2) 