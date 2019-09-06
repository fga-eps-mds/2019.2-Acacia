## Introdução
A arquitetura de software é uma abordagem usada no desevolvimento do software para auxiliar no direcionamento da equipe de trabalho de um projeto. Ela é uma abstração de um sistema que seleciona alguns detalhes e busca representá-los em um certo nível de abstração. A importância de adotar padrões arquiteturais pode vir a auxiliar em ganhos de eficiência na manutenção, evolução e agilidade. 

De acordo com [Bass, 2003](http://www.scielo.br/scielo.php?script=sci_arttext&pid=S1807-17752006000100003), a arquitetura de software de um programa ou de um sistema computacional é a estrutura ou as estruturas do sistema, que compreende elementos de software, as propriedades visíveis e externas desses elementos, e as relações entre eles. 

Complementar à este autor, [Krafzig, 2004](http://www.scielo.br/scielo.php?script=sci_arttext&pid=S1807-17752006000100003) define a arquitetura de software como um conjunto de declarações, que descreve os componentes de software e atribui funcionalidades de sistema para cada um deles. Ela descreve a estrutura técnica, limitações e características dos componentes, bem como as interfaces entre eles. Por este processo descrever as partes de um sistema, é possível esboçar o esqueleto do sistema e, por isso, tornar-se o plano de mais alto-nível da construção de cada novo sistema. 

## Metodologia

O primeiro passo dado pela equipe do projeto foi avaliar as potenciais tecnologias a serem usadas no projeto de desenvolvimento do produto proposto. Para cumprir este objetivo, foram feitos estudos que buscaram averiguar a viabilidade em usar as tecnologias previamente selecionadas, por meio de artigos e pesquisas de mercado. As tecnologias selecionadas previamente para o back-end foi Django-Rest, já para o front-end foram os frameworks Vue.js e React.

Após a prévia seleção a escolha consistiu na avaliação dos seguintes tópicos:
- Qual é o nível da curva de aprendizado?
- Qual é a familiaridade da equipe de desenvolvimento com as tecnologias?
- Qual é a relação entre o deadline de entrega do produto com a curva de aprendizado?

## Resultados obtidos

Após análise dos tópicos de avaliação de tecnologias, foi possível então averiguar que para o front-end a opção de tecnologia mais viável é a Vue.js e para back-end Django-rest. A seguir apresenta-se suas análises.

#### Resultados obtidos

1. **Curva de aprendizado**: Pelas fontes pesquisadas sobre as tecnologias, Vue mostrou-se com uma curva de aprendizado menor, em relação à React [[1]](https://medium.com/fundbox-engineering/react-vs-vue-vs-angular-163f1ae7be56) e [[2]]((https://deliciousbrains.com/react-vs-vue-2018/)). Em relação ao back-end, Django tem uma curva de aprendizado mais alta em relação a Flask [[3]](https://imasters.com.br/back-end/flask-x-django-como-escolher-o-framework-correto-para-seu-aplicativo-web), por exemplo. Apesar disto, os membros têm noções básicas do framework e de python.
2. **Familiaridade com as tecnologias**: De acordo com o quadro de conhecimentos atual, a equipe tem familiaridade com Python e pelos membros da equipe já terem conhecimento do padrão arquitetural MVC, possibilitando um back-end mais prático e produtivo. Já no front-end, não há conhecimentos consideráveis de Javascript. Apesar disto, será uma grande chance de aprendizado para todos do grupo de trabalhar com uma tecnologia em tendência no mercado de trabalho.
3. **Curva de aprendizado x Tempo**: Devido a imprevistos e definição tardia do tema a ser desenvolvido, o deadline está corrido. Logo, é importante que as tecnologias usadas tenham uma curva de aprendizado menor, com o objetivo de trabalhar a produtividade da equipe.

### Conclusão

Após análise dos fatores descritos na seção anterior, o cenário de desenvolvimento usando estas tecnologias é positivo. Apesar de Vue.js não ser um framework que a equipe domina, é possível equilibrar com o uso do Django, que usa python, sendo mais acessível para os integrantes de acordo com o quadro de conhecimento. 

## Referências

BASS, Len; CLEMENTS, Paul; KAZMAN, Rick. Software architecture in practice. Addison-Wesley Professional, 2003.

KRAFZIG, Dirk et al. Service-Oriented Architecture Best Practices. Indiana: Prentice Hall PTR, 2004.

[React vs Vue](https://medium.com/fundbox-engineering/react-vs-vue-vs-angular-163f1ae7be56)

[React vs Vue updated](https://deliciousbrains.com/react-vs-vue-2018/)

[The status of JavaScript libraries & frameworks](https://medium.com/hackernoon/the-status-of-javascript-libraries-frameworks-2018-beyond-3a5a7cae7513)

[Django vs Flask](https://imasters.com.br/back-end/flask-x-django-como-escolher-o-framework-correto-para-seu-aplicativo-web)