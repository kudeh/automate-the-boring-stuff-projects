# table-printer.py
# Author: Kene Udeh
# Source: Automate the Boring stuff with python Ch. 6 Project

def printTable(list2D):
    """Prints a table of items right justified
    Args:
        list2D (list): 2D list to print
    Returns:
        None
    """
    
    # get the max length string of each row
    row_max_len = []

    for row in range(len(list2D)):
        row_max_len.append(max([len(col) for col in list2D[row]]))

    # print table right Justified
    for col in range(len(list2D[0])):
        for row in range(len(list2D)):
            print(list2D[row][col].rjust(row_max_len[row]), end=' ')

        print()
        
        

if __name__ == "__main__":

    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]

    printTable(tableData)