#
# Python can have dynamic argument list (or dict)
#

def func(*args, **kwargs):
    print('invoke function with: ({}, {})'.format(args, kwargs))


if __name__ == '__main__':
    func(1, 2, 3, a='a', b='b')
    # you can convert a list to argument list
    # try to compare the results of these two function calls
    func(*[1, 2, 3])
    func([1, 2, 3])

    # you can convert a dict to argument dict
    func(**{'a':'a', 'b':'b'})
    func({'a':'a', 'b':'b'})