from operator import itemgetter


def filter_dict(dictionary, func=None, as_dict=False):
    func = func or itemgetter(1)
    result = list(filter(func, iter(list(dictionary.items()))))
    return as_dict and dictionary(result) or result
