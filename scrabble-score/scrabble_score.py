def score(word):
    letters = 'AEIOULNRST-DG-BCMP-FHVWY-K---JX--QZ'.split('-')
    dict_score = {b:a for a,c in enumerate(letters,1) for b in c}
    return sum([dict_score[i.upper()] for i in word])