import math

# taking the co-ordinate input.
def user_input():
    while True:
        try:
            print("\nInput Format: input 2 2 for (2,2)")
            number = input("Enter the co-ordinates: \n")
            a = int(number.split(" ")[0])
            b = int(number.split(" ")[1])
            return a, b
        
        except ValueError:
            print('\nInvalid input\n')
            print('_____________________________________________')
            continue

        except IndexError:
            print('\nInvalid input\n')
            print('_____________________________________________')
            continue
        
        else:
            break
      
def choice():
    letter = ''
    letter = input('Press Y for yes or N for no.\n').upper()
    while not (letter == 'Y' or letter == 'N'): #checking the validation of the letter choice
        print('That is an incorrect choice')
        letter = input('Press Y for yes or N for no.\n').upper()
                
    if letter == 'Y':
        return True
    else:
        return 0

# defining a function to calculate number of paths from (0, 0) to (a, b) 
def paths(a, b):
    return int((math.factorial(a+b))/(math.factorial(a)*math.factorial(b)))

# Taking the grid size
def grid():
    print('Please Enter the grid dimensions:')
    total = user_input()
    return total

# takeing user input for block points
def block_input():
    print('\nDo you want to add a block point?')
    choice_block = choice()
    if choice_block == True:
        z = user_input()
        return block_paths(z)
    else:
        return 0

def block_paths(z):
    b1 = z[0]
    b2 = z[1]
    while (b1 > m) or (b2 > n):
        print('Incorrect block point position, please re-enter.')
        z = block_input()
        b1 = z[0]
        b2 = z[1]
    blocked_p = (paths(b1,b2)*paths(m-b1, n-b2))
    return blocked_p

# takeing user input for jump points
def jump_input():
    print('\nDo you want to add a jump point?')
    choice_jump = choice()
    if choice_jump == True:
        x = []
        print('\nPlease enter the points you want to jump between')
        for a in range(2):
            b = user_input()
            x.extend(b)        
        a = (x[0],x[1])
        j1 = simple_paths - block_paths(a)
        j2 = (paths(m-x[2], n-x[3])*paths(x[0],x[1]))
        return (j1+j2)
    else:
        return 0


def main():
    print("Hello! I am Aditya, your personal path calculator.")
    print("Give me any hurdles and jumps.")
    print("I will tell you how many paths can take you to your goal.\n")
    while(True):
        global m, n, simple_paths
        total = grid()
        m = total[0] - 1
        n = total[1] - 1
        simple_paths = paths(m,n)
        final = simple_paths
        blocked_paths = block_input()
        if blocked_paths != 0:
            final = simple_paths - blocked_paths
        else:
            jumped_paths = jump_input()
            final = jumped_paths
        print('\nSo, you can reach the destination through ', final ,' ways.')
        print('\nDo you want to restart?')
        re_choice = choice()
        print('\n')
        if re_choice == True:
            continue
        elif re_choice == False:
            break
        
if __name__ == "__main__":
    main()
