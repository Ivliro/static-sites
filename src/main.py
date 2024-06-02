import os
import shutil

from copystatic import copy_recursive
from generate_page import generate_page, generate_pages_recursive

def main():
    print('deleting public')
    if os.path.exists('./public'):
        shutil.rmtree('./public')

    print('copy static into public')
    copy_recursive("./static",'./public')

    #generate_page('./content/index.md','./template.html','./public/index.html')
    generate_pages_recursive('./content','./template.html','./public')
    
main()