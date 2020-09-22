def distance(strand_a, strand_b):
    if len(strand_a) != len (strand_b):
        raise ValueError("The lengths of the strands is not equal.")
    else:
        tuples = zip(strand_a,strand_b)
        errors = [x != y for x , y in tuples]
        return errors.count(True)