def decorator_func(func):
    def wrapper():
        print('wrapper')
        print('Оборачиваем функцию', func)

        func()

    return wrapper

@decorator_func
def hello_world():
    print('hello')

hello_world()