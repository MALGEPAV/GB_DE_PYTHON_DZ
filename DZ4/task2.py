import typing


def kwargs_func(**kwargs) -> dict:
    result = dict()
    for key in kwargs:
        if isinstance(kwargs[key], typing.Hashable):
            result[kwargs[key]] = key
        else:
            result[str(kwargs[key])] = key
    return result


for item in kwargs_func(name='John', age=32, children=['Ann', 'Paul']).items():
    print(item)
