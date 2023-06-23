from entrypoint2 import entrypoint


@entrypoint
def func(*args):
    print(args)
