#!C:\webDev\pycharm\update_mycology_db\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pudb==2019.1','console_scripts','pudb3'
__requires__ = 'pudb==2019.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pudb==2019.1', 'console_scripts', 'pudb3')()
    )
