# Calculadora versão 2 criado por JeffeVargasP


from modules import clearPrompt, operations, getValues, memory

a = getValues.getValues.get()[0]
b = getValues.getValues.get()[1]
signal = getValues.getValues.getSignal()
operators = ['+', '-', '*', '/', '^']
clear = clearPrompt.clearPrompt.getSys()
controller = False

class main():

    def calc():

        while True:

            clear
            callFunct = {'+': operations.operations.sum(a,b), '-': operations.operations.sub(a,b),
                        '*': operations.operations.mul(a,b), '/': operations.operations.div(a,b),
                        '^': operations.operations.elv(a,b)}

            result = callFunct[signal]


            print(f'Resultado: {result}')
            input('')
            clearPrompt.clearPrompt.getSys()
            memory.calcMemory.mem(result)
            break
            


if __name__:
    main.calc()
