def add_first_arg(arg_default):

    def decorator(func):

        def wrapper(*args, **kwargs):

            if len(args) + len(kwargs) < func.__code__.co_argcount:
                args = (arg_default,) + args

            return func(*args, **kwargs)

        return wrapper

    return decorator
