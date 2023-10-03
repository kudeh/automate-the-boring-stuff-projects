# game-inventory.py
# Author: Kene Udeh
# Source: Automate the Boring stuff with python Ch. 5 Project

def displayInventory(inventory):
    """ Displays how much of what a player has in inventory
        
    Args:
        inventory (dict): Inventory containing items and their counts

    Returns: 
        None
    """
    print("Inventory:")
    item_total = 0

    for k, v in inventory.items():
        print(v, ' ', k)
        item_total += v

    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    """ Add Items to inventory
        Args:
            inventory (dict):  Inventory containing items and their counts
            addedItems (list): Items to add to inventory

        Returns:
            updatedInventory (dict): Inventory containing updated items and their counts
    """
     # YOUR CODE GOES HERE
    newInventory = dict(inventory)
    for item in addedItems:
        newInventory.setdefault(item, 0)

        if item not in inventory.keys():
            inventory[item] = 0
            newInventory = inventory
            for i in newInventory.keys():
                if i in addedItems:
                    newInventory[i] += 1

        elif item in inventory.keys():
            newInventory[item] += 1
    return newInventory
    


if __name__ == "__main__":

    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    displayInventory(stuff)

    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = addToInventory(inv, dragonLoot)
    displayInventory(inv)
