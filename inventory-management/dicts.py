def create_inventory(items):
    """
    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """
    my_dict = {}
    for item in items:
        if item not in my_dict:
            my_dict[item] = 1
            continue
        my_dict[item] += 1
    return my_dict


def add_items(inventory, items):
    """
    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """
    if len(inventory) == 0:
        return create_inventory(items)

    for item in items:
        if item in inventory:
            inventory[item] += 1
            continue
        inventory[item] = 1
    return inventory


def decrement_items(inventory, items):
    """
    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """
    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
    return inventory


def remove_item(inventory, item):
    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """
    if item in inventory:
        del inventory[item]
    return inventory


def list_inventory(inventory):
    """
    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    ret = list()
    for item in inventory.items():
        if item[1] > 0: ret.append(item)
    return ret
