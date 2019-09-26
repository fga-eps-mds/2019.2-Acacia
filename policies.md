# Repository Policies

## Introduction

This document is intended to explain the procedures to be performed in order to correctly follow this repository policies.

Here you can find our:

- Branch policies
- Commit policies

## Branch Policies

Branches must follow the rules explained in this section and must be written in English. 

Brief work flow explanation:

- The **master** branch represents the stable version of the product, containing tested and versioned code, which is ready to be delivered to the final user or customer. This branch comes from the **develop** branch through pull requests approved at the end of each release.

  Rules:

  1. There is only one **master** branch.

  2. Commits made **directly** in this branch are **not** allowed.

  

- The **develop** branch contains the most updated version of the code we are working on. This branch is always synchronized with the **master** branch and is the base of all **feature** branches.

  Rules:

  1. This branch is always synchronized with the **master** branch.

     

- The **feature** branches represent the system features to be developed, they must have the **develop** branch as both start and end.

  Rules:

  1. This branch always come from the **develop** branch.
  2. This branch is always merged to the **develop** branch.

  Naming rules:

  `feature/issueID-issue-name`

  

- The **release** branch represents a set of features coming from a specific point of the **develop** branch. This branch contains features that will probably be in the next stable release of the product. Only **bug fixes** are allowed in this branch.

  Rules:

  1. This branch always come from the **develop** branch.
  2. This branch is always merged to the **develop** and **master** branches.
  3. This branch only accepts merges from **bugfix** branches.

  Naming rules:

  `release/vVersion-number`

  

- The **bugfix** branches are used to implement solutions to bugs, found through tests applied to specific releases, in the **release** branch. This means that this branch must be started from and merged into a **release** branch.

  Rules:

  1. This branch always come from the **release** branch.
  2. This branch is always merged to the **release** branch.

  Naming rules:

  `bugfix/issueID-issue-name`

  

- The **hotfix** branch is used to implement solutions to urgent bugs found in the live environment. This means that this branch must be started and merged into the **master** branch. 

  Rules:

  1. This branch always come from the **master** branch.
2. This branch is always merged to the **master** branch.

  Naming rules:

  `hotfix/issueID-issue-name`

  

  Here are some images   representing this work flow:

  ![](https://fpy.cz/pub/slides/git-workshop/images/gitflow.png)

  ![](https://miro.medium.com/max/640/0*FTwKYpFGADX-5Y0O)

  ## Commit Policies
Commits should be briefly and clearly written, in English, describing what was done.

Commit writing rules:

``` 
#issueID Concise Message up to 50 characters
	
Optional and more detailed message
```

You can automatically close an issue by adding the keyword "Fix" before the #issueID:

`Fix #issueID Concise Message`

The commit concise message must uses the imperative, present tense. Here are some examples:

Bad examples:

`Renamed the iVars and removed the common prefix.`

`Creating branch policies document `

Good examples:

`Rename the iVars to remove the common prefix. `

`Create branch policies document`



## References

[Git-flow Applied to a Real Project](https://medium.com/empathyco/git-flow-applied-to-a-real-project-c08037e28f88)

[Writing git commit message](https://365git.tumblr.com/post/3308646748/writing-git-commit-messages)

