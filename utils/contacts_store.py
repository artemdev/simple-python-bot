"""Stores information about contacts into dictionary"""

contacts_store = {
}


def add(name, phone_number):
    contacts_store[name] = phone_number


def get_all_items():
    return contacts_store.items()


def get_all_names():
    return contacts_store.keys()


def change(name, phone_number):
    if name in get_all_names():
        add(name, phone_number)
        return True
    else:
        return False


def has_name(name):
    """ Checks if name exists in contacts store """
    return name in get_all_names()


def get_phone_by_name(name):
    """ Returns phone number by name """

    return contacts_store.get(name)
