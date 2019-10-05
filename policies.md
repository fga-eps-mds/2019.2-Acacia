# Políticas do Repositório
## Histórico de versão

| Data | Versão | Modificação | Autor |
| :- | :- | :- | :- |
| 23/08/2019 | 1.0 | Criação da primeira versão do documento | Vítor Cardoso |
| 03/09/2019 | 1.1 | Tradução do documento para português | Vítor Cardoso |

## Introdução

Este documento tem como objetivo  explicar os procedimentos a serem feitos para que as políticas deste repositório sejam seguidas adequadamente.

Aqui se encontram:

- Política de Branch
- Política de Commits

## Políticas de Branch

Branches devem seguir as seguintes regras explicadas neste tópico:

Breve explicação sobre o fluxo de trabalho:

- A branch **master** representa uma versão estável do produto, contendo código já testado e versionado, pronto para ser entregue ao usuário final ou cliente. Essa branch parte da branch **develop** através de pull requests aprovados no fim de cada release.

  Regras:

  1. Existe apenas uma branch **master**.
  2. **Não** são permitidos commits feitos diretamente na **master**.


- A branch **develop** contém a versão mais atualizada do código que está sendo desenvolvido. Essa branch está sempre sincronizada com a **master** e é base para as branches **feature**.

  Regras:

  1. Existe apenas uma branch **develop**.
  2. Essa branch está sempre sincronizada com a branch **master**.


- As branches **feature** representam as funcionalidades do sistema a serem desenvolvidas, elas devem ter a branch **develop** como sua origem e fim.

  Regras:

  1. Essa branch sempre é criada a partir da branch **develop**.
  2. Essa branch sempre é mesclada à branch **develop**.

  Regras de nomenclatura:

  `feature/issueID-titulo-da-issue`


- A branch **release** representa o conjunto de funcionalidades provenientes de um ponto específico da branch **develop**. Essa branch contém funcionalidades prontas que, provavelmente, estarão presentes na próxima versão estável do produto. Apenas **bug fixes** são permitidos nessa branch.

  Regras:

  1. Essa branch sempre é criada a partir da branch **develop**.
  2. Essa branch sempre é mesclada às branches **develop** e **master**.
  3. Essa branch aceita apenas mesclagens de branches do tipo **bugfix**.

  Regras de nomenclatura:

  `release/vNúmero-da-versão`




- As branches do tipo **bugfix** são utilizadas para implementar soluções para bugs, encontrados através de testes realizados em releases específicas, na branch **release**. Isso significa que a branch **bugfix** deve ter a branch **release** como sua origem e fim.

  Regras:

  1. Essa branch sempre é criada a partir da branch **release**.
  2. Essa branch sempre é mesclada na branch **release**.

  Regras de nomenclatura:

  `bugfix/issueID-titulo-da-issue`



  A branch **hotfix** é utilizada para implementar soluções para problemas urgentes encontrados no ambiente de produção. Isso significa que essa branch deve ter a branch **master** como sua orgigem e fim.


- Regras:

  1. Essa branch sempre é criada a partir da branch **master**.
2. Essa branch sempre é mesclada à branch **master**.

  Regras de nomenclatura:

  `hotfix/issueID-titulo-da-issue`




Observações: O título da issue utilizado no nome das branches deve ser mantido em português.


 Imagens para ajudar a visualizar o fluxo de trabalho descrito:

  ![](https://fpy.cz/pub/slides/git-workshop/images/gitflow.png)

  ![](https://miro.medium.com/max/640/0*FTwKYpFGADX-5Y0O)

## Políticas de Commits
Commits devem ser escritos de forma clara e breve, em Inglês, descrevendo as alterações feitas.

Regras para escrita das mensagens nos commits:

``` 
#issueID Mensagem breve descrevendo alterações
	
Mensagem mais detalhada sobre o que foi feito neste commit. (Opcional)
```

É possível fechar uma issue automaticamente adicionando a palavra chave "Fix" antes do id da issue:

`Fix #issueID Concise Message`

O caractere "#", por padrão, representa uma linha de comentário no arquivo de mensagem do commit. Para evitar problemas, é necessário alterar o caractere com o seguinte comando:

`git config --local core.commentChar auto`

Caso deseje utilizar um outro caractere específico para definir uma linha de comentário, basta substituir a palavra "auto" pelo caractere desejado.

A mensagem principal do commit deve ser escrita no modo imperativo. Aqui estão alguns exemplos:

Maus exemplos:

`Renamed the iVars and removed the common prefix.`

`Creating branch policies document `

Bons exemplos:

`Rename the iVars to remove the common prefix. `

`Create branch policies document`


## Referências

[Git-flow Applied to a Real Project](https://medium.com/empathyco/git-flow-applied-to-a-real-project-c08037e28f88)

[Writing git commit message](https://365git.tumblr.com/post/3308646748/writing-git-commit-messages)
