import os
import shutil

from copystatic import copy_recursive

def main():
    print('deleting public')
    if os.path.exists('./public'):
        shutil.rmtree('./public')

    print('copy static into public')
    copy_recursive("./static",'./public')

main()