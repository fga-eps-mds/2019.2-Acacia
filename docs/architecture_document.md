# Documento de arquitetura

## Histórico de revisão
 Data   | Versão | Modificação  | Autor  |
| :- | :- | :- | :- |
| 10/09/2019 | 0.1 | Adição do tópico Objetivo |  Durval Carvalho |
| 10/09/2019 | 0.2 | Adição do tópico Escopo e Django REST Framework |  Durval Carvalho |
| 11/09/2019 | 0.3 | Adição do tópico Metas e Restrições arquiteturais |  Durval Carvalho |
| 12/09/2019 | 0.4 | Adição de tópico Casos de Uso | Renato Britto Araújo |
| 12/09/2019 | 0.5 | Adição do tópico MTV |  Durval Carvalho |
| 12/09/2019 | 0.6 | Adição de diagrama de pacotes back-end e informações sobre base de dados | Renato Britto Araujo | 
| 12/09/2019 | 0.7 | Adição de diagrama de pacotes front-end e referências e comentário sobre MTV | Renato Britto Araujo |
| 12/09/2019 | 0.8 | Adição do tópico Banco de Dados |  Durval Carvalho |
| 12/09/2019 | 0.9 | Adição do informação sobre o super usuário |  Durval Carvalho |
| 12/09/2019 | 1.0 | Adição do tópico Vue.js | João Pedro Silva de Carvalho |
| 12/09/2019 | 1.1 | Adição do tópico Diagrama de classes e serviços | Flavio Vieira |

## 1. Introdução

### 1.1 Objetivo
Este documento oferece uma visão geral arquitetural do 
sitema que será implementado, permitindo assim que os 
envolvidos no projeto conheça como a aplicação será 
subdivida e quais será a função de cada componente.

Outro objetivo desse documento é elucidar quais foram as 
motivações que levaram a equipe a tomar decisões à respeito
dessa arquitetura.

### 1.2 Escopo

Esse documento aplica-se ao projeto <Nome do Projeto>, um 
sistema que será desenvolvido pelos alunos das disciplinas 
Métodos de Desenvolvimento de Software e Engenharia de 
Produto de Software, da Universidade de Brasília - Campus 
Gama.

### 1.3 Definições, Acrônimos e Abreviações

| **Sigla/Termo/Acrônimo** | **Definição** |
| ------------------------ | ------------- |
| MDS | Métodos de Desenvolvimento de <i>Software</i> | 
| EPS | Engenharia de Produto de <i>Software</i> | 
| FGA | Faculdade do Gama | 
| UnB | Universidade de Brasília | 
| DRF | Django Rest Framework |
| MTV | Model Template View |
| MVC | Model View Controller |

## 2. Representação arquitetural

### 2.1 Django REST Framework

O Django REST Framework é uma biblioteca para o Framework 
Django que disponibiliza funcionalidades para implementar 
APIs Rest de forma rápida e eficiente.

REST é a abreviação do termo <i>Representational State 
Transfer</i>, isto é, um conjunto de princípios e boas 
práticas desenvolvido pelo pesquisador Roy Fielding, que 
quando aplicados permite uma interface concisa que pode 
ser utilizado por diversas outras aplicações.

Como explicado acima o DRF é um framework do framework 
Django. Então primeiro explicaremos o motivo de termos 
escolhido Django para o back-end desse projeto.

#### 2.2.1 Django

O Django é um framework web criado com a linguagem Python, que 
utiliza o padrão model-template-view. Esse modelo MTV é basedo 
no modelo Model-View-Controler, com a diferença que as 
responsabilidades do módulo de Controller está dispersa no 
próprio Framework.

Outro motivo do uso do Django é sua robustez. O framework 
possui diversos módulos embutidos que aumenta a 
produtividade da equipe no decorrer do projeto. Os 2 
principais módulos que pode ser citado é o 
Mapeador objeto-relacional (OMR) que irá facilitar a vida 
dos desenvolvedores que não tiverem afinidade em SQL, e o 
painel administrativo que irá de forma visual criar, 
deletar, editar e visualizar objetos do banco de dados.

#### 2.2.2 Modelo MTV

A **Model** é a camada de acesso dos dados. Nessa camada contém 
as classes que abstraem os dados, as lógicas de validação, de 
filtro e de acesso.

O **View** é a camada da regras de negócios. Nessa camada será 
implementada as restrições, o que um usuário pode ou não pode 
fazer, e quais páginas eles tem acesso. É através dessa camada 
que as requisições do usuário será gerenciada.

Essa camada implementa algumas funções do Controller do padrão 
MVC, porém o MTV se diferencia de MVC por ser mais permissivo
quanto a comunicação entre diferentes partes do software 
[[1]](##referências).

O **Template** é a camada de apresentação. Os templates são 
arquivos de texto, que isola os dados do sistema da forma como 
esses dados serão apresentados. O formato mais comum é o HTML.

#### 2.2.3 Django REST
Assim contextualizado, podemos falar sobre o Django REST.
O Django REST possui diversos módulos embutidos que 
facilita a implementação dos princípios e boas práticas 
da arquitetura REST. 

Um exemplo de facilidade é o fato de por padrão as rotas 
dos recursos selecionados serem codificadas para 
respeitar o padrão da arquitetura REST, assim não sendo 
necessário escrever todas as 7 rotas do REST (index, new, 
create, show, edit, update e destroy).

### 2.2 Vue.js
O Vue.js é um framework para a criação de interfaces para o usuário. O Vue.js, desde a sua concepção, busca ser simples e objetivo, o que o torna com uma baixa curva de aprendizagem, ou seja, demora-se menos tempo para uma equipe aprender o Vue.js do que outros frameworks. Além disso, o Vue.js, diferentemente do Angular.js (mantido pela Google) e do React.js (mantido pelo Facebook), possui uma comunidade como sua mantenedora o que permite uma maior interação entre as pessoas que usam e as quem desenvolve esse framework que são beneficiados com mais feedbacks possibilitando melhores atualizações.

Os componentes do Vue.js são uma ferramenta importante. O funcionamento dele se baseia que o desenvolvedor pode separar a página em componentes quem possuem, cada um, seu próprio código em JavaScript, HTML e CSS, permitindo assim a reutilização dessas estruturas em outras partes da aplicação.

Uma das características mais distintas do Vue é seu sistema de reatividade não obstrusivo. Os modelos dados são simplesmente objetos JavaScript puros e quando você os modifica, a camada visual se atualiza. Isto torna o gerenciamento de estado simples e intuitivo. Em comparação com o JavaScript puro ou até mesmo o jQuery, utilizar a reatividade do Vue é bem mais simples.


## 3. Metas e Restrições arquiteturais

3.1 **Suportabilidade**

A aplicação poderá ser utilizada sem grandes problemas 
pelos principais navegadores modernos da atualizada, no 
entanto o enfoque será para o Google Chrome, tanto sua 
versão desktop quanto sua versão mobile, e o Safari, 
navegador padrão dos sistemas da Apple.

3.2 **Usabilidade**

O sistema deverá ser intuitivo e de simples uso, de forma 
que a curva de aprendizado para utilizar a aplicação não 
seja um impedimento para usar o sistema.

3.3 **Ferramentas de Desenvolvimento**

O projeto será desenvolvido em Python (versão 3.7), 
utilizando o framework Django (versão 2.2), em conjunto 
com o framework Vue, um framework JavaScript para criação 
de interfaces e aplicativos. 

Para facilitar a portabilidade do projeto, tanto para o 
ambiente de deploy quanto para os ambientes de 
desenvolvimento, será utilizado o <i>Docker</i> para 
realizar o empacotamento da aplicação.

3.4 **Confiabilidade**

O sistema terá uma cobertura mínima de testes de 90%, 
buscando garantir que suas funcionalidades foram 
suficientemente testadas.

## 4. Visão de Casos de Uso

Segue a lista de casos de uso:

- Criar colheita
- Comunicar com time de colheita
- Registrar árvores
- Registrar conta
- Registrar propriedade
- Selecionar voluntários
- Ver dados de todas as colheitas
- Ver lista de colheitas
- Voluntariar para colheita

### 4.1 Casos de Uso significantes para a arquitetura

![](https://i.imgur.com/V8oJ2z4.png)

Esse diagrama expõe os seguintes requisitos: 

- RF01: Permitir que o usuário faça cadastro e autenticação.
- RF03: Permitir cadastro de árvores, propriedades e colheitas.
- RF04: Permitir usuários se candidatar a colheita.
- RF05: Habilitar comunicação entre envolvidos em colheita (voluntários, líderes e proprietários). 
- RF08: Prover à líderes a possiblidade de escolher voluntários cadastrados em colheita.
- RF09 Mostrar dados à respeito de colheitas realizadas de forma transparente.

## 5. Visão Lógica
[Descrever uma visão lógica da arquitetura. Descrever as classes mais importantes, sua organização em pacotes de serviços e subsistemas. Diagramas de classes e sequência devem ser incluídos para ilustrar os relacionamentos entre as classes significativas na arquitetura, subsistemas, pacotes e camadas. Descrever também a relação de Vue.js com Django Rest no contexto do projeto e descrição breve dos pacotes.]

### 5.1 Diagrama de relações
[Relação macro dos componentes.]

### 5.2 Diagrama de pacotes
#### 5.2.1 _Back-end_

![](https://user-images.githubusercontent.com/45462822/64872015-c55ac780-d61c-11e9-90af-f77668dd10f6.png)

#### 5.2.2 _Front-end_

![](https://i.imgur.com/IOVK3p5.png)

## 6. Visão de implementação

### 6.1 Diagrama de classes e serviços

O diagrama de classe é uma representação estática para descrever 
a estrutura de um projeto, tem como objetivo principal documentar 
de formar visual, as fases de desenvolvimento do software. Com 
isso, e possível mapear/ilustrar de forma clara e objetiva a 
estrutura do software em nível macro e auxiliar no entendimento do 
escopo do projeto.

Na elaboração do diagrama de classe, foi utilizado a Linguagem de 
Modelagem Unificada, ou UML. Ao analisarmos o problema, foi 
levantando os principais componentes e comportamentos, para 
abstrairmos as classes, montar as associações e levantar as
cardinalidades.

Principais componentes do diagrama de classes:

Classes ou entidades; 
Associações ou relações;
Atributos ou campos;
Metodos;
Multiplicidade ou cadinalidade

### 6.2 Banco de Dados

Para os desenvolvimento do diagrama do banco de dados primeiro foi 
identificado quais seriam as entidades envolvidas no projeto. Após 
identificadas, foram analisado qual os atributos necessários para 
descrever uma instância de cada uma das entidades.

Assim que todas as entidades foram descritas, foi analisado quais 
seriam as relações entre elas, e suas respectivas cardinalidades.

O resultado desse passos são descritos abaixo.

#### 6.2.1 Entidades

* USUARIO
	* VOLUNTARIO
	* PROPRIETARIO
	* BENEFICIARIO
	* ADMINISTRADOR
* PROPRIEDADE
* COLHEITA

Um ponto a comentar é a relação especificação da entidade usuário.
O usuário representa qualquer perfil que tenha acesso as áreas do 
site que precisa de autenticação.

A especificação foi utilizada para reduzir o número de auto 
relacionamentos, melhorando assim o entendimento do projeto.

Vale ressaltar que a especificação da entidade usuário não 
impossibilita que um perfil de proprietário realize ações do perfil 
de voluntário, e vice-versa.

O perfil do admnistrador será o usuário responsável por 
administrar todos os dados do site. Esse será o <i>useruser</i> do 
Django. Ele poderá criar, editar e apagar qualquer dado que 
presente na aplicação.

Uma função importante do admnistrador é aprovar os eventos 
colheitas que os proprietários irão criar. Ele será responsável 
por não permitir que eventos suspeitos apareçam para os 
voluntários. 

Como por exemplo, imagine que um proprietário cadastre uma 
plantação com 10000 árvores e esteja solicitando 10000 voluntários.
Será função do administrador recusar esse evento.

Outro exemplo, é um proprietário que cadastre 20 árvores e 
solicite somente 1 voluntário. Será função do admnistrador entrar 
em contato com o proprietário e verificar os detalhes dessa 
colheita.

#### 6.2.2 Atributos

Qualquer **USUARIO** da aplicação, e isso inclui os voluntários, 
proprietários e beneficiários, irão ter um **nome**, um **email**, 
**senhas** e poderão cadastrar telefones para contato.

Um **VOLUNTARIO** deverá cadastrar sua **data de nascimento**, 
para que assim seja possível gerenciar voluntários menores de 
idade e seus responsáveis.

Um **PROPRIETARIO** deverá cadastrar o seu **cpf**, para que seja 
possível verificar se a propriedade que está cadastro realmente é 
de sua posse.

Uma **PROPRIEDADE** deve ter cadastrado o seu **endereço**, 
especificando o país, **estado**, **cidade**, **bairro**, 
**quadra**, **numero** e **complemento**, quando aplicável.

Também deverá especificar as **árvores** dessa propriedade, 
especificando o **fruto**, **mes da colheita**, **se precisa de 
escada para a colheita**, **se é necessário entrar na propriedade 
para ter acesso à árvore** (muros, cercas, cachorros, 
unicórnios alados,...) e também deverá conter **fotos**, tanto da 
propriedade quanto das árvores.

Uma **COLHEITA** deve ter cadastrado a sua **data agendada**, a 
**quantidade de voluntários necessários**, a **quantidade de 
voluntários cadastrados para essa colheita**, a **quantidade 
arrecadada**, a **descrição** do evento, a **situação** (já 
finalizada, agendada, cancelada, ...) e se o **proprietário estará 
presente** no dia.

#### 6.2.2 Relacionamentos

Um **voluntário** pode trabalhar em várias **colheitas**, e em uma 
**colheita** pode trabalhar vários **voluntários**. 
**Cardinalidade: N:M**

Um **voluntário** pode liderar vários **voluntários**, mas um 
**voluntário** só pode ter 1 líder. 
**Cardinalidade: N:M**

Um **voluntário** pode ser responsável por vários **voluntários**, 
mas um **voluntário** só pode ter 1 responsável. 
**Cardinalidade: 1:N**

Um **colheita** ocorre em uma **propriedade** e em uma 
**propriedade** pode ocorre várias **colheitas**.
**Cardinalidade: N:1**

Um **proprietário** pode possuir várias **propriedades**, mas uma 
**propriedade** só pode ser de um **proprietário**.
**Cardinalidade: 1:N**

Um **colheita** pode ser doada para vários **beneficiários**, e um 
**beneficiário** pode receber várias **colheitas**.
**Cardinalidade: N:M**

#### 6.2.3 Diagrama Entidade-Relacionamento
![](img/diagrama_entidade_relacionamento.png)

#### 6.2.4 Diagrama Lógico de Dados
![](img/diagrama_logico_de_dados.png)

## Referências

Departamento de Informática do SUS. Documento de Arquitetura de Software. Disponível em: <https://datasus.saude.gov.br/images/MDSF/MDSoftware/Artefatos/Arquitetura/MDS_DAS_Documento_Arquitetura_Software2.docx>. Acesso em: 10 de setembro de 2019.

[1] - Andrew Pinkham. Livro. Disponível em: <https://django-unleashed.com>. Acesso em: 12 de setembro de 2019.
