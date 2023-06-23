from entrypoint2 import entrypoint


@entrypoint
def main(files=[]):
    """This function has repeating arguments.
    :param files: test input
    """
    print(files)
