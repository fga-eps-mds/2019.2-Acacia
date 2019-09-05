# Histórico de Revisão
| Data   | Versão | Modificação  | Autor  |
| :- | :- | :- | :- |
| 30/08/2019 | 0.1 | Criação da estrutura do documento |  Durval Carvalho |
| 31/08/2019 | 0.2 | Adição dos tópico Introdução, Propósito, Escopo, Definições, acrônimos e abreviações e Visão Geral |  Durval Carvalho |
| 01/09/2019 | 0.3 | Adição dos tópico Posicionamento, Oportunidade de negócios, Descrição do problema |  Durval Carvalho 
| 02/09/2019 | 0.4 | Adição dos Envolvidos e dos Usuários, atualização do layout da Descrição do Problema  | Renato Britto Araujo |
| 02/09/2019 | 0.5 | Adição dos tópicos Recursos do Produto, Restrições | Durval Carvalho |
| 02/09/2019 | 0.6 | Adição da Visão geral do Produto, Perspectiva do Produto, Resumo das capacidades, Funções do Produto, Suposições e dependências | Leonardo da Silva Gomes |
| 03/09/2019 | 0.7 | Adição dos tópicos Faixas de Qualidade, Requisitos e Descrição do posição do produto | Durval Carvalho |
| 03/09/2019 | 0.7.1 | Revisão dos tópicos Propósito, Visão Geral, Descrição do posição do produto, Principais Necessidades dos Usuários e dos Envolvidos, Alternativas e Concorrências, Resumo das capacidades | Durval Carvalho |
| 03/09/2019 | 0.7.2 | Revisão gramatical e estrutural de todo o documento | Renato Britto Araujo, Leonardo da Silva Gomes |
| 04/09/2019 | 0.8 | Adição do escopo do projeto | João Pedro Silva de Carvalho |
| 05/09/2019 | 0.8.1 | União dos tópicos Introdução e Propósito; Adição das Referências no final do documento; Remoção do termo aplicativo para o termo aplicação web responsiva  | Durval Carvalho e Flavio Vieira |

## **1. Introdução**

Este documento estará repleto de dados que sustentarão o propósito, 
o contexto e a visão geral do produto, permitindo assim o entendimento do 
escopo do projeto.

Assim, será explicado o problema evidenciado, a oportunidade encontrada, a 
descrição dos principais envolvidos, uma possível solução, suas principais 
funcionalidades e seus requisitos. Para assim obter uma melhor compreensão 
do escopo e diminuir os riscos envolvidos.

### 1.1 Escopo

Esse projeto tem como objetivo auxiliar os integrantes do projeto 
Saskatoon que promovem a mobilização de voluntários para ajudarem 
a donos de plantações frutífera a fazerem suas colheitas. 
O software, que tem a função de gerenciar essa mobilização fazendo 
uma comunicação entre os participantes desse projeto, será uma 
aplicação web responsiva. Com isso o software contribuiria com o 
Saskatoon para ajudar no não disperdício de comida e promover uma 
alimentação mais saudável, que são parte dos Objetivos de 
Desenvolvimento Sustentável (ODS) definidos pela ONU.

### 1.2 Definições, acrônimos e abreviações
Estarão listadas neste tópico as definições, acrônimos e abreviações dos 
termos usados neste documento, para assim facilitar o compreendimento do 
público interessado no projeto

| **Sigla/Termo/Acrônimo** | **Definição** |
| ------------------------ | ------------- |
| Saskatoon | Sistema de gerenciamento de colheita desenvolvido pelo Les Fruits Défendus | 
| Santropol Roulant | Centro comunitário de alimentos situado em Montreal| 
| Les Fruits Défendus | Projeto de colheita urbana voluntária organizada pela Santropol Roulant | 
| ODS | Objetivos de Desenvolvimento Sustentável | 
| MDS | Métodos de Desenvolvimento de <i>Software</i> | 
| EPS | Engenharia de Produto de <i>Software</i> | 
| FGA | Faculdade do Gama | 
| UnB | Universidade de Brasília | 


### 1.3 Visão Geral

Este documento visa descrever os detalhes sobre as características 
do software a ser implementado. 
O documento é dividido da seguinte maneira: inicialmente, é 
explorado uma visão geral de todo o documento, exposição do 
problema que este projeto busca resolver e a descrição da parte 
interessada.

Logo após, foram expostos os recursos necessários, restrições e a 
descrição do desempenho do produto. Por fim, foram denominados os 
requisitos necessários para a realização do projeto.

Desta forma, a ideia principal deste documento de visão é fornecer 
de maneira objetiva e organizada os assuntos que tangem à 
problemática inicial.

## **2. Posicionamento**


A organização [Santropol Roulant](https://santropolroulant.org/en/history/) 
foi criada com a missão de diminuir o isolamento social e econômico entre 
jovens e idosos por meio da produção, preparo e distribuição de alimentos.

A partir dessa visão, diversos programas são desenvolvidos e apoiados com o 
objetivo de  produzir, adquirir, preparar e distribuir alimentos, 
principalmente orgânicos.

Um dos programa é o Les Fruits Défendus, que tem como objetivo 
conectar proprietários de árvores frutíferas locais com colheitores 
voluntarios para garantir que esses alimentos não sejam desperdiçados.

### 2.1 Oportunidade de negócios

Com base na visão do programa Les Fruits Défendus e na visão da 
organização mãe Santropol Roulant, foi identificado a oportunidade 
de aumentar o engajamento dos proprietários de plantações 
frutíferas e dos voluntários por meio de uma aplicação web 
responsiva, onde usuários podem acessar pode meio de computadores e 
smartphones.

Essas plataformas digitais se propõe a aumentar a transparência das 
atividades que serão realizadas, a facilitar a difusão das ideias por trás 
do projeto e facilitar o primeiro contato com o projeto.

### 2.2 Descrição do problema

| O problema é | que afeta | cujo impacto é | uma boa solução seria | 
| ------------ | --------- | -------------- | --------------------- | 
| O desperdício de alimentos produzido por árvores frutíferas locais | as pessoas e organizações que não tem acesso à comida orgânica | o consumo de alimentos não nutritivos danosos a saúde | convencer proprietários de árvores frutíferas locais à permitir a colheita e distribuição da produção excedente de frutos |


### 2.3 Descrição do posição do produto

O produto uma vez desenvolvido, poderá se posicionar no mercado 
como uma plataforma online de fácil utilização capaz de engajar 
voluntários para realizar diversas tarefas que beneficiam a 
comunidade local. Podendo assim chamar atenção de pessoas e 
empresas que buscam se associar com a imagem sustentável no 
produto criado.

## **3. Descrição dos Envolvidos e dos Usuários**

### 3.1 Resumo dos Envolvidos

| Nome | Descrição | Responsabilidade |
| :- | :- | :- |
| Avaliadores | Professores das disciplinas de MDS e EPS | Avaliar a qualidade do projeto desenvolvido pelos alunos de MDS e EPS |
| Desenvolvedores | Estudantes da Disciplina MDS da UnB FGA | Criar e manter documentos; Desenvolver e testar o software |
| Equipe de Engenharia de Produto | Estudantes da Disciplina EPS da UnB FGA | Criar e manter documentos; Gerenciar os desenvolvedores; Tomada de decisões a respeito do produto |

### 3.2 Descrição dos Usuários

| Nome | Descrição |
| :--- | :-------- |
| Beneficiários | Instituições recebedoras de doações da colheita |
| Líderes de colheita | Escolhe e gerencia voluntários, recolhe equipamento necessário para colheita e entrega-o junto à doação para <i>Les Fruits Défendus</i> |
| Proprietários de árvores | Cadastram sua(s) proriedade(s) e suas respectivas árvores, candidatam terreno para colheita voluntária com a condição de doar parte dos frutos para a <i>Les Fruits Défendus</i> |
| Voluntários de colheita | Se candidatam a participar de colheitas |

### 3.3 Principais Necessidades dos Usuários e dos Envolvidos

| Usuário | Necessidade | Solução Atual | Solução Proposta |
| :------ | :---------- | :------------ | :--------------- |
| Beneficiário | Doações de alimentos | Doações de pessoas e de ONGs | Website para se candidatar a receber doação |
| Líder de colheita | Interesse em forteceler comunidade local e/ou trabalho voluntário | Participação de coletivos, de OGNs e ações de iniciativa individual | Aplicação web responsiva para se candidatar à colheitas requisitadas pela comunidade local. |
| Proprietário de árvores | Receber ajuda em colheita e/ou interesse em forteceler comunidade local | Ações coletivas organizada pela Les Fruits Défendus | Aplicação web responsiva para cadastrar plantações que podem ser colheitas e doadas para outras organizações |
| Voluntário de colheita | Interesse em forteceler comunidade local e/ou trabalho voluntário | Participação de coletivos, de OGNs e ações de iniciativa individual | Aplicação web responsiva para se candidatar à trabalho voluntário e receber informações à respeito de suas colheitas |

### 3.4 Ambiente dos Usuários

Os usuários poderão utilizar a aplicação por meio de navegadores desktop e 
mobile.

### 3.5 Perfis dos Envolvidos

#### 3.5.1 Equipe de Desenvolvimento de <i>Software</i>

| Representantes | Tipo | Responsabilidade | Critério de sucesso | Envolvimento |
| -------------- | ---- | ---------------- | ------------------- | ------------ |
| Durval Carvalho de Souza, Flávio Vieira, Hugo Sobral de Lima Salomão,	João Pedro Silva de Carvalho, Leonardo da Silva Gomes, Renato Britto Araújo | Estudantes de MDS na UnB FGA | Criar e manter documentos; Desenvolver e testar o software | Completar o projeto proposto dentro do período estipulado e atendendo à todos os requisitos | Alto |

#### 3.5.2 Equipe de Engenharia de Produto de <i>Software</i> 

| Representantes | Tipo | Responsabilidade | Critério de sucesso | Envolvimento |
| -------------- | ---- | ---------------- | ------------------- | ------------ |
| Fabíola Malta Fleury, Martha Dantas Silva, Shayane Marques Alcântara, Vítor Cardoso Xoteslem | Estudantes de EPS na UnB FGA | Criar e manter documentos; Gerenciar os desenvolvedores; Tomada de decisões a respeito do <i>stack</i> de tecnologias | Completar o projeto proposto dentro do período estipulado e atendendo à todos os requisitos | Alto |

#### 3.5.3 Avaliadores

| Representantes | Tipo | Responsabilidade | Critério de sucesso | Envolvimento |
| -------------- | ---- | ---------------- | ------------------- | ------------ |
| Carla Rocha, Joenio Marques da Costa | Professores de EPS e MDS na UnB FGA | Avaliar qualidade do projeto criado | Transmitir conhecimento sobre projetos de <i>software</i> em grupo | Baixo |

### 3.6 Perfis dos Usuários

#### 3.6.1 Beneficiários

| Representantes | Tipo | Responsabilidade | Critério de sucesso | Envolvimento |
| -------------- | ---- | ---------------- | ------------------- | ------------ |
| Instituições | Instituições de auxílio a idosos/orfanatos | Se candidatar a receber doação, checar informações sobre colheitas | Conseguir doações de forma a suprir sua demanda de comida | Baixo |

#### 3.6.2 Líderes de colheita

| Representantes | Tipo | Responsabilidade | Critério de sucesso | Envolvimento |
| -------------- | ---- | ---------------- | ------------------- | ------------ |
| Entusiastas/interessados em trabalho voluntário | Líderes de colheita | Escolhe e gerência voluntários, recolhe equipamento necessário para colheita e entrega-o junto à doação para <i>Les Fruits Défendus</i> | Completar colheitas com sucesso | Alto |

#### 3.6.3 Proprietários de árvores

| Representantes | Tipo | Responsabilidade | Critério de sucesso | Envolvimento |
| -------------- | ---- | ---------------- | ------------------- | ------------ |
| Donos de propriedade urbana com árvores frutíferas | Proprietários de árvores dispostos a ajudar a comunidade e/ou incapacitados para realizar colheita | Disponibilizar sua propriedade para colheita e parte de seus frutos para a <i>Les Fruits Défendus</i> | Conseguir ajuda na colheita de suas árvores | Alto |

#### 3.6.4 Voluntário de colheita

| Representantes | Tipo | Responsabilidade | Critério de sucesso | Envolvimento |
| -------------- | ---- | ---------------- | ------------------- | ------------ |
| Entusiastas/interessados em trabalho voluntário | Pessoas com porte físico capaz de auxiliar colheita | Se candidatar a participar de colheita, comparecer ao evento e seguir ordens do líder de colheita | Participar em colheita | Médio |

### 3.8 Alternativas e Concorrências

#### 3.8.1 Saskatoon

O Saskatoon ([Repositório](https://github.com/tiagovaz/saskatoon), 
[Website](https://saskatoon.lesfruitsdefendus.org/)) é um projeto 
desenvolvido pelo coletivo Les Fruits Défendus com o objetivo de 
fomentar o senso de comunidade e facilitar o processo de fazer 
colheita coletiva para todos os usuários. Porém este projeto 
possui baixo engajamento da comunidade que o desenvolve e baixa 
aderência de novos colaboradores. Devido principalmente 
à sua falta de documentação e a utilização de tecnologias que 
serão descontinuadas, como o Python 2.7.

## **4. Visão geral do Produto**
 
### 4.1 Perspectiva do Produto
 
O projeto visa ser um facilitador no processo de Colheita Colaborativa em áreas urbanas, fomentando a agricultura urbana e a agroecologia que interfere fortemente em vários aspectos sociais e econômicos. Assim, utilizamos da relação entre proprietários de árvores frutíferas, voluntários para colheita e locais que possam receber doações destas frutas, para a diminuição de desperdício de comida, aumento do acesso a comida saudável e colaboração comunitária (socialização) acarretando na diminuição de transtornos mentais e fortalecimento de culturas locais. O produto é baseado em um sistema já existente,  o [Saskatoon](https://github.com/tiagovaz/saskatoon) utilizado pelo coletivo [LES FRUITS DÉFENDUS](https://santropolroulant.org/en/what-is-the-roulant/collectives/fruits-defendus/) em Montreal, uma iniciativa da organização [Santropol Roulant](https://santropolroulant.org/en/history/).
 
### 4.2 Resumo das capacidades
 
| Benefício para o Usuário | Recursos de suporte |
|:------------------------:|:-------------------:|
| Facilidade em se voluntariar | A aplicação disponibiliza uma interface de fácil entendimento onde os voluntários poderão visualizar todos os futuros eventos e se inscrever de acordo com sua aptidão. |
| Facilidade para visualizar o impacto de ações voluntárias na comunidade local | A partir das informações coletadas durante e após as ações coletivas, qualquer pessoa interessada no projeto poderá visualizar o impacto gerado pelo projeto, como quantidade de alimentos arrecadados e organizações beneficiadas |
| Facilidade em cadastrar um novo evento colaborativo | A aplicação irá estimular que proprietários de plantações locais criem novos eventos colaborativos em suas propriedades uma vez que visualizarem o impacto positivo gerado por ações anteriores.
 
### 4.3 Funções do Produto
 
O projeto está encarregado de ser o conectivo entre os proprietários de árvores e os voluntários, facilitando o processo de colaboração. A plataforma agrega diversas funcionalidades como cadastro, gerenciamento,  inscrição no projeto, etc.
 
### 4.4 Suposições e dependências
 
- O usuário deverá possuir um celular ou um computador com acesso à internet para acessar a aplicação.
 
- A aplicação web responsiva será utilizada por pessoas que desejam se voluntariar e pessoas que querem ajudar na colheita de seus frutos.
 
- A aplicação web responsiva irá facilitar a comunicação entre proprietário da árvore frutífera e o voluntário.

### 4.5 Custo e precificação
### 4.6 Licenciamento e instalação
### 4.7 Instalação

## **5. Recursos do Produto**

### 5.1 Recursos de suporte ao voluntário

Os voluntários que tiverem interessados no projeto podem se cadastrar na 
plataforma. Quando logados terão acesso aos seguintes recursos: 
* Histórico de colheitas que participaram.
* Organizações ou pessoas que foram beneficiadas com os alimentos coletados na colheita em que o voluntário estava presente.
* Próximas colheitas que podem se voluntariar.
* Vincular-se a uma colheita cadastrada

### 5.2 Recursos de suporte ao proprietário

Os proprietários de árvores frutíferas locais que tiverem interesse no 
projeto podem se cadastrar na plataforma. Quando logados terão acesso ao:

* Cadastro de plantações disponível para colheita
* Histórico de colheitas realizadas em suas propriedades.
* Organizações ou pessoas que foram beneficiadas com os alimentos coletados em sua propriedade.

### 5.3 Disponibilizar os resultados das últimas colheitas

Qualquer pessoa interessada no projeto terá acesso aos paineis de 
informação. Nessa parte da aplicação não será necessário autenticação do 
usuário e qualquer pessoa terá acesso aos dados das últimas colheitas, o 
destino dos frutos colhidos e informações sobre o projeto.

### 5.4 Enviar email para grupos cadastrados
 
A aplicação poderá enviar email para os usuários de acordo com as atividades 
que estão se aproximando. Esses emails serão enviados automaticamente de 
acordo com o contexto do usuário. Esses emails são:

5.4.1 Para os proprietários
* Sua plantação atingiu o número de voluntários necessários
* Sua plantação não atingiu o número de voluntários necessários
* A data de colheita está próxima

5.4.2 Para os voluntários
* A colheita que você está escrito atingiu o número de voluntários necessários
* A colheita que você está escrito não atingiu o número de voluntários necessários
* A colheita que você está escrito está próxima

## **6. Restrições**

Listagem de restrições externas e outras dependências:

* Conexão com a Internet.
* O projeto deve ser finalizado até o prazo limite 17/12/19.
* Foco para aprender novas tecnologias.
* Conhecimento básico de Inglês.

### 6.1 Restrições de Implementação
O sistema será implementado utilizando 2 principais frameworks, sendo eles
o Django Rest para o back-end e o Vue JS para o front-end.

### 6.2 Restrições externas
Dentre as restrições externas as que mais irão influenciar são a 
inexperiência com o framework Django, além de possíveis 
transtornos entre a equipe de desenvolvimento e de gerência.

### 6.3 Restrições de Design
É necessário que os usuários tenham acesso à internet para poder utilizar o 
software.

### 6.4 Restrições de Confiabilidade
Visando uma maior mantenabilidade do projeto pela comunidade open source, 
esse projeto tem o comprometimento de manter uma cobertura de testes de no 
mínimo 90%, para assim produzir um produto melhor.

## **7. Faixas de Qualidade**

Toda da interação com o software deve ocorrer de forma natural, de modo que 
o usuário não fique com dúvidas sobre como realizar determinada tarefa.

Os recursos que cada usuário tem acesso deve ser fácil entendimento, de modo 
que o usuário não desista durante alguma ação.

Com a finalidade de alcançar um público maior de usuários, a aplicação será 
desenvolvida tanto para o ambiente web quanto para smartphones.

## **8. Requisitos do Produto**

### 8.1 Requisitos do Sistema

Essa aplicação poderá ser acessada por meio dos principais navegadores web. 

### 8.2 Requisitos de Design

A aplicação deve ser auto explicativa, de forma que, o usuário não precise 
recorrer a canais de suporte para realizar alguma ação. Deste modo, toda os 
fluxos de uso devem ser pensados de modo que o resultado seja intuitivo e 
fácil de usar.

### 8.3 Requisitos de Portabilidade

O sistema deve ter suporte para principais navegadores web atuais, além de 
ser compatível com as últimas versões do Android.

### 8.4 Requisitos de Confiabilidade

A aplicação deve ser comprometer com os dados dos usuários cadastrados, de 
modo que informações sensíveis não seja comprometidas. 

### 8.1 Requisitos de Suportabilidade
O software desenvolvido deve ser compatível com os principais navegadores e 
smartphones modernos

### 8.2 Requisitos de Design
A aplicação deve ter uma interface que seja de fácil uso para pessoas. Dessa 
forma, será necessário uma interface intuitiva pensando na experiência do 
usuário.

### 8.3 Requisitos de Segurança
O sistema deve garantir a integridade dos dados fornecidos pelos usuários

### 8.4 Requisitos de Desempenho
O sistema deve ser otimizado de forma que usuários com conexões lentas 
recebam resposta de forma satisfatória.

## Referências
- Texto descritivo sobre a estrutura e objetivo dos tópicos do documento de visão. https://www.ibm.com/support/knowledgecenter/pt-br/SSWMEQ_4.0.6/com.ibm.rational.rrm.help.doc/topics/r_vision_doc.html. Acesso em 02 de setembro de 2019

- História da Santropol Roulant. Disponível em https://santropolroulant.org/en/history/. Acesso em 01 de setembro de 2019.

- Programas desenvolvidos pela Santropol Roulant. Disponível em https://santropolroulant.org/en/what-is-the-roulant/#block_cross. Acesso em 01 de setembro de 2019

- Projeto Les Fruits Défendus. Disponível em https://santropolroulant.org/en/what-is-the-roulant/collectives/fruits-defendus/. Acesso em 01 de setembro de 2019