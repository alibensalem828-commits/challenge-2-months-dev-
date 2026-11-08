# Ma Bible Git

Guide pratique pour débutant. Garde-le sous la main.

---

## 1. Les mots à comprendre

| Mot | Ce que c'est |
|---|---|
| **dépôt (repo)** | Ton dossier de projet suivi par Git |
| **commit** | Une sauvegarde datée de ton travail, avec un message |
| **branche** | Une version parallèle de ton code (`main`, `dev`...) |
| **remote** | Un dépôt distant (sur GitHub) |
| **origin** | Le surnom habituel de ton remote principal |
| **push** | Envoyer tes commits vers GitHub |
| **pull** | Récupérer les commits de GitHub vers chez toi |
| **merge** | Fusionner deux branches ensemble |
| **HEAD** | Là où tu te trouves actuellement |

---

## 2. Configuration (une seule fois par machine)

```bash
git config --global user.name "Ton Nom"
git config --global user.email "ton@email.com"
git config --global pull.rebase false        # fusionner par défaut
git config --global init.defaultBranch main  # nommer la branche main
```

Vérifier :
```bash
git config --global --list
```

**Pourquoi ?** Chaque commit porte ton nom et ton email. Sans ça, Git refuse de commiter.

---

## 3. Démarrer un projet

### Cas A — Le projet existe déjà chez toi

```bash
cd mon-projet
git init                    # créer le dépôt local
git add .                   # préparer tous les fichiers
git commit -m "premier commit"
git remote add origin https://github.com/toi/mon-repo.git
git push -u origin main
```

### Cas B — Le projet existe déjà sur GitHub

```bash
git clone https://github.com/toi/mon-repo.git
cd mon-repo
```

`clone` fait tout d'un coup : télécharge, configure `origin`, se place sur `main`.

---

## 4. Le cycle quotidien

C'est 90 % de ton usage de Git :

```bash
git status                       # que s'est-il passé ?
git add .                        # je prépare mes modifs
git commit -m "j'ai fait ceci"   # je sauvegarde
git push                         # j'envoie sur GitHub
```

### Détail des trois zones

```
Répertoire de travail  →  Zone de préparation  →  Dépôt local  →  GitHub
   (tes fichiers)              (staging)           (commits)      (remote)
                        add                 commit            push
```

- `git add fichier.html` — un seul fichier
- `git add .` — tout le dossier courant
- `git restore --staged fichier` — retirer de la préparation

### Bons messages de commit

```bash
git commit -m "ajout du formulaire de contact"    # bien
git commit -m "correction du bug d'affichage"     # bien
git commit -m "modif"                             # inutile
git commit -m "asdf"                              # à éviter
```

---

## 5. Regarder ce qui se passe

```bash
git status              # état actuel
git log                 # historique complet
git log --oneline       # historique compact (le plus utile)
git log --oneline --graph --all   # avec les branches en dessin
git diff                # ce que j'ai modifié sans encore faire add
git diff --staged       # ce qui est préparé mais pas commité
git show <hash>         # détail d'un commit précis
```

Pour sortir de `git log` : appuie sur `q`.

---

## 6. Les branches

```bash
git branch                    # lister les branches
git branch dev                # créer une branche dev
git switch dev                # aller sur dev
git switch -c dev             # créer ET aller dessus (raccourci)
git switch main               # revenir sur main
git branch -d dev             # supprimer dev (une fois fusionnée)
```

### Fusionner une branche

```bash
git switch main       # se placer sur la branche qui reçoit
git merge dev         # y ramener le travail de dev
```

### Pousser une branche locale vers un autre nom distant

```bash
git push -u origin dev:main
```

Traduction : « envoie ma branche locale `dev` vers la branche `main` de `origin`, et mémorise ce lien ». Grâce au `-u`, ensuite un simple `git push` suffira.

---

## 7. Travailler avec GitHub

```bash
git remote -v                                    # voir les remotes configurés
git remote add origin <url>                      # en ajouter un
git remote remove origin                         # en supprimer un
git remote set-url origin <nouvelle-url>         # corriger l'URL
```

**Attention au piège classique :** ne mets jamais de `\` en fin de ligne quand tu colles une URL. Le `\` dit au terminal « la commande continue à la ligne suivante », et il colle donc la ligne d'après à ton URL. C'est ce qui donnait `...git.gitgit`.

### Récupérer et envoyer

```bash
git pull                # récupérer + fusionner
git fetch               # récupérer sans fusionner (pour regarder d'abord)
git push                # envoyer
```

---

## 8. Résoudre les erreurs fréquentes

### « Identité d'auteur inconnue »
```bash
git config --global user.name "Ton Nom"
git config --global user.email "ton@email.com"
```

### « fatal: Pas de destination pour pousser »
Aucun remote n'est configuré :
```bash
git remote add origin https://github.com/toi/repo.git
```

### « 'origin' does not appear to be a git repository »
Le remote n'existe pas ou son URL est cassée :
```bash
git remote -v          # vérifier
git remote remove origin
git remote add origin <bonne-url>
```

### « ! [rejected] ... (fetch first) »
GitHub contient des choses que tu n'as pas (souvent un README créé à la création du repo) :
```bash
git pull origin main --allow-unrelated-histories
git push
```

### « refusing to merge unrelated histories »
Ton dépôt local et celui de GitHub n'ont aucun ancêtre commun :
```bash
git pull origin main --allow-unrelated-histories
```

### « Besoin de spécifier comment réconcilier des branches divergentes »
```bash
git config --global pull.rebase false
```

### « ! [rejected] ... (non-fast-forward) »
Ton local est en retard. Tire d'abord, puis pousse :
```bash
git pull origin main
git push
```

### Un éditeur s'ouvre pendant un merge
C'est normal, Git te demande de valider le message.
- **nano** : `Ctrl+O`, `Entrée`, puis `Ctrl+X`
- **vim** : `Échap`, puis `:wq`, puis `Entrée`

---

## 9. Annuler des choses

```bash
git restore fichier.html          # annuler mes modifs non commitées
git restore --staged fichier      # retirer de la zone de préparation
git commit --amend -m "nouveau"   # corriger le dernier message de commit
git revert <hash>                 # annuler un commit en créant l'inverse (sûr)
git reset --soft HEAD~1           # défaire le dernier commit, garder les fichiers
git reset --hard HEAD~1           # défaire le dernier commit, PERDRE les fichiers
```

`--hard` détruit du travail sans confirmation. À manier avec précaution.

---

## 10. Le fichier .gitignore

Crée un fichier nommé `.gitignore` à la racine du projet pour exclure ce qui ne doit pas être versionné :

```
node_modules/
.env
*.log
.DS_Store
dist/
build/
```

Ne commite **jamais** de mots de passe, de clés d'API, ou de fichiers `.env`.

---

## 11. Fiche mémo

```bash
# Configuration
git config --global user.name "Nom"
git config --global user.email "mail"

# Démarrer
git init
git clone <url>

# Quotidien
git status
git add .
git commit -m "message"
git push
git pull

# Branches
git switch -c ma-branche
git switch main
git merge ma-branche

# Remote
git remote -v
git remote add origin <url>

# Historique
git log --oneline
git diff
```

---

## 12. Le réflexe à garder

Quand quelque chose ne va pas, tape toujours ça en premier :

```bash
git status
```

Git te dit presque toujours où tu en es et ce qu'il te propose de faire. Lis le message en entier avant de chercher ailleurs — la solution y est souvent écrite.
