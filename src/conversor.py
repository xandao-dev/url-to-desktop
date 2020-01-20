import os, shutil
from typing import List, Optional
from pyfiglet import Figlet


def __print_logo(text_logo):
    figlet = Figlet(font='slant')
    print(figlet.renderText(text_logo))


def convert(path: Optional[str] = None) -> None:
    if path is None:
        path = os.getcwd()
        
    url_list_path = __get_url_files_path(path)
    url_filenames = __get_url_filenames_without_extension(url_list_path)
    old_url_folder_name = __create_old_url_folder(path, url_list_path)
    __copy_url_files_to_old_url_folder(path, url_list_path, old_url_folder_name)
    __change_url_to_desktop(url_list_path, url_filenames)


def __get_url_files_path(path: str) -> List[str]:
    url_list_path = list()
    for file in os.listdir(path):
        if file.endswith(".url") or file.endswith(".URL"):
            url_list_path.append(os.path.join(path, file))
    return url_list_path


def __get_url_filenames_without_extension(url_list_path: List[str]) -> List[str]:
    url_filenames = list()
    for path in url_list_path:
        url_filenames.append(os.path.splitext(os.path.basename(path))[0])
    return url_filenames


def __create_old_url_folder(path, url_list_path):
    if len(url_list_path) <= 0:
        return

    old_url_folder_name = 'old urls'
    if not os.path.isdir(os.path.join(path, old_url_folder_name)):
        os.mkdir(os.path.join(path, old_url_folder_name))
    return old_url_folder_name


def __copy_url_files_to_old_url_folder(path, url_list_path, old_url_folder_name):
    for file_path in url_list_path:
        shutil.copy(file_path, os.path.join(path, old_url_folder_name))


def __change_url_to_desktop(url_list_path: List[str], url_filenames: List[str]):
    for file_path, filename in zip(url_list_path, url_filenames):
        # Take the URL from file
        url_file = open(file_path, 'r')
        for i, line in enumerate(url_file):
            if i == 1:
                url = line
        url_file.close()

        # Verify if we got the URL
        if not url.startswith('URL'):
            break
        
        # Convert to DESKTOP
        url_file = open(file_path, 'w')
        url_file.write('[Desktop Entry]\n')
        url_file.write('Encoding=UTF-8\n')
        url_file.write(f'Name={filename}\n')
        url_file.write('Type=Link\n')
        url_file.write(url)
        url_file.write('Icon=text-html\n')
        url_file.close()

        # Rename the file from .url to .desktop
        os.rename(file_path, f'{os.path.join(os.path.dirname(file_path),filename)}.desktop')