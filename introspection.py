import inspect
def introspection_info(obj):
    return dict(
        type = type(obj).__name__,
        attributes = [i for i in dir(obj) if not callable(i)],
        methods = [i for i in dir(obj) if callable(i)],
        module = inspect.getmodule(introspection_info).__name__
    )


number_info = introspection_info(212)
print(number_info)
number_info = introspection_info('212')
print(number_info)
number_info = introspection_info(21.2)
print(number_info)
number_info = introspection_info((212,))
print(number_info)
number_info = introspection_info([212])
print(number_info)
number_info = introspection_info({212})
print(number_info)