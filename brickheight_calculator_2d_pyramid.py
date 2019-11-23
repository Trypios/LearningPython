'''
THIS PROGRAM CALCULATES THE MAX HEIGHT OF A 2D PYRAMID (IN BRICKS ROWS)
CONSTRUCTED FROM A SPECIFIED NUMBER OF BRICKS GIVEN BY THE USER.
IT DISCARDS THE EXCESS NUMBER OF BRICKS

ie:
the pyramid below is 3 rows high, constructed by 6-9 bricks.
If we had 10 bricks the rows would be four.
         ______
     ___[______]___
 ___[______][______]___
[______][______][______]
'''

available_bricks = int(input('Insert No of bricks: '))
used_bricks = 0
height = 0

while available_bricks-used_bricks > 0:
    used_bricks += 1
    height += 1
    available_bricks -= used_bricks
    print(used_bricks,available_bricks,height)
else:
    print('the pyramid is {} rows tall'.format(height))

'''
#Another way:

bricks = int(input('Insert No of Bricks: '))
height = 0
stock = 0

while stock <= bricks:
    if bricks <= 1:
        break
    else:
        stock += 1
        bricks -= stock
        height += 1
        print(bricks, stock, height)
print('the pyramid is {} rows tall'.format(height))
'''