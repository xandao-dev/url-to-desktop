import fire
from pyfiglet import Figlet
from src.conversor import url_to_desktop


def print_logo(text_logo):
    figlet = Figlet(font='slant')
    print(figlet.renderText(text_logo))


if __name__ == '__main__':
    print_logo("url -> desktop")
    fire.Fire(url_to_desktop)