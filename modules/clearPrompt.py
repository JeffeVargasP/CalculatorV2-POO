import os, sys

class clearPrompt():

    def getSys():

        getSystem = sys.platform
        
        if ('win' in getSystem):

            os.system('cls')

        else:

            os.system('clear')