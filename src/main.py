import fire
from src.conversor import convert, __print_logo
#from conversor import convert, __print_logo


if __name__ == '__main__':
    __print_logo("url -> desktop")
    fire.Fire(convert)