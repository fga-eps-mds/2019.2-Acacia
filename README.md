<p align="center">  <img src="img/wordmark_1.svg" width="400"></p>

## Visão geral

Acácia propõe-se a facilitar a criação de uma comunidade voluntária em torno da agricultura urbana, diminuindo o desperdício de comida e difundindo conhecimento em plantio e colheita neste ambiente. Para tal, a ferramenta conecta pessoas que possuem plantas frutíferas em local urbano, voluntários de colheita e beneficiários que buscam doações de alimentos, para que estes possam trabalhar juntos, com colheita colaborativa.

Este repositório tem como objetivo o desenvolvimento, a manutenção e a evolução do produto nomeado **Acácia**, uma aplicação web, que segue o conceito [Mobile first](https://digitalks.com.br/artigos/mobile-first-e-o-que-voce-realmente-precisa-saber-respeito/) e tem o intuito de auxiliar no processo de colheita colaborativa em áreas urbanas. Ele é baseado em um sistema já existente, o [Saskatoon](https://github.com/tiagovaz/saskatoon) utilizado pelo coletivo [LES FRUITS DÉFENDUS](https://santropolroulant.org/en/what-is-the-roulant/collectives/fruits-defendus/) em Montreal - que facilita a relação entre proprietários de árvores frutíferas, voluntários para colheita e beneficiários das doações dessas frutas, visando a redução do desperdício de comida.

  

## Como contribuir

  

Para contribuir com este projeto basta seguir:

-  [Guia de Contribuição](https://fga-eps-mds.github.io/2019.2-Acacia/#/contributing) 

-  [Código de Conduta](https://fga-eps-mds.github.io/2019.2-Acacia/#/code-of-conduct)

-  [Guia de Instalação](#guia-de-instalação)

-  [Políticas de Contribuição](https://fga-eps-mds.github.io/2019.2-Acacia/#/policies)

-  [Template para criação de issues](https://github.com/fga-eps-mds/2019.2-Acacia/tree/develop/.github/ISSUE_TEMPLATE)

-  [Template para criação de pull requests](https://github.com/fga-eps-mds/2019.2-Acacia/blob/develop/.github/PULL_REQUEST_TEMPLATE.md)

  

## Guia de Instalação

  

Essa aplicação tem seu ambiente configurado através de conteiners [Docker](https://www.docker.com), portanto, tem como pré-requisitos a instalação do [Docker](https://www.docker.com/get-started) e [Docker-compose](https://docs.docker.com/compose/install/).

Também é necessário ter o [Git](https://git-scm.com) instalado para clonar o repositório.

  

#### Back-end:

Clonar o repositório:

  

`git clone https://github.com/fga-eps-mds/2019.2-Acacia.git`

  

Execução do conteiner:

  

`docker-compose up`

  

Após esses passos a aplicação deverá estar acessível em:

  

`localhost:8080`

  

#### Front-end:

Para instalar a camada front-end da aplicação basta seguir os passos de instalação descritos [aqui](https://github.com/fga-eps-mds/2019.2-Acacia-Frontend)