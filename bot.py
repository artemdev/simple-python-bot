from utils.config import SUPPORTED_EXIT_COMMANDS, ALL_SUPPORTED_COMMANDS, SUPPORTED_TERMINATION_COMMANDS

from utils.decorators import input_error, register_command, handlers

store = {
}


@register_command('hello')
def hello():
    """ Greets user"""

    print('How can I help you?')


@register_command('add')
@input_error
def add(name, phone_number):
    """ Adds new contact to contacts store """
    if store.get(name):
        raise KeyError('Contact already exists')
    else:
        store[name] = phone_number
        print(f'Added {name} with {phone_number}')


@register_command('change')
@input_error
def change(name, phone_number):
    """ Changes phone number by name """

    if store.get(name):
        store[name] = phone_number
        print(f'New phone {phone_number}')
    else:
        raise KeyError('Contact not found')


@register_command('phone')
@input_error
def phone(name):
    """ Finds phone number by name """
    if (store.get(name)):
        print(f'{name} phone is {store.get(name)}')
    else:
        raise KeyError('Contact not found')


@register_command('show all')
@input_error
def show_all():
    """ Shows all names with phone numbers """

    for name, phone_number in store.items():
        print(f'{name} phone is {phone_number}')


def validate_command(command):
    """ Checks if user typed command supported by script """
    filtered_commands = list(filter(
        lambda valid_command: command in valid_command, ALL_SUPPORTED_COMMANDS))

    return filtered_commands[-1] if filtered_commands else None


def main():
    """ Validates command and calls handler"""

    while True:
        user_input = input('Please enter command: ').lower()

        valid_command = validate_command(user_input.split(' ')[0])

        if not valid_command:
            print(
                'Please enter one of the following commands: add, change, phone, show all, good bye, close, exit, .')
            continue

        if valid_command in SUPPORTED_EXIT_COMMANDS:
            print('Good bye!')
            break

        if valid_command in SUPPORTED_TERMINATION_COMMANDS:
            break

        command_args = user_input.split(valid_command)[-1].strip()
        command_args_list = [
            command for command in command_args.split(' ') if command]

        if handlers.get(valid_command):
            handlers[valid_command](*command_args_list)


if __name__ == "__main__":
    main()
