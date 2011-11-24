from webob.exc import HTTPMethodNotAllowed


def require_method(*method_names):

    def decorator(func):

        def wrapper(self, **kwargs):

            if self.request.method in method_names:
                return func(self, **kwargs)

            else:
                raise HTTPMethodNotAllowed()

        return wrapper

    return decorator


def action(func):

    def wrapper(self, **kwargs):
        self.params = kwargs
        self.context = self.get_context()
        result = func(self, **kwargs)

        if isinstance(result, dict):
            self.context.update(result)
            return self.context

        else:
            return result

    return wrapper
