# collatz.py
# Author: Kene Udeh
# Source: Automate the Boring stuff with python Ch. 4 Project

def collatz(number):
    """If number is even (number // 2) else (3 * number + 1)
    Args:
        number (int): number to collatz

    Returns:
        int: collatz number
    """
    if (number % 2) == 0:
        print(number // 2)
        return number // 2
    
    print(3 * number + 1)
    return 3 * number + 1


if __name__ == '__main__':
    

    try:
        
        num = int(input('Enter a number: '))
        result = collatz(num)
        while(result != 1):
            result = collatz(result)

    except ValueError:
        print('Please Enter a Valid Number')

    
    