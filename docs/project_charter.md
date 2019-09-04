# Termo de abertura

# 1. Introdução

Este documento inicia formalmente o projeto do Sistema de Colheita Colaborativa. Nas próximas sessões são detalhados: o que este projeto visa realizar, a oportunidade de negócio identificada, o escopo de atuação, os envolvidos (*stakeholders*), características de riscos, restrições e de custos, entregáveis, prazos e as ferramentas utilizadas no processo de desenvolvimento. Tais descrições visam elucidar a viabilidade do projeto.

# 2. Descrição do Projeto

O projeto visa auxiliar no processo de Colheita Colaborativa em áreas urbanas, facilitando a relação entre proprietários de árvores frutíferas, voluntários para colheita e  locais que possam receber doações destas frutas, visando então a diminuição do desperdício de comida. Ele é baseado em um sistema já existente, o [Saskatoon](https://github.com/tiagovaz/saskatoon) utilizado pelo coletivo [LES FRUITS DÉFENDUS](https://santropolroulant.org/en/what-is-the-roulant/collectives/fruits-defendus/) em Montreal.


# 3. Propósito do Projeto

Este projeto possui como objetivos:

-   Auxiliar na diminuição do desperdício de comida
-   Aumentar o acesso a comida local
-   Facilitar a disseminação de conhecimento de colheita e plantio de árvores frutíferas urbanas
- Facilitar o conhecimento de feiras e troca de conhecimento entre produtores de agricultura familiar e urbana


# 4. Oportunidade de Negócios

No texto dos Objetivos de Desenvolvimento Sustentável (ODS) da [ONU](https://nacoesunidas.org/pos2015/agenda2030/)  coloca-se a importância da erradicação da pobreza é um grande e importante desafio global para o desenvolvimento sustentável. 

Observa-se ainda, no [ODS 2](https://nacoesunidas.org/pos2015/ods2/) - Fome zero e Agricultura Sustentável a necessidade de: "*Acabar com a fome, alcançar a segurança alimentar e melhoria da nutrição e promover a agricultura sustentável* ". E, no [ODS 11] - Cidades e Comunidades sustentáveis(https://nacoesunidas.org/pos2015/ods11/), "Tornar as cidades e os assentamentos humanos inclusivos, seguros, resilientes e sustentáveis". 

Desta forma, uma das possíveis soluções é o fomento da agricultura urbana. A agricultura urbana permite a valorização de espaços limitados permitindo a construção de laços de vida comunitário por meio da produção de alimentos voltados para o autoconsumo, assim também diversificando a dieta de famílias. Desta forma, diminui-se os riscos de insegurança alimentar e nutricional e permite a comunidade desenvolver-se de forma sustentável e autogerida [1][2].


O projeto [Saskatoon](https://github.com/tiagovaz/saskatoon) está inserido neste contexto da agricultura urbana, em Montreal. Embora a agricultura urbana seja também desenvolvida no Brasil, principalmente em  áreas com populações socialmente marginalizadas [2], ainda não foi identificado pela equipe um produto que auxilie na gerência de colheita colaborativa ou distribuição de produtos agrícolas destes grupos ou para divulgação de feiras de produção familiar e troca de conhecimentos sobre plantio e colheita. 

# 5. Escopo do Projeto

Plataforma web responsiva, troca de informações entre pessoas em relação a agricultura urbana

# 6. Equipe e Papéis

## 6.1. Envolvidos

A equipe é compostas por alunos da disciplina de Métodos de Desenvolvimento de Software (MDS) e Engenharia de Produto de Software (EPS) responsáveis por diferentes papéis,  sendo os membros de MDS alocados em papéis de desenvolvimento e os estudantes de EPS em papéis de gerência  descritos a seguir em tabela.

| Papel | Responsabilidade | Estudante |
| :---: | :--------------: | :-----------: |
| Desenvolvedor | O desenvolvedor tem como papel desenvolver, testar, garantir a qualidade e entrega do produto |Hugo Sobral de Lima Salomão, Durval Carvalho de Souza, João Pedro Silva de Carvalho, Leonardo da Silva Gomes, Renato Britto Araújo|
| DevOps | Responsável pela configuração dos diferentes ambiente necessários do projetos tais como de desenvolvimento, de homologação e de produção, assim como automatização de testes, integração e deploy e entrega contínua. | Vitor Cardoso Xoteslem |
| Arquiteto de Software | No contexto da disciplina, atuará de maneira a analisar se a arquitetura de microserviços é viável para o projeto e dará suporte para as atividades do DevOps. |Shayane Marques Alcântara|
| Scrum Master | É um facilitador da equipe, responsável por retirar possíveis impedimentos que possam comprometer o andamento do projeto. |Martha Dantas Silva |
| Product Owner | Responsável por passar a visão do produto para a equipe, assim como priorizar a ordem de desenvolvimento do sistema de acordo com as necessidades elicitadas. |Fabíola Malta Fleury |

Além destes, existem outros envolvidos:

 - Consultor de visão de produto: O mantenedor do projeto [Saskatoon](https://github.com/tiagovaz/saskatoon), Tiago Vaz, está familiarizado com o seu contexto e seus funcionários e está disponível para auxiliar no desenvolvimento do projeto, embora não possa participar presencialmente
 - Professora: Possui como objetivo auxiliar o desenvolvimento do projeto para que os estudantes conheçam e pratiquem definições necessárias para o cumprimento do plano de ensino das disciplinas.

## 6.2. Usuários

| Nome| Descrição |
| :---: | :-----------------------:  |
| Agricultores urbanos| Donos de plantações que disponibilizarão seu plantio para que seja realizada a colheita. |
| Voluntários de colheita| Pessoas que disponibilizam ao menos duas horas para realizar a colheita.|
|Líderes de colheita|Pessoas que já possuem experiência na colheita, são responsáveis pela escolha dos voluntários e trabalham em conjunto com eles.|
|Beneficiários| Entidades que recebem a parcela da comida como doação|

# 7. Metodologia de Desenvolvimento

O processo do desenvolvimento deste projeto é baseado nas metodologias ágeis do Lean, Scrum e XP (eXtreme Programming). São utilizadas conforme o contexto da disciplina, com espaço para adaptações à necessidades da equipe.


# 8. Prazo e Custo

O projeto terá uma duração de um total de 16 sprints. A primeira sprint teve inicio no dia 13 de Agosto de 2019, de maneira que a última sprint será iniciada no dia  25 de novembro de 2019, totalizando 4 meses de duração de projeto. Durante esse período, haverão duas datas de entregas importantes, sendo elas denominadas releases. Uma ocorrerá na Sprint 7, que inicia-se dia 30 de setembro, enquanto outra ocorrerá na Sprint 16, a partir do dia 25 de novembro. 


O custo do projeto foi calculado utilizando os seguintes valores, em reais:

| Nome | Custo | Quantidade | Custo Mensal | Custo Total |
| :--: | :---: | :--------: | :----------: | :---------: |
| Desenvolvedores Júnior | 3500 | 6 | 21.000 | 84.000|
| Engenheiros de Produto  | 6500 | 4 | 26.000 | 104.000 |
| ΔRisco  | 5.000 | - | 5.000 | 20.000 |
| |||| 174.000|

Os valores para os salários foram obtidos a partir de salários de pessoas que exercem cargos semelhantes em Brasília. O custo do risco é equivalente ao salário médio da equipe. Leva-se consideração ainda, além do custo, uma margem de lucro de 10%, totalizando então em **R$191.400,00** o custo do projeto.

# 9. Estratégia de Comunicação

Para comunicação interna da equipe são utilizados: o aplicativo Telegram, Hangouts, aulas e reuniões presenciais.

Para comunicação com outros envolvidos são utilizados e-mails, hangouts e o github.


# Referências

[1] ALMEIDA, Daniela. Agricultura urbana e segurança alimentar em Belo Horizonte: cultivando uma cidade sustentável. **Revista Agriculturas: experiencias em agroecologia.**, v. 1, p. 25-28, 2004.

[2] AQUINO, Adriana María de; ASSIS, Renato Linhares de. Agricultura orgânica em áreas urbanas e periurbanas com base na agroecologia. **Ambiente & sociedade**, v. 10, n. 1, p. 137-150, 2007.
