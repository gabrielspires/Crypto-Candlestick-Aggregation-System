# Documentação

## Problema

Candlesticks são extremamente relevantes na negociação de Bitcoins e criptomoedas como um todo. Aprendendo como funcionam os padrões das candlesticks, você pode sair na frente e agir sobre esses indicadores antes que os outros traders tomem conta.

Como os candlesticks utilizam dados brutos de preços e são atualizados assim que um período é concluído, os padrões dos candlesticks são considerados indicadores do futuro e não do passado. Isso torna o reconhecimento de padrões dos candlesticks uma obrigação se você planeja negociar criptomoedas.

Um candle consiste em quatro valores, _open_, _high_, _low_ e _close_. O valor _open_ se refere ao primeiro valor do período e o valor _close_ ao último valor, enquanto os valores _high_ e _low_ representam o valor mais alto e o mais baixo do período, respectivamente. Este projeto busca valores em tempo real de uma API pública e os salva em memória. Periodicamente, os dados salvos são agregados em candlesticks de 1, 5 ou 15 minutos e salvos em um banco de dados local. O aplicativo roda continuamente, salvando os candlesticks assim que o período é concluído. 


## Decisões de projeto

### Docker

Foram criados dois serviços usando o docker-compose, um deles usa uma imagem padrão do MariaDB e o outro usa uma imagem construída usando a imagem do python 3.8.5, porém o gerenciador de dependências Poetry e as dependencias do projeto são instalados através do dockerfile. No arquivo do docker-compose também é criada uma rede que ambos os serviços usam, isso é útil porque assim os containers conseguem se comunicar através dos hostnames que são sempre iguais e nao precisam usar os endereços de IP que são dinâmicos.

### Poetry

Poetry foi usado para gerenciar as dependencias do projeto porque eu já tinha usado ele em outros projetos e acho prático.

### Banco de dados

Para o banco de dados, optei por usar o MariaDB já que ele é uma versão do MySQL, porém open-source. Todos os comandos são idênticos e as bibliotecas do python feitas pra mysql funcionam com MariaDB sem problemas.

Como esse é um projeto público, optei por usar a opção do mysql que permite que a senha de root do banco fique vazia para facilitar. Em versões privadas caso alguém crie um fork desse projeto e coloque em produção em um banco real sugiro que mude essa opção no arquivo do docker-compose.

### Programação paralela

Existem dois aspectos do sistema que devem rodar o tempo todo, a requisição de dados que chama a api publica da Poloniex e os métodos que criam os candlesticks no final de cada período. Pesquisei algumas formas de rodar código de forma concorrente e acabei optando por utilizar a biblioteca threading por ser mais simples de usar e mais fácil pra fazer os testes, uma vez que ainda não tinha muita experiencia com programação paralela em python. Cada um dos métodos que precisa rodar continuamente chama a si mesmo através do método threading.Timer(). Os métodos que realizam os requests tem um delay de 0.3 segundos cada, uma vez que o máximo de requisições à api é de 6 por segundo, assim cada método realiza no máximo 3 requisições por segundo.

## Possíveis melhorias

~~Um dos principais pontos que eu pretendo melhorar no sistema é deixar ele mais genérico. Atualmente só é possível buscar os dados e criar candles de Bitcoin e Monero. Um jeito de melhorar isso seria buscar os códigos das moedas usando o comando 'returnCurrencies' da api e dar ao usuário a opção de qual moeda usar mostrando os códigos e nomes na tela, ou então passando o código do par no construtor da classe.~~ _Melhoria implementada._

Também gostaria de ter feito os testes de integração, não tenho muita experiência com isso e preferi focar em fazer os testes de unidade.

~~Alguns métodos ficaram um pouco grandes, seria boa prática quebra-los em métodos menores, pretendo fazer isso no futuro.~~ _Melhoria implementada._

## Principais dificuldades

A minha principal dificuldade foi em achar um jeito de fazer as requisições em tempo real, tentei fazer com async mas não consegui fazer do jeito que queria então acabei optando por usar a biblioteca threading. Outra dificuldade foi em achar um jeito bom pra decidir quando fechar as candles. Acabei decidindo usar o módulo time, fechando as candles no último segundo de cada período, não sei se existe um método mais elegante mas assim funcionou bem e de forma consistente.

A parte de testes também foi um ponto de dificuldade, uma vez que não tinha muita experiência com isso. Acabei optando por fazer somente testes de unidade mas pretendo aumentar a cobertura de testes fazendo os testes de integração com o banco.