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
