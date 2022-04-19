magic_square = [[8, 3, 4],
                [1, 5, 9],
                [6, 7, 3]]
i=0
while i<len(magic_square):
    j=0
    row=0
    column=0
    d1=0
    while j<len(magic_square[i]):
        row=row+magic_square[i][j]
        column=column+magic_square[j][i]
        d1=d1+magic_square[j][j]
        j+=1
    i+=1
print("Row",row)
print("column",column)
print("decimal",d1)
if row==column==d1:
    print("it is a magic_square")
else:
    print("it is not a magic_square")


                