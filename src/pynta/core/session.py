class _Session(object):
    pass


class LazySession(object):

    def __init__(self, *args, **kwargs):
        super(LazySession, self).__init__(*args, **kwargs)
        self.__dict__.update(kwargs)


Session = LazySession
