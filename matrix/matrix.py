class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = [[int(j) for j in i.split(' ')] for i in matrix_string.split('\n')]

    def row(self, index):
        return self.matrix_string[index-1]
      

    def column(self, index):
        return [i[index-1] for i in self.matrix_string] 