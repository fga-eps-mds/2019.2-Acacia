# Documento de arquitetura

## Histórico de revisão
 Data   | Versão | Modificação  | Autor  |
| :- | :- | :- | :- |
| 10/09/2019 | 0.1 | Adição do tópico Objetivo |  Durval Carvalho |
| 10/09/2019 | 0.2 | Adição do tópico Escopo e Django REST Framework |  Durval Carvalho |

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

## 2. Representação arquitetural

### 2.1 Django REST Framework

O Django REST Framework é uma biblioteca para o Framework 
Django que disponibiliza funcionalidades para implementar 
APIs Rest de forma rápida.

REST é a abreviação do termo <i>Representational State 
Transfer</i>, isto é, um conjunto de princípios e boas 
práticas desenvolvido pelo pesquisador Roy Fielding, que 
quando aplicados permite uma interface concisa que 
diversas outras aplicações podem utilizar, tanto para 
consumir dados quanto para renderizar telas.

Como explicado acima o DRF é um framework do framework 
Django. Então primeiro explicaremos o motivo de termos 
escolhido Django para o back-end desse projeto.

O Django é o framework web criado com a linguagem Python. 
Uma linguagem que todos da equipe já tiveram contato e em plena ascensão no meio acadêmico e no mercado de trabalho.

Outro motivo do uso do Django é sua robustez. O framework 
possui diversos módulos embutidos que aumenta a 
produtividade da equipe no decorrer do projeto. Os 2 
principais módulos que pode ser citado é o 
Mapeador objeto-relacional (OMR) que irá facilitar a vida 
dos desenvolvedores que não tiverem afinidade em SQL, e o 
painel administrativo que irá de forma visual criar, 
deletar, editar e visualizar objetos do banco de dados.

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

## 3. Restrições e Restrições arquiteturais
[Esta seção descrever os requisitos de software e restrições que tem um impacto significante na arquitetura.]

## 4. Visão de Casos de Uso
[Esta seção lista as especificações centrais e significantes para a arquitetura do sistema em relação aos atores da aplicação.]

### 4.1 Casos de Uso significantes para a arquitetura
[Desenhar o diagrama de caso de uso relevante, consultar bibliografia sobre casos de uso.]

## 5. Visão Lógica
[Descrever uma visão lógica da arquitetura. Descrever as classes mais importantes, sua organização em pacotes de serviços e subsistemas. Diagramas de classes e sequência devem ser incluídos para ilustrar os relacionamentos entre as classes significativas na arquitetura, subsistemas, pacotes e camadas. Descrever também a relação de Vue.js com Django Rest no contexto do projeto e descrição breve dos pacotes.]

### 5.1 Diagrama de relações
[Relação macro dos componentes.]

### 5.2 Diagrama de pacotes
[Basta uma imagem do diagrama nos tópicos abaixo.]
#### 5.2.1 _Back-end_

#### 5.2.2 _Front-end_


## 6. Visão de implementação


### 6.1 Diagrama de classes e serviços

### 6.2 Diagrama do banco de dados


## Referências

Departamento de Informática do SUS. Documento de Arquitetura de Software. Disponível em: <datasus.saude.gov.br/images/MDSF/MDSoftware/Artefatos/Arquitetura/MDS_DAS_Documento_Arquitetura_Software2.docx>. Acesso em: 10 de setembro de 2019.
