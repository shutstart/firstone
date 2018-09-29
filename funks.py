def fun(m):
    return m * m


f = fun
print(fun(2))
# HIGHER ORDER FUNCTION:
# when a function takes a function as an argument and it returns a function as
# an argument.

# Map function:


def cube(a):
    return a * a * a


def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


listy = [1, 2, 4, 5, 7]
cubes = my_map(cube, listy)

print(cubes)


def logger(msg):

    def log():
        print("log:", msg)
    return log


logsub = logger('ji')  # logsub now is nothing but log function now we can use
# logsub() to call log function
logsub()  # logsub remembered our msg ('ji') and this is nothing but closure

#  application of first class closures


def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}<\{0}>'.format(tag, msg))
        return "you fool"

    return wrap_text


html_ss = html_tag('h1')
html_ss("hello this is me")
html_ss("i was wondering if after all these years you would like to meet")
print(html_ss("its no secret"))
