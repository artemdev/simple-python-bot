from utils.config import SUPPORTED_EXIT_COMMANDS, ALL_SUPPORTED_COMMANDS, SUPPORTED_TERMINATION_COMMANDS

from utils.decorators import input_error, register_command, handlers
import utils.contacts_store as contacts_store


@register_command('hello')
def hello():
    """ Greets user"""

    print('How can I help you?')


@register_command('add')
@input_error
def add(name, phone_number):
    """ Adds new contact to contacts store """
    contacts_store.add(name, phone_number)

    print(f'Added {name} with {phone_number}')


@register_command('change')
@input_error
def change(name, phone_number):
    """ Changes phone number by name """

    if contacts_store.change(name, phone_number):
        print(f'Changed {name} with {phone_number}')
    else:
        print('Contact not found')


@register_command('phone')
@input_error
def phone(name):
    """ Finds phone number by name """
    if (contacts_store.has_name(name)):
        print(f'{name} phone is {contacts_store.get_phone_by_name(name)}')
    else:
        print('Contact not found')


@register_command('show all')
@input_error
def show_all():
    """ Shows all names with phone numbers """

    for name, phone_number in contacts_store.get_all_items():
        print(f'{name} phone is {phone_number}')


def validate_command(command):
    """ Checks if user typed command supported by script """
    filtered_commands = list(filter(
        lambda valid_command: valid_command in command, ALL_SUPPORTED_COMMANDS))
    return filtered_commands[-1] if filtered_commands else None


def main():
    """ Validates command and calls handler"""

    while True:
        user_input = input('Please enter command: ').lower()

        valid_command = validate_command(user_input)

        if not valid_command:
            print(
                'Please enter one of the following commands: add, change, phone, show all, good bye, close, exit, .')
            continue

        if valid_command in SUPPORTED_EXIT_COMMANDS:
            print('Good bye!')
            break

        if valid_command in SUPPORTED_TERMINATION_COMMANDS:
            break

        parsed_args = user_input.split(valid_command)[
            1].strip()

        command_args = parsed_args.split(
            ' ') if parsed_args else []

        if handlers.get(valid_command):
            handlers[valid_command](*command_args)


if __name__ == "__main__":
    main()
