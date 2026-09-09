# **Git CheatSheet From Beginner To Pro**

## Git Setup
- `git config --global user.name "Your Name"`
- `git config --global user.email "your@gmail.com"`

## Daily workflow
- `git status -> this helps to see what have change`
- `git add . -> stage everything `
- `git add file.py -> stage a specific file`
- `git commit -m "message" -> A message to keep you and your team mates posted about changes made`
- `git log --online -> check your commit history`

## Branches  Checks
- `git branch  -> List branches availabel`
- `git branch new  -> create a new branch`
- `git checkout -b new  -> switch to new`
- `git merge new  -> join the new to the main branch`

## Remote Commands
- `git remote -v  -> helps you see your github link`
- `git push -> upload a repo/file on github`
- `git pull  -> download a repo from github`
- `git clone <url>  -> copy a repo from github`

 ## Undo git commands
- `git restore file.py  -> undo changes before adding`
- `git reset file.py  ->  unstage after adding`
- `git reset --hard HEAD  -> delete all local changes (careful!)`
- `git revert <commit-id>  -> safe undo of a commit`