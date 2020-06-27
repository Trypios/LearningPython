import random

def randomizer(dict):
    """Returns a random key from a dictionary"""
    return random.choice(list(dict.keys()))

def group(*args):
    """Takes weights as arguments and returns the sum"""
    total_weight = 0
    for person in args:
        total_weight += weights[person]
    return total_weight

def heavy_or_light(w1, w2):
    """Determines the status of the 1st argument"""
    if w1 > w2:
        return 'heavier'
    else:
        return 'lighter'

def underline(string):
    """returns a string of characters '=' equal to the argument"""
    lines = '=' * (len(weighing1) - 1)
    return lines
        
    
# 12 people of equal weights, then randomly turn one of them heavier/lighter
weights = {'1': 10, '2': 10, '3': 10, '4': 10, '5': 10, '6': 10, '7': 10, '8': 10, '9': 10, '10': 10, '11': 10, '12': 10}
weights[randomizer(weights)] = random.choice([15, 5])

# 1st weighing
# (case1)
weighing1 = '\nWeighing #1: Comparing (1 2 3 4) with (5 6 7 8)'
print(weighing1)
print(underline(weighing1))

if group('1', '2', '3', '4') == group('5', '6', '7', '8'):
    print('(1 2 3 4) = (5 6 7 8)')
    print('Since the groups are equal, the suspect is one of the other group (9 10 11 12)')
    
    # 2nd weighing
    weighing2 = '\nWeighing #2: Comparing (9 10 11) with a standard weighted group like (1 2 3)'
    print(weighing2)
    print(underline(weighing2))
    
    # (case 1a)
    if group('9', '10', '11') == group('1', '2', '3'):
        print('(9 10 11) = (1 2 3)')
        print('Since the groups are equal, the suspect is (12)')
        
        # 3rd weighing
        # (case 1a)
        weighing3 = '\nWeighing #3: Comparing (12) with any one of the others'
        print(weighing3)
        print(underline(weighing3))
        
        status = heavy_or_light(weights['12'], weights['1'])
        print('(12) is {} than the rest'.format(status))
    
    # (case 1b & 1c)
    else: #group('9', '10', '11') != group ('1', '2', '3')
        status = heavy_or_light(group('9', '10', '11'), group('1', '2', '3'))
        
        # (case 1b)
        if status == 'heavier':
            print('(9 10 11) > (1 2 3)')
            print('The suspect is {} and among (9 10 11)'.format(status))
            
            # 3rd weighing
            # (case 1b)
            weighing3 = '\nWeighing #3: Comparing (9) with (10)'
            print(weighing3)
            print(underline(weighing3))
            
            if weights['9'] > weights['10']:
                print('(9) > (10)')
                print('So (9) is {} than the rest'.format(status))
            elif weights['9'] < weights['10']:
                print('(9) < (10)')
                print('So (10) is {} than the rest'.format(status))
            else: # weights['9'] == weights['10']
                print('(9) = (10)')
                print('So (11) is {} than the rest'.format(status))
                
        # (case 1c)
        else: # status == 'lighter'
            print('(9 10 11) < (1 2 3)')
            print('The suspect is {} and among (9 10 11)'.format(status))
            
            # 3rd weighing
            # (case 1b)
            weighing3 = '\nWeighing #3: Comparing (9) with (10)'
            print(weighing3)
            print(underline(weighing3))
            
            if weights['9'] < weights['10']:
                print('(9) < (10)')
                print('So (9) is {} than the rest'.format(status))
            elif weights['9'] > weights['10']:
                print('(9) > (10)')
                print('So (10) is {} than the rest'.format(status))
            else: # weights['9'] == weights['10']
                print('(9) = (10)')
                print('So (11) is {} than the rest'.format(status))

######################
######################
            
# 1st weighing
# (case2)
else: # group('1', '2', '3', '4') != group('5', '6', '7', '8')
    if group('1', '2', '3', '4') > group('5', '6', '7', '8'):
        print('(1 2 3 4) > (5 6 7 8)')
        print('The suspect is either heavier in group (1 2 3 4) or lighter in group (5 6 7 8)')
        
        print('')
        print('Take the 1st halves of groups (1 2 3 4) and (5 6 7 8) and two more persons: an unknown like (7) and a known standard weighted like (9)...')
        print('...to form the groups (1 5 6) and (2 7 9)')
        
        # 2nd weighing
        weighing2 = '\nWeighing #2: Comparing (1 5 6) with (2 7 9)'
        print(weighing2)
        print(underline(weighing2))

        # (case 2a)
        if group('1', '5', '6') > group('2', '7', '9'):
            print('(1 5 6) > (2 7 9)')
            print('The suspect is either a heavier (1) or a lighter (7)')

            # 3rd weighing
            # (case 2a)
            weighing3 = '\nWeighing #3: Comparing (1) with (9)'
            print(weighing3)
            print(underline(weighing3))

            if weights['1'] > weights['9']:
                status = heavy_or_light(weights['1'], weights['9'])
                print('(1) > (9)')
                print('So (1) is heavier than the rest')
            else:
                status = heavy_or_light(weights['7'], weights['9'])
                print('(1) < (9)')
                print('So (7) is lighter than the rest')
 
        elif group('1', '5', '6') < group('2', '7', '9'):
            print('(1 5 6) < (2 7 9)')
            print('The suspect is either a heavier (2) or a lighter out of (5 6)')

            # 3rd weighing
            # (case 2b)
            weighing3 = '\nWeighing #3: Comparing (5) with (6)'
            print(weighing3)
            print(underline(weighing3))

            if weights['5'] < weights['6']:
                status = heavy_or_light(weights['5'], weights['6'])
                print('(5) < (6)')
                print('So (5) is lighter than the rest')
            elif weights['5'] > weights['6']:
                print('(5) > (6)')
                status = heavy_or_light(weights['6'], weights['5'])
                print('So (6) is lighter than the rest')
            else: # weights['5'] == weights['6']
                print('(5) = (6)')
                status = heavy_or_light(weights['2'], weights['9'])
                print('So (2) is heavier than the rest')
            
        # (case 2c)
        else: # group('1', '5', '6') == group('2', '7', '9')
            print('(1 5 6) = (2 7 9)')
            print('The suspect is either a lighter (8) or a heavier out of (3 4)')

            # 3rd weighing
            # (case 2c)
            weighing3 = '\nWeighing #3: Comparing (3) with (4)'
            print(weighing3)
            print(underline(weighing3))

            if weights['3'] < weights['4']:
                status = heavy_or_light(weights['4'], weights['3'])
                print('(3) < (4)')
                print('So (4) is heavier than the rest')
            elif weights['3'] > weights['4']:
                print('(3) > (4)')
                status = heavy_or_light(weights['3'], weights['4'])
                print('So (3) is heavier than the rest')
            else: # weights['5'] == weights['6']
                print('(3) = (4)')
                status = heavy_or_light(weights['8'], weights['9'])
                print('So (8) is lighter than the rest')

######################
######################

    # 1st weighing
    # (case 3 - similar to case 2, inverted)
    else: # ('1', '2', '3', '4') < group('5', '6', '7', '8')
        print('(1 2 3 4) < (5 6 7 8)')
        print('The suspect is either lighter in group (1 2 3 4) or heavier in group (5 6 7 8)')
        
        print('')
        print('Take the 1st halves of groups (1 2 3 4) and (5 6 7 8) and two more persons: an unknown like (3) and a known standard weighted like (9)...')
        print('...to form the groups (1 2 5) and (3 6 9)')
        
        # 2nd weighing
        weighing2 = '\nWeighing #2: Comparing (1 2 5) with (3 6 9)'
        print(weighing2)
        print(underline(weighing2))
        
        # (case 3a)
        if group('1', '2', '5') < group('3', '6', '9'):
            print('(1 2 5) < (3 6 9)')
            print('The suspect is either a heavier (6) or a lighter out of (1 2)')

            # 3rd weighing
            # (case 3a)
            weighing3 = '\nWeighing #3: Comparing (1) with (2)'
            print(weighing3)
            print(underline(weighing3))
            
            if weights['1'] < weights['2']:
                status = heavy_or_light(weights['1'], weights['2'])
                print('(1) < (2)')
                print('So (1) is lighter than the rest')
            elif weights['2'] > weights['1']:
                print('(1) > (2)')
                status = heavy_or_light(weights['2'], weights['1'])
                print('So (2) is lighter than the rest')
            else: # weights['5'] == weights['6']
                print('(1) = (2)')
                status = heavy_or_light(weights['6'], weights['9'])
                print('So (6) is heavier than the rest')
            
        # (case 3b)
        elif group('1', '2', '5') > group('3', '6', '9'):
            print('(1 2 5) > (3 6 9)')
            print('The suspect is either a heavier (5) or a lighter (3)')

            # 3rd weighing
            # (case 3b)
            weighing3 = '\nWeighing #3: Comparing (3) with (9)'
            print(weighing3)
            print(underline(weighing3))

            if weights['3'] == weights['9']:
                status = heavy_or_light(weights['5'], weights['9'])
                print('(3) = (9)')
                print('So (5) is heavier than the rest')
            else:
                status = heavy_or_light(weights['3'], weights['9'])
                print('(3) < (9)')
                print('So (3) is lighter than the rest')
        
        # (case 3c)
        else: # group('1', '2', '5') == group('3', '6', '9')
            print('(1 2 5) = (3 6 9)')
            print('The suspect is either a lighter (4) or a heavier out of (7 8)')

            # 3rd weighing
            # (case 3c)
            weighing3 = '\nWeighing #3: Comparing (3) with (4)'
            print(weighing3)
            print(underline(weighing3))

            if weights['7'] < weights['8']:
                status = heavy_or_light(weights['8'], weights['7'])
                print('(7) < (8)')
                print('So (8) is heavier than the rest')
            elif weights['7'] > weights['8']:
                print('(7) > (8)')
                status = heavy_or_light(weights['7'], weights['8'])
                print('So (7) is heavier than the rest')
            else: # weights['5'] == weights['6']
                print('(7) = (8)')
                status = heavy_or_light(weights['4'], weights['9'])
                print('So (4) is lighter than the rest')
        
# testing
print('\n\n')
if status == 'lighter':
    print('{} is {}'.format(min(weights, key=weights.get), status))
elif status == 'heavier':
    print('{} is {}'.format(max(weights, key=weights.get), status))
print(weights)