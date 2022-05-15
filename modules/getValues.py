operators = ['+', '-', '*', '/', '^']
choice = str(input(''))

class getValues():

    def get():
        for get in choice:
            if(get in operators):
                signal = get
        
        a = choice.replace(signal, ' ').split()[0]
        b = choice.replace(signal, ' ').split()[1]
        a = int(a)
        b = int(b)

        return a, b

    def getSignal():
        for get in choice:
            if(get in operators):
                signal = get

        return signal