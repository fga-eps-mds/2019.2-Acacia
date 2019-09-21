| Data   | Versão | Modificação  | Autor  |
| :- | :- | :- | :- |
| 20/09/2019 | 0.1 | Criação da versão inicial do documento | [Shayane Alcântara](https://github.com/shayanealcantara)|
| 20/09/2019 | 0.2 | Adição do estudo em backend | [Shayane Alcântara](https://github.com/shayanealcantara)|


## Introdução
Teste de software é o processo de execução de um produto para determinar se ele atingiu suas especificações e funcionou corretamente no ambiente para o qual foi projetado. O seu objetivo é revelar falhas em um produto, para que as causas dessas  falhas sejam identificadas e possam ser corrigidas pela equipe de desenvolvimento antes da entrega final [[1]](#referencias). 

## Metodologia

O primeiro passo dado pela equipe do projeto foi avaliar as potenciais ferramentas a serem usadas no projeto de desenvolvimento de testes. Para cumprir este objetivo, foram feitos estudos que buscaram averiguar a viabilidade em usar as ferramentas previamente selecionadas, por meio de experiências dos membros e pesquisas de mercado. As ferramentas são específicas para cada tecnologia definida: Vue.js (javascript) e Django Rest Framework (python).

Após a prévia seleção a escolha consistiu na avaliação dos seguintes tópicos:
- A ferramenta possui alto volume de documentação?
- Qual é a familiaridade da equipe de desenvolvimento com as ferramentas?
- Qual é a relação entre o deadline de entrega do produto com o nível de complexidade da ferramenta?

### Front-end

O código a ser testado no front-end estará em Javascript, logo as ferramentas devem ser compatíveis com a linguagem. Para tal foram abordados alguns frameworks interessantes como o [Jest](https://jestjs.io), [Mocha](https://mochajs.org) e [Jasmine](https://jasmine.github.io).

O Jasmine se destaca por ser um framework de testes unitários orientado à comportamento, ou seja, tenta se aproximar ao máximo do comportamento do usuário. Enquanto isso o Mocha se mostra um framework bastante flexível em suas configurações. Já o Jest é uma ferramenta marcada pela facilidade na configuração inicial.

Para testes realização de *end-to-end*, quando necessário, foram abordadas ferramentas como o [Nightwatch.js](https://nightwatchjs.org) e [Cypress](https://www.cypress.io).

#### Guia de estilo

Como já mencionado, a camada front-end da aplicação será feita usando o framework Vue.js, que tem seu próprio [Guia de estilo](https://vuejs.org/v2/style-guide/). Esse guia deverá ser seguido com objetivo de evitar erros, perda de tempo e adoção de anti-padrões.

### Back-end

O código a ser testado no back-end estará em Python, logo as ferramentas devem ser compatíveis com a linguagem. Pela tecnologia ser Django Rest, ela auxilia de certa forma a implementação de testes, visto que descreve em sua documentação oficial uma série de [classes e recursos](https://www.django-rest-framework.org/api-guide/testing/#testing) com este fim, como a APIClient e APITestCase.  

Além deste recurso anterior, foi abordada a biblioteca [Unnitest](https://docs.python.org/3/library/unittest.html#module-unittest) e o [Pytest](https://docs.pytest.org/en/latest/), ambas nativas do Python. Com elas é possível executar testes unitários em massa ou individuais de forma simples, sem a necessidade de instalação de módulos extras. A saída de execução é prática e concisa, podendo gerar relatórios mais detalhados. 

Outra ferramenta abordada foi a [Doctest](https://wiki.python.org.br/DocTest) é uma biblioteca padrão do Python que procura e interpreta docstrings na aplicação. A sintaxe nesses trechos de docstrings é diferenciada, simulando um interpretador interativo do Python [[2]](https://klauslaube.com.br/2011/07/18/ferramentas-de-testes-em-django-parte-1.html).

#### Guia de estilo

O propósito de um guia de estilo é manter a consistência em relação a padrões de escrita do código. Para cumprir este objetivo, será necessário a adoção do [Guia de estilo](https://wiki.python.org.br/GuiaDeEstilo) definido pela comunidade Python, com diretrizes padronizadas.

## Resultados

No Back-end, a opção mais viável para desenvolver os teste é a biblioteca **Unnitest**, em que os testes são escritos através de classes e que utiliza-se os esquemas de assertions para garantir o comportamento do código testado, garantindo certa facilidade e praticidade pela familiaridade com a linguagem e a experiência de alguns membros. Além disso, há um grande volume de [documentação](https://django-portuguese.readthedocs.io/en/1.0/topics/testing.html), o que pode auxiliar no desenvolvimento decorrente do projeto e consequentemente diminuir a complexidade de execução.

No Front-end, a opção mais interessante, levando em conta o prazo e escopo do projeto, é realizar testes unitários utilizando o **Jest**, pois é uma ferramenta de testes completa e ao mesmo tempo de rápida configuração inicial.  
No caso dos testes *end-to-end* a melhor opção é o **Cypress** por conta de sua boa performance e facilidade de configuração.

## Planos futuros

## Referências

[1] NETO, Arilo. Introdução a Teste de Software. Disponível em: <http://www.garcia.pro.br/EngenhariadeSW/artigos%20engsw/teste/teste%20de%20software%20-%20artigo%201%20-%20rev1%20-%20introducao%20a%20teste%20de%20sw.pdf>. Acesso em: 20/09/2019.
  
[2] LAUBE, Klaus. Ferramentas de testes em django. Disponível em: <https://klauslaube.com.br/2011/07/18/ferramentas-de-testes-em-django-parte-1.html>. Acesso em: 20/09/19.