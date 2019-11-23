# Calculate the total cost of tile it would take to cover a floor plan of width and height,
# using a cost entered by the user.

class Tile():
    '''Tile: WIDTH x LENGTH, COST'''
    def __init__(self,width,length,cost):
        self.width = width
        self.length = length
        self.cost = cost

    def __str__(self):
        return '\nA single tile ({}cm x {}cm) costs €{:.2f}.\n'.format(self.width,self.length,self.cost)

    def area(self):
         return (self.width*self.length)/100

def tile_info():
    lst = []
    while 1:
        try:
            width = float(input('Enter the width of each tile in cm: '))
            lst.append(width)
            break
        except:
            print('Invalid input, please try again...')
    while 1:
        try:
            length = float(input('Enter the length of each tile in cm: '))
            lst.append(length)
            break
        except:
            print('Invalid input, please try again...')
    while 1:
        try:
            cost = float(input('What is the cost of each tile in euro: '))
            lst.append(cost)
            break
        except:
            print('Invalid input, please try again...')
    return lst

def square_floor():
    while 1:
        try:
            width = float(input('Enter the width of your floor in meters: '))
            break
        except:
            print('Invalid input, please try again...')
    while 1:
        try:
            length = float(input('Enter the length of your floor in meters: '))
            break
        except:
            print('Invalid input, please try again...')
    return width*length

def complex_floor():
    area = float(input('\nThen enter the area of your floor in square meters (m²): '))
    return area

def is_square():
    while True:
        try:
            question = input('Is your floor plan Rectangle or Complex? r/c')
            if question[0].lower() == 'r':
                return True
            elif question[0].lower() == 'c':
                return False
            else:
                print('Invalid input, please try again...')
        except:
            print('Invalid input, please try again...')


    #cost = float(input('Enter the amount each individual tile costs'))


# MAIN CODE

a,b,c = tile_info()
client_tile = Tile(a,b,c)
print(client_tile)
if is_square():
    client_floor = square_floor()
    print('\nThe area of your floor plan is {}m²\n'.format(client_floor))
else:
    client_floor = complex_floor()
    print('\nThe area of your floor plan is {}m²\n'.format(client_floor))
total_cost = (client_floor/client_tile.area())*client_tile.cost
print('The total cost of tiles for your floor plan will be: €{:.0f}'.format(total_cost))
print('You will need minimum {:.2f} tiles'.format(client_floor/client_tile.area()))