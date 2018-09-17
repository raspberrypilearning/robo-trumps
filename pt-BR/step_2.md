## Ler dados do robô de um arquivo

Geralmente é útil poder ler informações de um arquivo. Você pode alterar os dados no arquivo sem precisar alterar seu código.

+ Abra este trinket: <a href="http://trinket.io/python/8485e01af6" target="_blank">trinket.io/python/8485e01af6</a>.

+ Seu projeto inicial inclui um arquivo `cartas.txt` que contém dados sobre os robôs. Será necessário alterar o nome deste arquivo para cartas.txt.
    
    Clique em `cartas.txt` para ver os dados:
    
    ![screenshot](images/robotrumps-cards.png)
    
    Em cada linha há dados sobre um robô. Os dados são separados por vírgulas.
    
    Cada linha contém as seguintes informações:
    
    Nome, classificação de inteligência, quanto tempo dura a bateria, nome do arquivo de imagem

+ Vamos ler os dados do arquivo para que você possa usá-lo.
    
    O primeiro passo é abrir o arquivo `cartas.txt` no seu script:
    
    ![screenshot](images/robotrumps-open.png)

+ Agora você pode ler os dados do arquivo:
    
    ![screenshot](images/robotrumps-read.png)

+ Você deve sempre fechar um arquivo quando terminá-lo:
    
    ![screenshot](images/robotrumps-close.png)

+ Isso nos dá o arquivo como uma string, você precisa dividi-lo em partes individuais de dados.
    
    Primeiro, você pode dividir o arquivo em uma lista de linhas:
    
    ![screenshot](images/robotrumps-lines.png)
    
    Olhe atentamente para a saída. Existem três itens na lista, cada um é uma linha do arquivo.

+ Agora você pode passar por cima dessas linhas uma de cada vez
    
    ![screenshot](images/robotrumps-loop.png)

+ Em vez de imprimir as linhas, leia-as para as variáveis:
    
    ![screenshot](images/robotrumps-variables.png)

+ Você quer poder usar esses dados mais tarde para procurar os valores de um determinado robô. Vamos usar o nome do robô como chave para um dicionário.
    
    Adicione um dicionário `robos`:
    
    ![screenshot](images/robotrumps-dict.png)

+ Agora vamos adicionar uma entrada ao dicionário 'robos' para cada robô.
    
    O nome é a chave e o valor é uma lista de dados para esse robô.
    
    Adicione o código destacado:
    
    ![screenshot](images/robotrumps-data.png)
    
    Você pode remover o comando `print(robos)` depois de testar o seu script.