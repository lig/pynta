from operator import itemgetter


def filter_dict(dictionary, func=None, as_dict=False):
    func = func or itemgetter(1)
    result = filter(func, dictionary.iteritems())
    return as_dict and dictionary(result) or result
