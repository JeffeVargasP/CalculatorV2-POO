from modules import clearPrompt, operations

operators = ['+', '-', '*', '/', '^', '**']

class calcMemory():

    def mem(result):

        while True:
            
            choice = str(input('Deseja utilizar o resultado? [S/n] ')).lower()
            
            if (choice == 's'):

                memory = str(input(f'{result}'))
                clearPrompt.clearPrompt.getSys()
                for get in memory:
                    if (get in operators):
                        signal = get

                c = memory.replace(signal, ' ').split()[0]
                c = int(c)

                callFunct2 = {'+': operations.operations.sum(result,c), '-': operations.operations.sub(result,c),
                        '*': operations.operations.mul(result,c), '/': operations.operations.div(result,c),
                        '^': operations.operations.elv(result,c)}

                result = callFunct2[signal]
                print(f'Resultado: {result}')
                input('')
                clearPrompt.clearPrompt.getSys()
                
            else:
                break
