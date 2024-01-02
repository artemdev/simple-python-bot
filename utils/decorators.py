""" Module for registering commands """

handlers = {
}


def register_command(command):
    """ Registers command in handlers """
    def outer_wrapper(func):
        def wrapper(*args):
            return func(*args)

        handlers[command] = func

        return wrapper
    return outer_wrapper


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError as e:
            print(e)
        except ValueError as e:
            print(f'ValueError occurred: {e}')
        except KeyError as e:
            print(f'KeyError occurred: {e}')

        except TypeError as e:
            if (func.__name__ == 'add' or func.__name__ == 'change'):
                print(
                    'Please type command name followed by name and phone. Example: add Alex 1234567890')
                return

            if (func.__name__ == 'phone'):
                print('Please type command name followed by name. Example: phone Alex')
                return

            print(f'TypeError occurred: {e}')

    return wrapper
