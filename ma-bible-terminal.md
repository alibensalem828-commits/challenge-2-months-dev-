# Ma Bible Terminal (Linux)

Tout ce qu'il faut pour être à l'aise dans le terminal. À lire et relire.

---

## 0. Comprendre ce que tu vois

Ton invite de commande :

```
➜  defi-de-42j git:(dev) ✗
```

- `➜` — le symbole de ton thème (Oh My Zsh)
- `defi-de-42j` — le dossier où tu te trouves
- `git:(dev)` — tu es dans un dépôt Git, sur la branche `dev`
- `✗` — il y a des modifications non commitées

Quand il n'y a pas de `✗`, ton dossier Git est propre.

### La forme d'une commande

```bash
commande -options arguments
   ls      -l      /home
```

- **options courtes** : une lettre, un tiret → `-l`, `-a`
- **options longues** : un mot, deux tirets → `--all`, `--help`
- On peut les combiner : `ls -l -a` = `ls -la`

---

## 1. Les chemins

| Symbole | Signification |
|---|---|
| `/` | la racine du système |
| `~` | ton dossier personnel (`/home/missingno0`) |
| `.` | le dossier courant |
| `..` | le dossier parent |
| `-` | le dossier précédent |

**Chemin absolu** — part de la racine, marche depuis n'importe où :
```bash
/home/missingno0/ia/vs/defi-de-42j
```

**Chemin relatif** — part d'où tu es :
```bash
../autre-dossier
./mon-script.sh
```

---

## 2. Se déplacer et regarder

```bash
pwd                    # où suis-je ? (print working directory)
ls                     # lister
ls -l                  # format long (droits, taille, date)
ls -lh                 # tailles lisibles (Ko, Mo, Go)
ls -a                  # inclure les fichiers cachés (.git, .env)
ls -la                 # les deux
ls -lt                 # trier par date, plus récent d'abord
ls -lS                 # trier par taille
ls Documents/          # lister un autre dossier

cd Documents           # entrer dans Documents
cd ~/Téléchargements   # aller n'importe où depuis chez toi
cd ..                  # remonter
cd ../..               # remonter deux fois
cd ~                   # rentrer à la maison
cd                     # pareil, tout seul
cd -                   # revenir au dossier précédent

tree                   # arborescence en dessin (sudo apt install tree)
tree -L 2              # limiter à 2 niveaux de profondeur
```

---

## 3. Créer, déplacer, copier, supprimer

```bash
touch fichier.txt              # créer un fichier vide
mkdir mon-dossier              # créer un dossier
mkdir -p projet/src/css        # créer toute l'arborescence d'un coup

cp fichier.txt copie.txt       # copier
cp fichier.txt ~/Documents/    # copier ailleurs
cp -r dossier/ ~/Documents/    # copier un dossier (-r = récursif)
cp -i source dest              # demander avant d'écraser

mv fichier.txt ~/Documents/    # déplacer
mv ancien.txt nouveau.txt      # renommer
mv dossier/ ~/Documents/       # déplacer un dossier (pas besoin de -r)

rm fichier.txt                 # supprimer un fichier
rm -r dossier/                 # supprimer un dossier
rm -i fichier.txt              # demander confirmation
rmdir dossier-vide/            # supprimer un dossier vide seulement
```

> **`rm` ne met rien à la corbeille.** C'est définitif, immédiat, sans confirmation. Ne tape **jamais** `rm -rf /` ni `rm -rf ~`.
>
> Sécurité utile : `alias rm='rm -i'` pour toujours avoir une confirmation.

---

## 4. Les jokers (wildcards)

```bash
*              # n'importe quelle suite de caractères
?              # un seul caractère
[abc]          # a, b ou c
{jpg,png}      # jpg ou png
```

En pratique :

```bash
ls *.pdf                       # tous les PDF
mv *.pdf ~/Documents/pdf/      # déplacer tous les PDF
rm *.log                       # supprimer tous les .log
cp img*.jpg ~/Images/          # tous les fichiers commençant par img
mv *.{jpg,png,gif} ~/Images/   # trois extensions d'un coup
ls fichier?.txt                # fichier1.txt, fichierA.txt...
```

---

## 5. Ouvrir des fichiers

### xdg-open — le double-clic du terminal

**XDG** = X Desktop Group (aujourd'hui freedesktop.org), le standard commun à tous les bureaux Linux.

`xdg-open` ne lit rien lui-même : il regarde le type du fichier, consulte quelle application ton système lui associe, et la lance.

```bash
xdg-open rapport.pdf        # → lecteur PDF
xdg-open photo.jpg          # → visionneuse d'images
xdg-open video.mp4          # → lecteur vidéo
xdg-open page.html          # → navigateur
xdg-open .                  # → explorateur de fichiers sur le dossier courant
xdg-open https://github.com # → navigateur
```

**Crée le raccourci `open` :**
```bash
echo "alias open='xdg-open'" >> ~/.zshrc
source ~/.zshrc
open rapport.pdf
```

### Applications précises

```bash
code fichier.html      # VS Code
code .                 # VS Code sur tout le dossier courant
firefox fichier.pdf    # navigateur
evince fichier.pdf     # lecteur PDF GNOME
eog photo.jpg          # visionneuse d'images GNOME
nautilus .             # explorateur de fichiers GNOME
```

Ajoute `&` à la fin pour rendre la main au terminal : `code . &`

---

## 6. Lire du texte sans quitter le terminal

```bash
cat fichier.txt          # tout afficher d'un coup
cat -n fichier.txt       # avec les numéros de ligne
cat a.txt b.txt          # afficher deux fichiers à la suite

less fichier.txt         # lire page par page
head fichier.txt         # 10 premières lignes
head -30 fichier.txt     # 30 premières lignes
tail fichier.txt         # 10 dernières lignes
tail -30 fichier.txt     # 30 dernières
tail -f app.log          # suivre en direct (Ctrl+C pour arrêter)

wc -l fichier.txt        # compter les lignes
```

### Dans `less`

| Touche | Action |
|---|---|
| `Espace` | page suivante |
| `b` | page précédente |
| `↑` `↓` | ligne par ligne |
| `/mot` | chercher |
| `n` / `N` | occurrence suivante / précédente |
| `g` / `G` | début / fin |
| `q` | **quitter** |

C'est le même `less` que Git utilise pour `git log`. Si tu es bloqué dans un affichage, `q` te sort.

---

## 7. Éditer dans le terminal

### nano — simple, à privilégier

```bash
nano fichier.txt
```

Les raccourcis sont affichés en bas. Le `^` signifie **Ctrl**.

| Raccourci | Action |
|---|---|
| `Ctrl+O` puis `Entrée` | sauvegarder |
| `Ctrl+X` | quitter |
| `Ctrl+W` | chercher |
| `Ctrl+K` | couper la ligne |
| `Ctrl+U` | coller |
| `Ctrl+G` | aide |

### vim — si tu tombes dedans par accident

```
Échap   puis   :q!   puis   Entrée      → sortir sans sauver
Échap   puis   :wq   puis   Entrée      → sauver et sortir
```

### micro — la bonne alternative

```bash
sudo apt install micro
micro fichier.txt
```

Comme nano, mais avec `Ctrl+S`, `Ctrl+C`, `Ctrl+V` comme partout ailleurs. Tu t'y retrouveras probablement mieux.

---

## 8. Chercher

### Chercher des fichiers

```bash
find . -name "*.pdf"              # tous les PDF ici et en dessous
find ~ -name "apprentissage*"     # dans tout ton home
find . -type d -name "css"        # chercher un dossier (-type d)
find . -type f -name "*.html"     # chercher un fichier (-type f)
find . -size +100M                # fichiers de plus de 100 Mo
find . -mtime -7                  # modifiés dans les 7 derniers jours

which python3                     # où est installé un programme ?
```

### Chercher dans le contenu

```bash
grep "mot" fichier.txt            # lignes contenant "mot"
grep -i "mot" fichier.txt         # sans distinction majuscules/minuscules
grep -n "mot" fichier.txt         # avec numéros de ligne
grep -r "mot" .                   # récursif dans tout le dossier
grep -rn "TODO" . --include="*.js"   # dans les .js seulement
grep -v "mot" fichier.txt         # lignes qui NE contiennent PAS
```

---

## 9. Les tubes et redirections

Le **tube** `|` envoie la sortie d'une commande dans l'entrée d'une autre.

```bash
ls -la | less                     # lister page par page
cat gros.log | grep "erreur"      # filtrer
ls | wc -l                        # compter les fichiers
history | grep git                # retrouver mes commandes git
ps aux | grep firefox             # trouver un processus
```

Les **redirections** écrivent dans un fichier :

```bash
ls > liste.txt          # écrire (écrase le contenu existant)
ls >> liste.txt         # ajouter à la fin
commande 2> erreurs.txt # rediriger seulement les erreurs
commande &> tout.txt    # sortie + erreurs
commande > /dev/null    # jeter la sortie (le trou noir du système)
```

---

## 10. Les raccourcis clavier

Ce sont eux qui font la différence entre galérer et être efficace.

| Raccourci | Action |
|---|---|
| **Tab** | **compléter automatiquement** |
| Tab Tab | montrer toutes les possibilités |
| ↑ / ↓ | commandes précédentes |
| `Ctrl+R` | chercher dans l'historique |
| `Ctrl+C` | interrompre la commande en cours |
| `Ctrl+D` | fermer le terminal |
| `Ctrl+L` | nettoyer l'écran (= `clear`) |
| `Ctrl+A` | début de ligne |
| `Ctrl+E` | fin de ligne |
| `Ctrl+U` | effacer avant le curseur |
| `Ctrl+K` | effacer après le curseur |
| `Ctrl+W` | effacer le mot précédent |
| `Alt+←` `Alt+→` | se déplacer mot par mot |
| `Ctrl+Shift+C` / `Ctrl+Shift+V` | copier / coller |

**Utilise Tab en permanence.** Tape `cd Télé` puis Tab : il complète. Ça évite les fautes de frappe et te confirme que le fichier existe.

`Ctrl+R` puis quelques lettres retrouve n'importe quelle commande déjà tapée.

---

## 11. Les caractères spéciaux (le piège du `\`)

```bash
mv "mon fichier.pdf" ~/Documents/     # guillemets
mv mon\ fichier.pdf ~/Documents/      # ou antislash
```

Le `\` dit « le caractère suivant est littéral, pas spécial ».

**En fin de ligne**, `\` signifie « la commande continue à la ligne suivante ». C'est exactement ce qui t'a piégé avec Git :

```bash
git remote add origin https://github.com/...git\
git push
```
Le terminal a lu ça comme une seule ligne, d'où l'URL `...gitgit`. Ne colle jamais un `\` en fin d'URL.

Autres caractères à connaître :

| Caractère | Rôle |
|---|---|
| `#` | commentaire, le reste de la ligne est ignoré |
| `;` | enchaîner deux commandes |
| `&&` | enchaîner **si la première réussit** |
| `\|\|` | enchaîner **si la première échoue** |
| `&` | lancer en arrière-plan |
| `$` | variable (`$HOME`, `$PATH`) |

```bash
mkdir projet && cd projet      # entrer seulement si la création a marché
```

---

## 12. Droits et permissions

```bash
ls -l
-rw-r--r--  1 missingno0 users  1024 Jul 21 10:30 fichier.txt
```

Décodage de `-rw-r--r--` :

```
-        rw-       r--       r--
type   propriétaire groupe   autres
```

- `r` = lecture (4)
- `w` = écriture (2)
- `x` = exécution (1)
- Premier caractère : `-` fichier, `d` dossier, `l` lien

```bash
chmod +x script.sh          # rendre exécutable
chmod 755 script.sh         # rwxr-xr-x (classique pour un script)
chmod 644 fichier.txt       # rw-r--r-- (classique pour un fichier)
chown moi:moi fichier       # changer le propriétaire
```

**sudo** = exécuter en administrateur. Il demande ton mot de passe (rien ne s'affiche quand tu tapes, c'est normal).

```bash
sudo apt install truc
```

N'utilise `sudo` que quand c'est nécessaire. Jamais pour bidouiller dans ton home.

---

## 13. Installer des logiciels (Ubuntu/Debian)

```bash
sudo apt update                  # rafraîchir la liste des paquets
sudo apt upgrade                 # mettre à jour l'installé
sudo apt install nom-du-paquet   # installer
sudo apt remove nom-du-paquet    # désinstaller
sudo apt search mot              # chercher
```

Quelques outils qui valent le coup :
```bash
sudo apt install tree htop micro curl unzip
```

---

## 14. Système et processus

```bash
htop               # gestionnaire de tâches (q pour quitter)
ps aux             # liste des processus
kill 1234          # arrêter le processus n°1234
killall firefox    # arrêter par nom

df -h              # espace disque libre
du -sh *           # taille de chaque élément du dossier
du -sh dossier/    # taille d'un dossier
free -h            # mémoire RAM

uname -a           # infos système
whoami             # mon nom d'utilisateur
date               # date et heure
uptime             # depuis quand la machine tourne
```

---

## 15. Archives

```bash
zip -r archive.zip dossier/       # compresser en zip
unzip archive.zip                 # décompresser
unzip archive.zip -d destination/ # décompresser ailleurs

tar -czf archive.tar.gz dossier/  # compresser en tar.gz
tar -xzf archive.tar.gz           # décompresser
```

Moyen mnémotechnique : **c**reate, e**x**tract, g**z**ip, **f**ile.

---

## 16. Réseau

```bash
ping google.com              # tester la connexion (Ctrl+C pour arrêter)
curl https://site.com        # afficher le contenu d'une page
curl -O https://site.com/fichier.zip   # télécharger
wget https://site.com/fichier.zip      # télécharger aussi
ip a                         # mes adresses IP
```

---

## 17. Les alias — se simplifier la vie

Un alias est un raccourci que tu crées toi-même. Ils vivent dans `~/.zshrc`.

```bash
nano ~/.zshrc
```

Ajoute à la fin :

```bash
alias open='xdg-open'
alias ll='ls -lah'
alias ..='cd ..'
alias ...='cd ../..'
alias gs='git status'
alias ga='git add .'
alias gc='git commit -m'
alias gp='git push'
alias gl='git log --oneline --graph'
alias c='clear'
```

Puis recharge :
```bash
source ~/.zshrc
```

Désormais `gs` fait `git status`, `open truc.pdf` ouvre ton PDF.

---

## 18. Quand tu es perdu

```bash
commande --help        # aide rapide
man commande           # manuel complet (q pour quitter)
tldr commande          # exemples concrets (sudo apt install tldr)
history                # mes 1000 dernières commandes
```

`tldr` est le plus utile au début : il donne directement des exemples plutôt qu'un manuel de 400 lignes.

---

## 19. Erreurs fréquentes et solutions

| Message | Cause | Solution |
|---|---|---|
| `command not found` | programme non installé ou faute de frappe | `sudo apt install ...` |
| `No such file or directory` | mauvais chemin | `ls` pour vérifier, utilise Tab |
| `Permission denied` | droits insuffisants | `sudo` ou `chmod +x` |
| `Is a directory` | tu traites un dossier comme un fichier | ajoute `-r` |
| `Directory not empty` | `rmdir` sur un dossier plein | `rm -r` |
| Le terminal ne répond plus | commande en cours | `Ctrl+C` |
| Un affichage bizarre bloqué | tu es dans `less` ou `man` | `q` |
| Bloqué dans vim | vim | `Échap` `:q!` `Entrée` |

---

## 20. Les 5 réflexes

1. **Tab** — toujours, pour tout compléter
2. **`pwd` et `ls`** — quand tu ne sais plus où tu es
3. **Lis le message d'erreur en entier** — la solution y est souvent
4. **`Ctrl+C`** — pour sortir de tout ce qui tourne
5. **`q`** — pour sortir de tout ce qui affiche

---

## 21. Fiche mémo

```bash
# Navigation
pwd  ls -lah  cd ~  cd ..  cd -

# Fichiers
touch f.txt   mkdir -p a/b   cp -r src dst   mv a b   rm -r dossier

# Ouvrir
xdg-open f.pdf     code .     nano f.txt     less f.txt

# Lire
cat f.txt   head -20 f   tail -f log   wc -l f

# Chercher
find . -name "*.pdf"      grep -rn "mot" .

# Tubes
ls | wc -l      history | grep git      cat f | less

# Système
htop   df -h   du -sh *   free -h

# Paquets
sudo apt update && sudo apt install truc

# Aide
commande --help    man commande    tldr commande
```

---

## 22. Petit exercice pour tester

```bash
cd ~
mkdir -p test-terminal/docs
cd test-terminal
touch note.txt
nano note.txt              # écris quelque chose, Ctrl+O Entrée Ctrl+X
cat note.txt
cp note.txt docs/
ls -la docs/
mv note.txt docs/note-originale.txt
tree
xdg-open .                 # ton explorateur s'ouvre sur ce dossier
cd ~
rm -r test-terminal
```

Si tu suis ces douze lignes sans hésiter, tu as l'essentiel.
