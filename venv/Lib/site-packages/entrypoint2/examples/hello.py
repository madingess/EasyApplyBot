from entrypoint2 import entrypoint


@entrypoint
def hello(message):
    # type of 'message' is not defined, default is str
    print(message)
