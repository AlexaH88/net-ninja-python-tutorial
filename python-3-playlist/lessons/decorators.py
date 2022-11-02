# a decorator is a wrapper function to be applied to another function
# define the wrapper function so it can be called with the @ below
# func is the question function below
def cough_dec(func):

    # wrapper function that extends the behaviour of the question function below
    def func_wrapper():
        # code before function
        print('*cough*')
        # run the function
        func()
        # code after function
        print('*cough*')

    return func_wrapper()


@cough_dec
def question():
    print('Can you give me a discount on that?')


# decorators can be applied to any and several functions
@cough_dec
def answer():
    print("It's only 50p, you cheapskate")


question()
answer()
