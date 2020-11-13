# IMPORT MODULES FROM SUBFOLDERS #
""" It's neccesary in order to import modules not in the same folder, but in a different one.
This is the way to tell python the location on those subfolders: """
import sys


sys.path.insert(0, '../lowlevel')
# ------------------------------ #

import messages

values = messages.messagesDict.values()

for v in values:
        print v + "\n"


