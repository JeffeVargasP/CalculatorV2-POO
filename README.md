# CalculatorV2-POO
<hr>
<h4>Recriando a calculadora de meu primeiro projeto em python usando Programação Orientada a Objeto, porém tudo está apenas com a lib os e sys para limpar o prompt/terminal, o resto é puro código do zero.</h4>

<h1> UTILIZAÇÃO <h1>
<hr>
<h4> AVISO!!! Este passo a passo só irá funcionar no windows com python instalado e git bash </h4>

<h4>

`git clone git@github.com:JeffeVargasP/CalculatorV2-POO.git`

Caso queira mudar o nome da pasta apenas use este código substituindo as <> e seu conteúdo

`git clone git@github.com:JeffeVargasP/CalculatorV2-POO.git <nome-da-pasta>`

Após isso entre na pasta

`cd <nome-da-pasta>`

A seguir use o que funcionar em seu sistema

`python main.py` ou `python3 main.py`

Isso irá retornar nada em escrito, mas não quer dizer que o programa não funcionou!
Você pode fazer as seguintes operações adição(+), subtração(-), multiplicação(*), divisão(/), potência(^)

`2+2`

Então o código retornará o resultado da soma que é 4.

Em seguida será exibido uma mensagem.

`Deseja utilizar o resultado? [S/n] ` Obs: Entre os colchetes = [], estão as duas possíveis respostas. Não se preocupe com letras maiúscolas ou minúscolas, apenas digite 's' para sim e 'n' para fechar o programa.

Caso você digite 's', o programa irá exibir o número anterior e você colocará o operador seguido do número.

Exemplo: `4*4` Obs: Seguindo a lógica da explicação, o quatro já foi pré-colocado e foram adicionados o operador '*' e o número '4', o número que aparece antes do operador não pode ser apagado, caso deseje alterar, você deve rodar o código novamente.

O resultado será igual à 16!

Essa pergunta se repetirá por quantas vezes você ainda quiser retuilizar o número resultante da conta anterior.

<h2> FAQ </h2>

- Eu posso utilizar mais de um número? na conta? NÃO! Caso você use mais que dois números, o código irá quebrar. Sim, muito chato isso, mas você terá que utilizar sempre a função de memória para adicionar a conta e conhecer um pouco da ordem de precedência.

- Poderia colocar a ordem? Claro!

1. `( )`     --> O que estiver dentro dos parenteses devem ser resolvidos primeiramente.
2.  `^`      --> Após os parenteses deve-se resolver as potências.`
3. `* ou /`  --> Multiplicações e divisões vem após a potência, deve-se resolver quem vier primeiro.
4. `+ ou -`  --> Adição e subtração, novamente, quem vier primeiro será resolvido com preferência.

</h4>