# Le cours de CSS complet

**Ton manuel de référence.** Tout ce qu'il te faut pour intégrer n'importe quelle maquette, proprement, sans framework.

> **Comment utiliser ce document.** Tu ne le lis pas comme un roman. Tu ouvres VS Code à côté et **tu tapes chaque exemple**. Un module lu sans code tapé = un module non appris. À la fin de chaque module il y a un « À toi » : fais-le avant de passer au suivant.

---

## Sommaire

| # | Module | Pourquoi c'est là |
|---|--------|-------------------|
| 1 | Brancher le CSS et la syntaxe | Les bases matérielles |
| 2 | Les sélecteurs | Viser le bon élément |
| 3 | Cascade, spécificité, héritage | **90 % de tes futurs bugs** |
| 4 | Le box model | La géométrie de tout |
| 5 | Les unités | px, rem, em, %, vw… |
| 6 | Les couleurs | hex, rgb, hsl |
| 7 | La typographie | Ce qui fait « pro » ou « amateur » |
| 8 | `display` | Comment un élément se comporte |
| 9 | **Flexbox** | Le module le plus rentable |
| 10 | **Grid** | Les vraies mises en page |
| 11 | `position` et `z-index` | Superposer, coller, fixer |
| 12 | **Responsive** | Non négociable en 2026 |
| 13 | Les variables CSS | Le CSS maintenable |
| 14 | Transitions, transform, animations | Le vernis qui vend |
| 15 | Ombres, arrondis, dégradés | La finition |
| 16 | Pseudo-classes et pseudo-éléments | `:hover`, `::before`… |
| 17 | Arrière-plans et `overflow` | Images de fond, débordements |
| 18 | Organiser son CSS | Reset, ordre, nommage |
| 19 | Les 12 erreurs de débutant | À relire avant chaque projet |
| 20 | Aide-mémoire | La fiche à garder ouverte |

---

# MODULE 1 — Brancher le CSS et la syntaxe

## Les trois façons de brancher du CSS

```html
<!-- 1. Externe — LA bonne méthode, la seule que tu utilises -->
<link rel="stylesheet" href="style.css">

<!-- 2. Interne — dans le <head>, acceptable pour un test rapide -->
<style>
  p { color: red; }
</style>

<!-- 3. En ligne — à éviter, spécificité énorme, impossible à maintenir -->
<p style="color: red;">Texte</p>
```

Le `<link>` se met dans le `<head>`. Un fichier CSS externe est mis en cache par le navigateur : la deuxième page de ton site charge plus vite. C'est aussi la seule façon de styler 20 pages avec un seul fichier.

## L'anatomie d'une règle

```css
h1 {                      /* h1 = le sélecteur */
  color: navy;            /* color = propriété, navy = valeur */
  font-size: 2rem;        /* le ; est obligatoire à chaque ligne */
}                         /* l'ensemble { } = le bloc de déclaration */
```

Une **déclaration** = `propriété: valeur;`
Une **règle** = sélecteur + bloc de déclarations.

## Les commentaires

```css
/* Ceci est un commentaire CSS */
/* Il n'existe QUE cette syntaxe. Pas de // en CSS. */
```

Sers-t'en pour découper ton fichier en sections :

```css
/* ============ NAVBAR ============ */
/* ============ HERO ============ */
```

## Ce que tu mets en haut de chaque fichier CSS

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
```

Trois lignes qui t'évitent des heures de galère. On explique `box-sizing` au module 4. Les deux premières annulent les marges par défaut incohérentes des navigateurs.

---

# MODULE 2 — Les sélecteurs

Un sélecteur, c'est ta façon de dire « je veux styler **ça** ».

## Les sélecteurs de base

```css
p            { }   /* type : tous les <p> */
.carte       { }   /* classe : tous les éléments class="carte" */
#header      { }   /* id : l'unique élément id="header" */
*            { }   /* universel : absolument tout */
h1, h2, h3   { }   /* groupe : les trois à la fois */
```

**Classe ou id ?** Tu utilises **des classes, presque toujours**. Un id doit être unique dans la page, il a une spécificité énorme (module 3) et il n'est pas réutilisable. Les id servent surtout aux ancres (`#contact`) et au JavaScript. Règle simple : **style = classe, JS et ancres = id**.

Un élément peut porter plusieurs classes :

```html
<button class="btn btn-primaire grand">Envoyer</button>
```

C'est la base des systèmes de design : une classe pour la structure, une pour la variante.

## Les combinateurs (relations entre éléments)

```css
article p      { }   /* descendant : tous les p DANS un article, à tout niveau */
article > p    { }   /* enfant direct : seulement les p enfants immédiats */
h2 + p         { }   /* frère adjacent : le p qui suit IMMÉDIATEMENT un h2 */
h2 ~ p         { }   /* frères suivants : tous les p après un h2, même parent */
```

L'espace (descendant) est le plus utilisé. Le `>` sert quand tu as des listes imbriquées et que tu ne veux styler que le premier niveau.

## Les sélecteurs d'attribut

```css
a[target]              { }   /* les liens qui ONT un attribut target */
input[type="email"]    { }   /* valeur exacte */
a[href^="https"]       { }   /* ^ = commence par */
a[href$=".pdf"]        { }   /* $ = finit par */
a[href*="google"]      { }   /* * = contient */
```

Très pratique pour les formulaires (`input[type="checkbox"]`) et pour marquer les liens externes ou les PDF.

## À toi

Dans un fichier, écris le sélecteur qui cible :
1. Tous les liens à l'intérieur du `<nav>`, et eux seuls
2. Le paragraphe qui suit directement chaque `<h2>`
3. Tous les champs de type mot de passe
4. Les éléments qui ont **à la fois** la classe `carte` et la classe `active` (indice : pas d'espace entre les deux)

---

# MODULE 3 — Cascade, spécificité, héritage

**Le module le plus important du document.** Quand tu écris une règle et qu'« elle ne s'applique pas », la réponse est ici dans 90 % des cas.

## 1. La cascade

Quand deux règles de **même spécificité** visent le même élément, **la dernière écrite gagne**.

```css
p { color: blue; }
p { color: red; }    /* le texte sera rouge */
```

Ça vaut aussi entre fichiers : si tu charges `style.css` puis `theme.css`, `theme.css` gagne à égalité.

## 2. La spécificité

Chaque sélecteur reçoit un score en trois cases : **(id, classe, type)**.

| Sélecteur | Score |
|-----------|-------|
| `p` | (0,0,1) |
| `.intro` | (0,1,0) |
| `#page` | (1,0,0) |
| `nav ul li a` | (0,0,4) |
| `.menu a:hover` | (0,2,1) |
| `#page .intro p` | (1,1,1) |
| `style="..."` (en ligne) | (1,0,0,0) — au-dessus de tout |

**On compare case par case, de gauche à droite.** Ce n'est pas une addition.

```
(0,1,0)  bat  (0,0,7)
```

Une seule classe écrase sept balises. Dès qu'une case supérieure diffère, les suivantes ne comptent même pas.

Les **pseudo-classes** (`:hover`, `:first-child`) comptent comme une classe.
Les **pseudo-éléments** (`::before`, `::after`) comptent comme un type.

## 3. `!important`

```css
p { color: red !important; }
```

Ça écrase tout, y compris le style en ligne. **Tu ne l'utilises pas.** Si tu en as besoin, c'est que ton CSS est mal structuré — et le jour où tu voudras surcharger ton `!important`, tu devras en mettre un autre. C'est une spirale. Les seules exceptions légitimes : surcharger le CSS d'une librairie tierce que tu ne peux pas modifier.

## 4. L'héritage

Certaines propriétés se transmettent automatiquement aux enfants :

**Héritées :** `color`, `font-family`, `font-size`, `font-weight`, `line-height`, `text-align`, `letter-spacing`, `visibility`, `cursor`.

**Non héritées :** `background`, `border`, `padding`, `margin`, `width`, `height`, `display`, `position`.

D'où le réflexe pro : tu poses ta typographie **une seule fois** sur `body`, et toute la page en hérite.

```css
body {
  font-family: system-ui, sans-serif;
  color: #1a1a1a;
  line-height: 1.6;
}
```

Deux mots-clés utiles : `inherit` (force l'héritage d'une propriété qui ne l'est pas) et `initial` (remet la valeur par défaut du navigateur).

```css
button {
  font-family: inherit;   /* les boutons n'héritent PAS de la police par défaut ! */
}
```

Note ce cas : `input`, `button`, `textarea` et `select` n'héritent pas de la police. C'est LE truc qui fait qu'un formulaire a l'air moche. Ajoute cette règle systématiquement.

## L'ordre de résolution complet

Quand deux règles s'affrontent, le navigateur tranche dans cet ordre :
1. `!important` gagne
2. Sinon, la **spécificité** la plus haute gagne
3. Sinon, la **dernière écrite** gagne
4. Un style hérité perd toujours contre un style appliqué directement

## À toi

**Puzzle 1.** De quelle couleur est ce texte ? Donne les 4 scores.

```html
<div id="page">
  <p class="intro">Bonjour</p>
</div>
```
```css
p             { color: blue; }
.intro        { color: green; }
div p         { color: red; }
#page .intro  { color: orange; }
```

**Puzzle 2.** Pourquoi cette règle ne marche pas, et comment tu corriges sans utiliser `!important` ?

```css
.btn { background: blue; }
nav ul li a.btn { background: gray; }
```

---

# MODULE 4 — Le box model

Tout élément HTML est une boîte à quatre couches, de l'intérieur vers l'extérieur :

```
        ┌─────────── margin (transparent, pousse les voisins) ────────────┐
        │  ┌────────── border (la bordure visible) ──────────────────┐    │
        │  │  ┌──────── padding (espace intérieur, prend le fond) ─┐ │    │
        │  │  │                                                    │ │    │
        │  │  │              CONTENT (ton texte, ton image)        │ │    │
        │  │  │                                                    │ │    │
        │  │  └────────────────────────────────────────────────────┘ │    │
        │  └─────────────────────────────────────────────────────────┘    │
        └─────────────────────────────────────────────────────────────────┘
```

## La distinction à ne jamais oublier

- **`padding`** = espace **à l'intérieur**, entre le contenu et la bordure. **Prend la couleur de fond.**
- **`margin`** = espace **à l'extérieur**, entre cet élément et ses voisins. **Toujours transparent.**

Question type d'entretien et de validation : *« différence entre margin et padding ? »* → padding est dedans et coloré, margin est dehors et transparent.

## Les raccourcis

```css
.boite {
  padding: 20px;                    /* les 4 côtés */
  padding: 10px 20px;               /* haut/bas  gauche/droite */
  padding: 10px 20px 30px;          /* haut  gauche/droite  bas */
  padding: 10px 20px 30px 40px;     /* haut  droite  bas  gauche (sens horaire) */

  padding-top: 10px;                /* un seul côté */
  padding-inline: 20px;             /* moderne : gauche + droite */
  padding-block: 10px;              /* moderne : haut + bas */
}
```

Le sens horaire (haut → droite → bas → gauche) vaut aussi pour `margin` et `border`.

## `box-sizing` : la ligne qui change tout

Par défaut (`content-box`), `width` ne mesure **que le contenu**. Padding et border s'ajoutent par-dessus.

```css
.carte {
  width: 300px;
  padding: 20px;
  border: 5px solid;
}
```
→ Largeur réelle à l'écran : **350 px** (300 + 20+20 + 5+5). Et si tu mets `width: 100%` avec du padding, ton élément déborde de son parent. C'est LE bug classique.

Avec `box-sizing: border-box`, `width` inclut le padding et la border :

```css
* { box-sizing: border-box; }
```
→ La même carte fait **exactement 300 px**. Le contenu se réduit à 250 px pour compenser.

**Le margin reste toujours à l'extérieur**, dans les deux modes. `border-box` ne le change pas.

## La fusion des marges (margin collapsing)

Deux marges verticales qui se touchent **fusionnent** : on garde la plus grande, on ne les additionne pas.

```css
.haut { margin-bottom: 30px; }
.bas  { margin-top: 20px; }
```
→ L'espace entre les deux est de **30 px**, pas 50.

Ça ne concerne **que le vertical**, et **jamais** dans un conteneur `flex` ou `grid`. C'est une des raisons pour lesquelles on utilise `gap` en Flexbox : pas de surprise.

## `width`, `height` et leurs cousins

```css
.conteneur {
  width: 100%;
  max-width: 1200px;    /* ne dépasse jamais 1200px */
  min-width: 320px;     /* ne descend jamais sous 320px */
  margin: 0 auto;       /* centre horizontalement un bloc de largeur définie */

  height: 100vh;        /* 100% de la hauteur de la fenêtre */
  min-height: 400px;    /* au moins 400px, mais grandit si le contenu déborde */
}
```

**Le combo à connaître par cœur** — le conteneur centré de tous les sites :

```css
.conteneur {
  width: 100%;
  max-width: 1200px;
  margin-inline: auto;
  padding-inline: 1rem;   /* pour que ça ne colle pas aux bords sur mobile */
}
```

**Évite `height` fixe sur du texte.** Le jour où le contenu grandit, il déborde. Utilise `min-height` ou laisse le contenu décider.

## À toi

1. Un élément a `width: 300px`, `padding: 20px`, `border: 5px solid`, `margin: 10px`. Quelle largeur occupe-t-il **sans** `border-box` ? **Avec** ? (Compte aussi l'espace pris avec le margin.)
2. Crée trois cartes avec des `width`, `padding` et `border` **différents** dans le CSS, mais qui font **exactement la même largeur finale** à l'écran. Vérifie dans DevTools.
3. Pourquoi `width: 100%` + `padding: 20px` fait déborder un élément de son parent sans `border-box` ?

---

# MODULE 5 — Les unités

## Les unités absolues

`px` — le pixel. Fiable, prévisible. Tu l'utilises pour : les bordures (`1px`), les petits rayons, les ombres. **Évite-le pour les tailles de texte** (raison au module 12 : accessibilité).

## Les unités relatives

| Unité | Relative à quoi | Usage type |
|-------|-----------------|------------|
| `rem` | La taille de police de `<html>` (16px par défaut) | **Ton unité par défaut** : texte, padding, margin |
| `em` | La taille de police de **l'élément lui-même** | Padding de bouton proportionnel au texte |
| `%` | La taille du **parent** | Largeurs fluides |
| `vw` / `vh` | 1 % de la largeur / hauteur de la fenêtre | Sections plein écran |
| `ch` | La largeur du caractère « 0 » | `max-width: 65ch` pour la lisibilité |
| `fr` | Une fraction de l'espace libre (Grid uniquement) | Colonnes de Grid |

## rem vs em : la seule différence qui compte

`rem` regarde **toujours** la racine (`html`). Résultat stable et prévisible.

`em` regarde **l'élément courant**, et **s'accumule** dans les imbrications :

```css
.parent { font-size: 20px; }
.parent .enfant { font-size: 0.5em; }   /* = 10px */
.parent .enfant .petit-fils { font-size: 0.5em; }  /* = 5px ! ça s'empile */
```

**Règle pratique : `rem` par défaut, `em` seulement quand tu veux que l'espacement suive la taille du texte** (typiquement le padding d'un bouton, qui doit grossir si le bouton est en gros texte).

## La conversion mentale

Base 16 px, donc :

| rem | px |
|-----|-----|
| 0.5rem | 8px |
| 0.75rem | 12px |
| **1rem** | **16px** |
| 1.25rem | 20px |
| 1.5rem | 24px |
| 2rem | 32px |
| 3rem | 48px |

## `clamp()` — le responsive sans media query

```css
h1 {
  font-size: clamp(1.75rem, 5vw, 3.5rem);
}
```

Lecture : `clamp(minimum, valeur idéale, maximum)`. Le titre fait 5 % de la largeur de l'écran, mais jamais moins de 1.75rem ni plus de 3.5rem. **Une ligne remplace trois media queries.** Excellent pour les titres et les paddings de section.

## À toi

1. `html` est à 16px. Combien font `1.5rem` en pixels ? Et si un utilisateur règle son navigateur sur 20px ?
2. Écris un `h1` qui fait entre 2rem et 4rem selon la largeur de l'écran, avec `clamp()`.
3. Un paragraphe de texte : quelle `max-width` en `ch` pour une lecture confortable ? (Cherche « longueur de ligne lisibilité » si tu bloques — la réponse est entre 45 et 75.)

---

# MODULE 6 — Les couleurs

## Les quatre notations

```css
.exemple {
  color: red;                          /* nom : 147 mots-clés, utile pour tester */
  color: #e63946;                      /* hexadécimal : le standard des maquettes */
  color: #e3a;                         /* raccourci de #ee33aa */
  color: rgb(230 57 70);               /* rouge vert bleu, 0 à 255 */
  color: rgb(230 57 70 / 0.5);         /* avec transparence (syntaxe moderne) */
  color: hsl(355 79% 56%);             /* teinte, saturation, luminosité */
  color: hsl(355 79% 56% / 0.5);
}
```

## Pourquoi HSL vaut le détour

- **H** (hue) : 0-360°, la teinte sur la roue chromatique. 0 = rouge, 120 = vert, 240 = bleu.
- **S** (saturation) : 0 % = gris, 100 % = couleur pure.
- **L** (lightness) : 0 % = noir, 50 % = couleur normale, 100 % = blanc.

L'intérêt : **créer des variantes cohérentes en une seconde.**

```css
--bleu:        hsl(210 80% 50%);
--bleu-clair:  hsl(210 80% 70%);   /* même teinte, plus lumineux */
--bleu-fonce:  hsl(210 80% 30%);   /* pour un :hover */
```

Avec du hexadécimal, tu devrais aller chercher trois codes sans savoir s'ils s'harmonisent.

## Le contraste : la règle qui te fera gagner des points Lighthouse

Le texte doit contraster suffisamment avec son fond. Norme WCAG AA :
- Texte normal : ratio **4.5:1** minimum
- Grand texte (18px+ gras, ou 24px+) : **3:1**

Le gris clair sur blanc, c'est joli sur ta maquette et illisible en vrai. Vérifie sur **webaim.org/resources/contrastchecker** ou directement dans l'onglet Lighthouse de DevTools.

## Astuce : ne choisis pas tes couleurs au hasard

Si tu n'as pas de charte client : prends une couleur principale, une neutre foncée pour le texte, une neutre claire pour les fonds. Trois couleurs suffisent pour un site propre. Sites utiles : **coolors.co**, **realtimecolors.com**.

---

# MODULE 7 — La typographie

**C'est ce qui sépare visuellement un site amateur d'un site pro.** Plus que les couleurs, plus que les animations.

## Les propriétés essentielles

```css
body {
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  font-size: 1rem;
  font-weight: 400;        /* 100 à 900 ; 400 = normal, 700 = gras */
  line-height: 1.6;        /* SANS unité : 1.6 × la taille de police */
  letter-spacing: 0;
  color: #1a1a1a;          /* jamais #000 pur : trop dur à l'œil */
}
```

**`line-height` sans unité, toujours.** Avec `1.6` (et pas `1.6rem`), la valeur se recalcule pour chaque élément selon sa propre taille. Avec une unité, elle se fige et tes gros titres se chevauchent.

## Les valeurs qui marchent

| Contexte | line-height |
|----------|-------------|
| Corps de texte | 1.5 à 1.7 |
| Titres | 1.1 à 1.3 |
| Boutons, éléments serrés | 1 à 1.2 |

## `font-family` et la pile de secours

```css
font-family: 'Inter', system-ui, sans-serif;
```

Le navigateur essaie de gauche à droite. Si `Inter` n'est pas chargée, il passe à `system-ui` (la police native du système — belle et instantanée), puis à la sans-serif générique. **Termine toujours par une famille générique** (`sans-serif`, `serif`, `monospace`).

## Charger une police (Google Fonts)

Dans le `<head>` :

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
```

Deux règles de perf : **une seule famille** par site (deux maximum), et **seulement les graisses utilisées** (`wght@400;600;700` et pas tout le spectre). Chaque graisse est un fichier à télécharger, et Lighthouse le voit.

## L'échelle typographique

Ne choisis pas tes tailles au hasard. Prends une échelle et tiens-t'y :

```css
h1 { font-size: 2.5rem; }   /* 40px */
h2 { font-size: 2rem; }     /* 32px */
h3 { font-size: 1.5rem; }   /* 24px */
h4 { font-size: 1.25rem; }  /* 20px */
p  { font-size: 1rem; }     /* 16px */
small { font-size: 0.875rem; } /* 14px */
```

**Jamais de texte en dessous de 14px.** Et le corps de texte à 16px minimum : c'est la taille de lecture confortable, et c'est ce que Lighthouse attend.

## Les autres propriétés utiles

```css
text-align: center;              /* left | right | center | justify */
text-transform: uppercase;       /* MAJUSCULES — utile pour les petits labels */
text-decoration: none;           /* enlever le soulignement des liens */
font-style: italic;
letter-spacing: 0.05em;          /* espacer les lettres — bien sur les majuscules */
word-spacing: 0.1em;
white-space: nowrap;             /* empêcher le retour à la ligne */
text-overflow: ellipsis;         /* affiche « … » (avec overflow:hidden + nowrap) */
```

Le combo « texte tronqué sur une ligne » :

```css
.tronque {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

Et sur plusieurs lignes :

```css
.tronque-3-lignes {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
```

**N'écris jamais `text-align: justify` sur du web.** Ça crée des rivières blanches horribles sans césure.

## La longueur de ligne

```css
.article p {
  max-width: 65ch;
}
```

Au-delà de ~75 caractères, l'œil perd sa ligne en revenant à gauche. C'est un détail de typographe qui rend un blog immédiatement plus lisible.

## À toi

Prends ta page « À propos » du Jour 2 et applique une vraie typo : une police Google Fonts, une échelle cohérente, `line-height: 1.6` sur le corps, `max-width: 65ch` sur les paragraphes. Compare avant/après. C'est souvent le changement le plus spectaculaire pour le moins d'effort.

---

# MODULE 8 — `display`

`display` détermine **comment un élément se comporte dans le flux** de la page.

| Valeur | Comportement |
|--------|--------------|
| `block` | Prend toute la largeur, va à la ligne. `width`/`height`/margins verticaux fonctionnent. (`div`, `p`, `h1`, `section`) |
| `inline` | Reste dans le texte. **`width`, `height` et margins verticaux sont ignorés.** (`span`, `a`, `strong`) |
| `inline-block` | Reste dans la ligne **mais** accepte width/height/margins. (`img`, `button`) |
| `none` | Retiré de la page, ne prend aucune place |
| `flex` | Conteneur Flexbox (module 9) |
| `grid` | Conteneur Grid (module 10) |

## Le piège n°1 des débutants

```html
<a href="#" class="btn">Cliquez</a>
```
```css
.btn {
  padding: 1rem 2rem;   /* le padding horizontal marche… */
  width: 200px;         /* …mais ça, c'est IGNORÉ */
}
```

Un `<a>` est `inline`. Correction :

```css
.btn {
  display: inline-block;   /* ou block, ou flex */
  padding: 1rem 2rem;
  width: 200px;
}
```

**Réflexe : « mon width ne marche pas » → l'élément est inline.**

## `display: none` vs `visibility: hidden` vs `opacity: 0`

```css
display: none;        /* disparaît ET libère sa place. Invisible aux lecteurs d'écran. */
visibility: hidden;   /* invisible mais GARDE sa place */
opacity: 0;           /* invisible, garde sa place, reste CLIQUABLE (piège !) */
```

Pour un menu burger : `display: none` (ou une transform hors écran si tu veux l'animer — voir module 14).

---

# MODULE 9 — Flexbox

**Le module qui va te faire gagner le plus de temps de toute ta carrière.** Flexbox aligne des éléments sur **une dimension** : une ligne, ou une colonne.

## Le principe

Tu déclares `display: flex` sur un **parent**. Ses **enfants directs** deviennent des « items flex » et s'alignent selon un axe.

```css
.conteneur {
  display: flex;
}
```

Instantanément, les enfants passent côte à côte.

## Les deux axes — à comprendre avant tout le reste

```
flex-direction: row (défaut)
   axe principal  ────────────────────►  (horizontal)
   axe secondaire ▼ (vertical)

flex-direction: column
   axe principal  ▼ (vertical)
   axe secondaire ────────────────────►  (horizontal)
```

**`justify-content` agit sur l'axe PRINCIPAL. `align-items` agit sur l'axe SECONDAIRE.**

C'est tout le secret. Si tu retiens ça, tu ne te tromperas plus jamais. Et note bien : **quand tu passes en `column`, les deux s'inversent** — `justify-content` gère alors le vertical.

## Les propriétés du parent

```css
.conteneur {
  display: flex;

  flex-direction: row;          /* row | row-reverse | column | column-reverse */

  justify-content: flex-start;  /* axe principal :
                                   flex-start | flex-end | center |
                                   space-between | space-around | space-evenly */

  align-items: stretch;         /* axe secondaire :
                                   stretch | flex-start | flex-end | center | baseline */

  flex-wrap: nowrap;            /* nowrap | wrap — autoriser le passage à la ligne */

  gap: 1rem;                    /* espace entre les items — LA bonne méthode */
  row-gap: 1rem;
  column-gap: 2rem;

  align-content: flex-start;    /* aligne les LIGNES quand il y a wrap */
}
```

## Comprendre `justify-content` visuellement

```
flex-start      [AAA][BBB][CCC]..................
center          .........[AAA][BBB][CCC].........
flex-end        ..................[AAA][BBB][CCC]
space-between   [AAA].......[BBB].......[CCC]        ← rien aux extrémités
space-around    ...[AAA]......[BBB]......[CCC]...    ← demi-espace aux bords
space-evenly    .....[AAA].....[BBB].....[CCC].....  ← espaces tous égaux
```

`space-between` est celui que tu utiliseras le plus : c'est la navbar (logo à gauche, liens à droite).

## Les propriétés des enfants

```css
.item {
  flex-grow: 0;        /* 0 = ne grandit pas ; 1 = prend l'espace libre */
  flex-shrink: 1;      /* 1 = peut rétrécir si ça déborde */
  flex-basis: auto;    /* taille de départ avant répartition */

  flex: 1;             /* raccourci = flex: 1 1 0 → « prends une part égale » */
  flex: 0 0 300px;     /* « fais exactement 300px, ne grandis ni ne rétrécis » */

  align-self: center;  /* surcharge align-items pour CET item seulement */
  order: 2;            /* change l'ordre visuel sans toucher au HTML */
}
```

**`flex: 1` sur tous les enfants = colonnes de largeur égale.** C'est le raccourci le plus utile de Flexbox.

## Les 6 recettes à connaître par cœur

**1. Centrage parfait (horizontal ET vertical)**

```css
.parent {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}
```
La réponse à la question classique « comment tu centres un élément ? ». Trois lignes.

**2. La navbar**

```css
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
}
```

**3. Une rangée de cartes de largeur égale**

```css
.cartes { display: flex; gap: 1.5rem; }
.carte  { flex: 1; }
```

**4. Des cartes qui passent à la ligne toutes seules**

```css
.cartes { display: flex; flex-wrap: wrap; gap: 1.5rem; }
.carte  { flex: 1 1 300px; }   /* min 300px, sinon on va à la ligne */
```
Ça, c'est du responsive **sans une seule media query**. Retiens-le.

**5. Le footer collé en bas de page (même si la page est courte)**

```css
body {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}
main { flex: 1; }   /* main mange tout l'espace libre, le footer est poussé en bas */
```

**6. Un élément poussé à droite dans une barre**

```css
.item-a-droite { margin-left: auto; }
```
Un `margin: auto` en Flexbox absorbe tout l'espace disponible. Élégant.

## `gap` plutôt que `margin`

```css
/* ❌ L'ancienne méthode, pénible */
.carte { margin-right: 1rem; }
.carte:last-child { margin-right: 0; }

/* ✅ La bonne */
.cartes { display: flex; gap: 1rem; }
```

`gap` n'ajoute jamais d'espace aux extrémités. Il fonctionne en Flexbox et en Grid. Utilise-le systématiquement.

## À toi — l'entraînement obligatoire

**Fais les 24 niveaux de Flexbox Froggy** (flexboxfroggy.com, disponible en français). Compte 30-40 min. C'est le meilleur investissement de ta journée.

Ensuite, sans rien copier :
1. Une navbar : logo à gauche, 4 liens à droite, alignés verticalement
2. Trois cartes tarifs de largeur égale avec un `gap` de 2rem
3. Un footer en 3 colonnes
4. Un élément parfaitement centré au milieu de l'écran
5. Une grille de 6 cartes qui passe de 3 à 2 à 1 colonne **sans media query** (recette 4)

**Objectif : coder une navbar en moins de 15 minutes, de mémoire.**

---

# MODULE 10 — Grid

Flexbox aligne sur **une** dimension. Grid gère **deux** dimensions : lignes ET colonnes simultanément.

## Quand utiliser lequel

| Situation | Outil |
|-----------|-------|
| Navbar, boutons alignés, footer en colonnes | **Flexbox** |
| Centrer un élément | **Flexbox** |
| Rangée de cartes qui s'adapte | **Flexbox** (ou Grid) |
| Galerie d'images en grille régulière | **Grid** |
| Mise en page complète (header/sidebar/main/footer) | **Grid** |
| Tableau de bord avec zones de tailles différentes | **Grid** |

Formule à retenir : **Flexbox pour le contenu, Grid pour la mise en page.** Et les deux se combinent — une cellule de Grid peut être un conteneur Flex.

## La base

```css
.grille {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;   /* 3 colonnes égales */
  gap: 1rem;
}
```

L'unité **`fr`** (fraction) répartit l'espace **libre**. `1fr 1fr 1fr` = trois parts égales. `2fr 1fr` = la première colonne fait le double de la seconde.

## `repeat()` et les colonnes

```css
grid-template-columns: repeat(3, 1fr);          /* = 1fr 1fr 1fr */
grid-template-columns: 250px 1fr;               /* sidebar fixe + contenu fluide */
grid-template-columns: repeat(4, minmax(0, 1fr));
```

`minmax(min, max)` définit une taille plancher et plafond.

## LA recette Grid la plus utile

```css
.galerie {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}
```

Traduction : *« mets autant de colonnes que tu peux, chacune fait au minimum 280px, et elles se partagent l'espace restant. »*

Résultat : **une grille entièrement responsive en 3 lignes, sans aucune media query.** Elle passera toute seule de 4 à 3 à 2 à 1 colonne selon l'écran. Apprends-la par cœur, tu la réutiliseras sur chaque projet.

> `auto-fit` fait grossir les colonnes pour remplir la ligne. `auto-fill` garde des colonnes vides. Dans 95 % des cas tu veux `auto-fit`.

## Placer un élément sur plusieurs cases

```css
.item-large {
  grid-column: span 2;        /* occupe 2 colonnes */
  grid-row: span 2;           /* occupe 2 lignes */
  grid-column: 1 / 3;         /* de la ligne de grille 1 à la 3 */
  grid-column: 1 / -1;        /* toute la largeur (très pratique) */
}
```

## Les zones nommées — la mise en page lisible

```css
.layout {
  display: grid;
  grid-template-columns: 220px 1fr;
  grid-template-rows: auto 1fr auto;
  grid-template-areas:
    "header  header"
    "sidebar main"
    "footer  footer";
  min-height: 100vh;
  gap: 1rem;
}

.header  { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main    { grid-area: main; }
.footer  { grid-area: footer; }
```

Tu dessines littéralement ta page en ASCII dans le CSS. Et en responsive, tu redessines :

```css
@media (max-width: 768px) {
  .layout {
    grid-template-columns: 1fr;
    grid-template-areas:
      "header"
      "main"
      "sidebar"
      "footer";
  }
}
```

Toute la mise en page mobile réorganisée en 6 lignes.

## Alignement dans Grid

```css
.grille {
  justify-items: center;   /* horizontal, dans chaque cellule */
  align-items: center;     /* vertical, dans chaque cellule */
  place-items: center;     /* raccourci des deux */

  justify-content: center; /* la grille entière dans son conteneur */
  align-content: center;
}
```

Bonus : **le centrage le plus court du CSS**

```css
.parent { display: grid; place-items: center; min-height: 100vh; }
```

## À toi

1. **Grid Garden** (cssgridgarden.com, en français) : les 28 niveaux, ~25 min.
2. Une galerie de 9 images avec la recette `auto-fit / minmax`. Redimensionne la fenêtre : elle doit se réorganiser seule.
3. Un layout complet header / sidebar / main / footer avec `grid-template-areas`, qui devient une colonne unique sous 768px.

---

# MODULE 11 — `position` et `z-index`

## Les cinq valeurs

```css
position: static;     /* défaut — dans le flux normal, top/left ignorés */
position: relative;   /* dans le flux, mais décalable par rapport à SA position */
position: absolute;   /* sorti du flux, positionné / au parent positionné le plus proche */
position: fixed;      /* sorti du flux, positionné / à la FENÊTRE, ne bouge pas au scroll */
position: sticky;     /* normal, puis se fige quand il atteint un seuil au scroll */
```

Dès que la position n'est pas `static`, tu peux utiliser `top`, `right`, `bottom`, `left` et `z-index`.

## La règle d'or de `absolute`

**Un élément en `absolute` se positionne par rapport à son ancêtre positionné le plus proche.** Si aucun ancêtre n'a de `position` autre que `static`, il se cale sur la page entière — et tu ne comprends pas pourquoi ton badge est parti dans le coin.

Le duo qu'on utilise **toujours** ensemble :

```css
.carte {
  position: relative;      /* je deviens le repère */
}
.carte .badge {
  position: absolute;      /* je me place DANS la carte */
  top: 10px;
  right: 10px;
}
```

**`relative` sur le parent, `absolute` sur l'enfant.** C'est le pattern du badge « Promo », de l'icône dans un champ de recherche, de la légende sur une image.

## `sticky` — la navbar qui suit

```css
.navbar {
  position: sticky;
  top: 0;
  z-index: 100;
}
```

Elle défile normalement, puis se colle en haut. Deux conditions pour que ça marche : **il faut un `top` (ou `bottom`) défini**, et **le parent ne doit pas avoir `overflow: hidden`**. C'est la cause n°1 des « mon sticky ne marche pas ».

## `fixed` — le bouton flottant

```css
.bouton-contact {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  z-index: 50;
}
```

Utilisé pour : le bouton « retour en haut », le chat, le bandeau cookies, les modales.

## `z-index`

Contrôle l'ordre d'empilement. Ne fonctionne **que** sur les éléments positionnés (pas `static`).

```css
.modale       { z-index: 1000; }
.overlay      { z-index: 999; }
.navbar       { z-index: 100; }
.dropdown     { z-index: 10; }
```

**Utilise une échelle par paliers** (10, 50, 100, 1000) plutôt que 1, 2, 3 : tu pourras toujours intercaler quelque chose. Et ne mets jamais `z-index: 99999` — c'est le début du chaos.

Attention au **contexte d'empilement** : un enfant ne peut jamais passer au-dessus d'un élément qui est au-dessus de son parent, quel que soit son `z-index`. Si ton `z-index` semble ignoré, regarde le parent.

## Le centrage à l'ancienne (bon à savoir lire)

```css
.centre {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
```

Tu ne l'écris plus (Flexbox est mieux), mais tu le rencontreras dans du code existant. Le `translate(-50%,-50%)` recentre l'élément sur son propre milieu.

## À toi

1. Une carte produit avec un badge « -30 % » collé en haut à droite de l'image
2. Une navbar sticky qui reste en haut au scroll
3. Un bouton « retour en haut » fixe en bas à droite

---

# MODULE 12 — Le responsive

**Non négociable.** Plus de la moitié du trafic web est sur mobile, et Google indexe la version mobile en priorité. Un site non responsive est invendable.

## Étape 0 — la balise viewport

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

Dans le `<head>` de **chaque** page. Sans elle, le mobile fait semblant d'être un écran de 980px et dézoome tout. **Aucune media query ne fonctionnera** si elle est absente.

## Le mobile-first

Tu écris **d'abord le style mobile** (sans media query), puis tu ajoutes ce qui change sur grand écran avec `min-width`.

```css
/* Mobile par défaut */
.cartes {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
}

/* Tablette et + */
@media (min-width: 768px) {
  .cartes { grid-template-columns: repeat(2, 1fr); }
}

/* Desktop et + */
@media (min-width: 1024px) {
  .cartes { grid-template-columns: repeat(3, 1fr); }
}
```

**Pourquoi mobile-first plutôt que l'inverse ?** Le mobile est le cas le plus contraint : en partant de là tu es obligé de garder l'essentiel. Le CSS est plus court, tu écris moins de surcharges, et le mobile (qui a le moins de puissance) charge le CSS le plus simple.

## Les points de rupture

```css
@media (min-width: 480px)  { }   /* grand mobile */
@media (min-width: 768px)  { }   /* tablette */
@media (min-width: 1024px) { }   /* laptop */
@media (min-width: 1280px) { }   /* grand écran */
```

Ce sont des repères, pas une loi. **La bonne méthode : élargis la fenêtre lentement et mets une media query au moment où ça devient moche.** Ton design décide, pas une liste d'iPhone.

## La syntaxe complète

```css
@media (min-width: 768px) { }                          /* à partir de */
@media (max-width: 767px) { }                          /* jusqu'à */
@media (min-width: 768px) and (max-width: 1023px) { }  /* entre les deux */
@media print { }                                        /* impression */
@media (prefers-color-scheme: dark) { }                 /* mode sombre système */
@media (prefers-reduced-motion: reduce) { }             /* accessibilité animations */
```

Ce dernier compte pour Lighthouse et pour les gens sensibles au mouvement :

```css
@media (prefers-reduced-motion: reduce) {
  * { animation: none !important; transition: none !important; }
}
```
(Un des rares cas où `!important` est justifié.)

## Les images fluides — la règle qui sauve tout

```css
img {
  max-width: 100%;
  height: auto;
  display: block;
}
```

Sans `max-width: 100%`, une image de 2000px de large fait déborder toute ta page sur mobile. `height: auto` préserve les proportions. `display: block` supprime l'espace fantôme sous les images (les images sont `inline` par défaut, elles s'alignent sur la ligne de base du texte).

Ces trois lignes vont dans ton reset. **À vie.**

## Les autres réflexes responsive

```css
/* Conteneur qui respire sur mobile */
.conteneur {
  width: 100%;
  max-width: 1200px;
  margin-inline: auto;
  padding-inline: 1rem;
}

/* Titres fluides sans media query */
h1 { font-size: clamp(1.75rem, 5vw, 3.5rem); }

/* Zones tactiles : 44px minimum (recommandation Apple/Google) */
.btn, nav a {
  min-height: 44px;
  display: inline-flex;
  align-items: center;
}

/* Vidéos et iframes responsives */
.video { aspect-ratio: 16 / 9; width: 100%; }
```

## Le test de vérité

1. **DevTools → mode appareil** (icône téléphone, ou `Ctrl+Shift+M`). Teste iPhone SE (375px), c'est le plus étroit.
2. **Aucun défilement horizontal.** Jamais. Si tu en as un, cherche un élément avec une largeur fixe, un `width: 100%` + padding sans `border-box`, ou une image sans `max-width`.
3. **Sur ton vrai téléphone.** DevTools ment sur les polices et le tactile. Lance Live Server, récupère l'adresse réseau (`http://192.168.x.x:5500`) et ouvre-la sur ton téléphone connecté au même wifi.
4. **Textes lisibles sans zoomer**, boutons cliquables au pouce.

## À toi

Reprends ta landing page du Jour 7 et vérifie-la en mode iPhone SE. Corrige jusqu'à ce qu'il n'y ait **aucun** défilement horizontal et que tout soit lisible. Puis ouvre-la sur ton téléphone.

---

# MODULE 13 — Les variables CSS

Aussi appelées « propriétés personnalisées ». C'est ce qui rend un CSS maintenable.

## Déclaration et usage

```css
:root {
  /* Couleurs */
  --primaire: hsl(210 80% 50%);
  --primaire-fonce: hsl(210 80% 40%);
  --texte: #1a1a1a;
  --texte-doux: #666;
  --fond: #ffffff;
  --fond-alt: #f5f5f5;
  --bordure: #e0e0e0;

  /* Espacements */
  --esp-xs: 0.5rem;
  --esp-sm: 1rem;
  --esp-md: 2rem;
  --esp-lg: 4rem;

  /* Divers */
  --rayon: 8px;
  --ombre: 0 2px 8px rgb(0 0 0 / 0.1);
  --transition: 200ms ease;
}

.btn {
  background: var(--primaire);
  padding: var(--esp-sm) var(--esp-md);
  border-radius: var(--rayon);
  transition: background var(--transition);
}

.btn:hover {
  background: var(--primaire-fonce);
}
```

`:root` = l'élément `<html>`. Les variables y sont accessibles partout.

## Pourquoi c'est un gain énorme

Le client dit « finalement je préfère du vert ». Sans variables : tu cherches 40 occurrences de `#3b82f6` dans 800 lignes. Avec : **tu changes une ligne.**

`var(--nom, valeur-de-secours)` permet un défaut : `color: var(--accent, blue)`.

## Le mode sombre en 8 lignes

C'est l'application la plus impressionnante :

```css
:root {
  --fond: #ffffff;
  --texte: #1a1a1a;
}

[data-theme="dark"] {
  --fond: #121212;
  --texte: #f0f0f0;
}

body {
  background: var(--fond);
  color: var(--texte);
}
```

Puis en JavaScript (Jour 19 de ta roadmap) : `document.documentElement.dataset.theme = 'dark'`. **Toute la page bascule.** Tu n'as pas une seule autre règle à écrire.

## À savoir

- Les variables CSS **héritent** — tu peux les redéfinir localement sur un composant.
- Elles sont lisibles et modifiables en JavaScript (contrairement aux variables Sass).
- Elles fonctionnent dans tous les navigateurs modernes. Aucune raison de s'en priver.

---

# MODULE 14 — Transitions, transform, animations

## Les transitions

```css
.btn {
  background: var(--primaire);
  transition: background 200ms ease, transform 200ms ease;
}

.btn:hover {
  background: var(--primaire-fonce);
  transform: translateY(-2px);
}
```

Syntaxe : `transition: <propriété> <durée> <courbe> <délai>;`

**Trois règles de pro :**

1. **Nomme les propriétés, n'écris pas `transition: all`.** `all` force le navigateur à surveiller tout, c'est mauvais pour la performance et ça produit des effets involontaires.
2. **150 à 300 ms.** En dessous on ne voit rien, au-dessus ça donne une impression de lenteur. `200ms` est une excellente valeur par défaut.
3. **Anime seulement `transform` et `opacity` quand c'est possible.** Ce sont les deux seules propriétés que le navigateur peut animer sur la carte graphique. Animer `width`, `height`, `top` ou `margin` force un recalcul de toute la mise en page à chaque image → saccades.

Les courbes : `ease` (défaut, bon), `ease-out` (bon pour les entrées), `linear` (mécanique), `cubic-bezier(...)` (sur mesure).

## `transform`

```css
transform: translateY(-4px);          /* déplacer */
transform: translate(10px, 20px);
transform: scale(1.05);               /* agrandir de 5% */
transform: rotate(45deg);
transform: rotate(45deg) scale(1.1);  /* on combine, l'ordre compte */
```

`transform` ne déplace **que le rendu visuel** : l'élément garde sa place dans le flux, rien ne bouge autour. C'est pour ça que c'est fluide.

## Les animations

```css
@keyframes apparition {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.section {
  animation: apparition 600ms ease-out forwards;
}
```

`forwards` = l'élément reste dans l'état final au lieu de revenir au départ.

Avec des étapes intermédiaires :

```css
@keyframes pulsation {
  0%, 100% { transform: scale(1); }
  50%      { transform: scale(1.05); }
}

.badge {
  animation: pulsation 2s ease-in-out infinite;
}
```

## Le bon dosage

Une animation doit se remarquer **sans se voir**. Sur un site client :
- `:hover` sur les boutons et les cartes → oui, toujours
- Apparition douce des sections au scroll → oui, c'est ce qui fait « moderne »
- Un loader animé → oui
- Des éléments qui tournent, rebondissent, clignotent → **non**

## L'apparition au scroll

C'est l'effet qui fait « site d'agence ». Le CSS :

```css
.reveler {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 600ms ease-out, transform 600ms ease-out;
}

.reveler.visible {
  opacity: 1;
  transform: translateY(0);
}
```

Le JS ajoute la classe `.visible` quand la section entre à l'écran (`IntersectionObserver` — c'est au Jour 20 de ta roadmap). Le CSS est déjà prêt.

---

# MODULE 15 — Ombres, arrondis, dégradés, bordures

## Les bordures

```css
border: 1px solid #e0e0e0;         /* épaisseur style couleur */
border-bottom: 2px solid;
border: none;
outline: 2px solid blue;           /* comme border, mais ne prend pas de place */
outline-offset: 4px;
```

**Ne supprime jamais l'`outline` sans remplacement.** C'est l'anneau de focus qui permet la navigation au clavier. Si tu veux le restyler :

```css
:focus-visible {
  outline: 2px solid var(--primaire);
  outline-offset: 3px;
}
```

## Les arrondis

```css
border-radius: 8px;
border-radius: 8px 8px 0 0;    /* haut-gauche, haut-droit, bas-droit, bas-gauche */
border-radius: 50%;            /* cercle parfait (sur un élément carré) */
border-radius: 999px;          /* pilule — pour les boutons et badges */
```

Reste **cohérent** : choisis 4px, 8px ou 12px et applique le même partout (via `--rayon`). Des arrondis différents sur chaque élément, ça se voit immédiatement.

## Les ombres

```css
box-shadow: 0 2px 8px rgb(0 0 0 / 0.1);
/*          ↑  ↑   ↑    ↑
            X  Y  flou couleur */

box-shadow: inset 0 2px 4px rgb(0 0 0 / 0.1);   /* ombre intérieure */
```

**Une échelle qui marche**, à copier telle quelle :

```css
:root {
  --ombre-sm: 0 1px 3px rgb(0 0 0 / 0.08);
  --ombre-md: 0 4px 12px rgb(0 0 0 / 0.1);
  --ombre-lg: 0 12px 32px rgb(0 0 0 / 0.14);
}
```

Le secret d'une ombre crédible : **beaucoup de flou, peu d'opacité, léger décalage vers le bas** (la lumière vient d'en haut). Une ombre noire à 50 % d'opacité fait immédiatement amateur.

Effet de survol classique sur une carte :

```css
.carte {
  box-shadow: var(--ombre-sm);
  transition: box-shadow 200ms ease, transform 200ms ease;
}
.carte:hover {
  box-shadow: var(--ombre-lg);
  transform: translateY(-4px);
}
```

## Les dégradés

```css
background: linear-gradient(to right, #667eea, #764ba2);
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
background: radial-gradient(circle, #667eea, #764ba2);

/* Voile sombre sur une image de fond, pour rendre le texte lisible */
background:
  linear-gradient(rgb(0 0 0 / 0.5), rgb(0 0 0 / 0.5)),
  url('hero.jpg') center / cover no-repeat;
```

Ce dernier est **le pattern du hero de landing page**. Sans le voile, ton titre blanc est illisible sur une photo claire.

---

# MODULE 16 — Pseudo-classes et pseudo-éléments

## Les pseudo-classes (un `:`) — un état

```css
a:hover        { }   /* souris dessus */
a:focus        { }   /* sélectionné au clavier */
a:focus-visible{ }   /* focus clavier uniquement — préfère celui-ci */
a:active       { }   /* pendant le clic */
a:visited      { }   /* lien déjà visité */

input:checked  { }   /* case cochée */
input:disabled { }
input:required { }
input:invalid  { }   /* validation HTML échouée */
input:placeholder-shown { }

li:first-child { }
li:last-child  { }
li:nth-child(2)     { }   /* le 2e */
li:nth-child(odd)   { }   /* impairs — pour zébrer un tableau */
li:nth-child(even)  { }
li:nth-child(3n)    { }   /* tous les 3 */

.carte:not(.active) { }   /* toutes sauf celles qui ont .active */
```

`:has()` est le plus récent et le plus puissant — le « sélecteur parent » qu'on attendait depuis 20 ans :

```css
.carte:has(img) { }              /* les cartes QUI CONTIENNENT une image */
label:has(input:checked) { }     /* le label dont la case est cochée */
```

## Les pseudo-éléments (deux `::`) — un morceau généré

```css
.carte::before { content: ""; }
.carte::after  { content: ""; }
p::first-line  { }
p::first-letter{ }
::selection    { background: yellow; }   /* le surlignage de sélection */
::placeholder  { color: #999; }
```

**`content` est obligatoire**, même vide, sinon rien ne s'affiche.

Usages concrets :

```css
/* Astérisque rouge sur les champs obligatoires */
.champ-requis label::after {
  content: " *";
  color: red;
}

/* Trait décoratif sous un titre de section */
.section-titre::after {
  content: "";
  display: block;
  width: 60px;
  height: 3px;
  background: var(--primaire);
  margin-top: 0.75rem;
}

/* Icône devant un lien externe */
a[target="_blank"]::after {
  content: " ↗";
}
```

## Le style de lien complet

```css
a {
  color: var(--primaire);
  text-decoration: none;
  transition: color 200ms ease;
}
a:hover { text-decoration: underline; }
a:focus-visible {
  outline: 2px solid var(--primaire);
  outline-offset: 2px;
}
```

---

# MODULE 17 — Arrière-plans et `overflow`

## `background`

```css
background-color: #f5f5f5;
background-image: url('photo.jpg');
background-size: cover;        /* remplit, quitte à rogner — le plus utilisé */
background-size: contain;      /* entier, quitte à laisser du vide */
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;  /* effet parallaxe simple */

/* Raccourci */
background: #f5f5f5 url('photo.jpg') center / cover no-repeat;
```

`cover` vs `contain` : **cover remplit et rogne, contain montre tout et laisse du vide.** Pour un hero, c'est toujours `cover`.

## `object-fit` — le `cover` des balises `<img>`

```css
.carte img {
  width: 100%;
  height: 220px;
  object-fit: cover;      /* rogne intelligemment, ne déforme JAMAIS */
}
```

**À utiliser sur toutes tes grilles de cartes.** Sans ça, des images de proportions différentes déforment ta grille ou s'étirent horriblement. `object-fit: cover` te donne une grille parfaitement régulière avec n'importe quelles images. C'est un détail qui fait toute la différence visuelle.

## `overflow`

```css
overflow: visible;    /* défaut — le contenu déborde */
overflow: hidden;     /* on coupe */
overflow: auto;       /* barre de défilement si nécessaire */
overflow: scroll;     /* barre toujours visible */
overflow-x: auto;     /* horizontal seulement — pour un tableau large sur mobile */
overflow-y: auto;
```

Deux usages classiques :

```css
/* Tableau scrollable horizontalement sur mobile */
.tableau-conteneur { overflow-x: auto; }

/* Image qui zoome dans une carte sans déborder */
.carte { overflow: hidden; border-radius: 8px; }
.carte img { transition: transform 400ms ease; }
.carte:hover img { transform: scale(1.05); }
```

⚠️ **`overflow: hidden` casse `position: sticky`** chez les enfants. Si ta navbar sticky ne colle pas, cherche un `overflow: hidden` sur un parent.

## Le scroll fluide

```css
html {
  scroll-behavior: smooth;
  scroll-padding-top: 80px;   /* compense la hauteur de la navbar sticky */
}
```

Deux lignes, et tes ancres `#contact` défilent en douceur en s'arrêtant au bon endroit.

---

# MODULE 18 — Organiser son CSS

## Ton reset de départ

À mettre en haut de chaque projet :

```css
*, *::before, *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: system-ui, -apple-system, sans-serif;
  line-height: 1.6;
  color: #1a1a1a;
  background: #fff;
  -webkit-font-smoothing: antialiased;
}

img, picture, video, svg {
  max-width: 100%;
  height: auto;
  display: block;
}

input, button, textarea, select {
  font: inherit;      /* sinon ils gardent la police par défaut du navigateur */
  color: inherit;
}

button { cursor: pointer; background: none; border: none; }

h1, h2, h3, h4 { line-height: 1.2; }

ul[class], ol[class] { list-style: none; }   /* enlever les puces des listes stylées */
```

## L'ordre de ton fichier

```css
/* 1. Reset                */
/* 2. Variables (:root)    */
/* 3. Styles de base       */  /* body, h1-h6, p, a, img */
/* 4. Utilitaires          */  /* .conteneur, .sr-only, .btn */
/* 5. Composants           */  /* .navbar, .carte, .footer */
/* 6. Sections de page     */  /* .hero, .services, .temoignages */
/* 7. Media queries        */
```

**Du plus général au plus spécifique.** Comme ça, la cascade travaille pour toi au lieu de contre toi.

## Nommer ses classes

La convention **BEM** est la plus répandue :

```css
.carte             { }   /* Bloc */
.carte__titre      { }   /* Élément (partie du bloc) */
.carte__image      { }
.carte--vedette    { }   /* Modificateur (variante) */
```

```html
<article class="carte carte--vedette">
  <img class="carte__image" src="..." alt="...">
  <h3 class="carte__titre">Titre</h3>
</article>
```

Tu n'es pas obligé d'être puriste. **Ce qui compte : des noms qui décrivent le rôle, pas l'apparence.**

```css
/* ❌ */ .texte-rouge, .marge-20, .grand-titre-bleu
/* ✅ */ .message-erreur, .carte__titre, .btn--primaire
```

Le jour où le client veut du bleu au lieu du rouge, `.texte-rouge { color: blue }` c'est ridicule. `.message-erreur`, ça reste juste.

## Une classe utilitaire à connaître

```css
.sr-only {
  position: absolute;
  width: 1px; height: 1px;
  padding: 0; margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}
```

Cache visuellement un texte tout en le laissant lisible par les lecteurs d'écran. Pour les libellés de champs de recherche, les liens « aller au contenu ». Lighthouse aime.

---

# MODULE 19 — Les 12 erreurs de débutant

À relire avant chaque livraison.

1. **Oublier `box-sizing: border-box`** → les largeurs explosent, tout déborde.
2. **Oublier la balise viewport** → aucune media query ne fonctionne sur mobile.
3. **Mettre `width` sur un élément `inline`** → c'est ignoré. Passe en `inline-block` ou `block`.
4. **Utiliser `!important` pour forcer** → tu masques un problème de spécificité qui reviendra plus fort.
5. **Des `height` fixes sur du texte** → ça déborde dès que le contenu grandit. Utilise `min-height`.
6. **`px` pour les tailles de police** → casse l'accessibilité (l'utilisateur ne peut plus agrandir). Utilise `rem`.
7. **Oublier `max-width: 100%` sur les images** → défilement horizontal sur mobile garanti.
8. **Supprimer l'`outline` du focus** → site inutilisable au clavier, gros malus Lighthouse.
9. **Des marges partout au lieu de `gap`** → CSS bavard, `:last-child` à corriger sans arrêt.
10. **Trop de `position: absolute`** → tu construis une mise en page rigide qui casse en responsive. Flexbox et Grid d'abord ; `absolute` seulement pour superposer.
11. **Nommer ses classes selon l'apparence** (`.texte-rouge`) au lieu du rôle (`.message-erreur`).
12. **Ne tester qu'en desktop** → 50 % de tes visiteurs sont sur mobile, et Google indexe la version mobile.

---

# MODULE 20 — Aide-mémoire

## Les 8 lignes de départ de tout projet

```css
*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }
img { max-width: 100%; height: auto; display: block; }
input, button, textarea, select { font: inherit; }
body { font-family: system-ui, sans-serif; line-height: 1.6; color: #1a1a1a; }
```

## Les 6 recettes à savoir de mémoire

```css
/* 1. Centrage parfait */
.parent { display: flex; justify-content: center; align-items: center; min-height: 100vh; }

/* 2. Navbar */
.navbar { display: flex; justify-content: space-between; align-items: center; }

/* 3. Conteneur centré */
.conteneur { width: 100%; max-width: 1200px; margin-inline: auto; padding-inline: 1rem; }

/* 4. Grille responsive SANS media query */
.grille { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; }

/* 5. Footer collé en bas */
body { display: flex; flex-direction: column; min-height: 100vh; }
main { flex: 1; }

/* 6. Badge dans une carte */
.carte { position: relative; }
.carte .badge { position: absolute; top: 10px; right: 10px; }
```

## Flexbox en une phrase

> `justify-content` = axe **principal**. `align-items` = axe **secondaire**.
> En `row`, principal = horizontal. En `column`, principal = vertical.

## Spécificité en une phrase

> Score `(id, classe, type)`, comparé case par case de gauche à droite.
> Une classe bat n'importe quel nombre de balises.

## Les réflexes de débogage

| Symptôme | Regarde d'abord |
|----------|-----------------|
| « Ma règle ne s'applique pas » | Spécificité (module 3), ordre des règles, faute de frappe dans le sélecteur |
| « Mon `width` est ignoré » | L'élément est `inline` (module 8) |
| « Ça déborde du parent » | `box-sizing` manquant, ou image sans `max-width` |
| « Défilement horizontal sur mobile » | Une largeur fixe, une image, ou un `100vw` + padding |
| « Mon `absolute` part n'importe où » | Le parent n'a pas `position: relative` |
| « Mon `sticky` ne colle pas » | Pas de `top` défini, ou `overflow: hidden` sur un parent |
| « Mon `z-index` est ignoré » | L'élément est `static`, ou contexte d'empilement du parent |
| « Espace bizarre sous mon image » | `display: block` manquant sur l'image |

## Tes trois outils quotidiens

1. **DevTools (F12)** — onglet Éléments : tu vois le box model en direct, tu modifies le CSS en live, tu vois quelles règles sont barrées (= écrasées). C'est ton meilleur professeur.
2. **MDN** (developer.mozilla.org, en français) — la référence. Cherche « MDN + nom de la propriété ».
3. **CSS-Tricks** — « A Complete Guide to Flexbox » et « A Complete Guide to Grid ». Mets-les en favori aujourd'hui.

---

# Ton programme d'aujourd'hui

| Bloc | Durée | Contenu |
|------|-------|---------|
| 1 | 45 min | Modules 1-4, en tapant chaque exemple. Fais les « À toi ». |
| 2 | 30 min | Modules 5-8 + applique une vraie typo à ta page du Jour 2. |
| 3 | **1 h 15** | **Module 9 + Flexbox Froggy (24 niveaux) + les 5 exercices** |
| 4 | 45 min | Module 10 + Grid Garden + la galerie `auto-fit` |
| 5 | 30 min | Modules 11-12 + rends ta landing page du Jour 7 impeccable en mobile |
| 6 | 45 min | Modules 13-17 : variables, transitions, ombres, `object-fit` — applique-les à ta landing page |
| 7 | 30 min | Module 18-19 : nettoie et réorganise ton CSS. Commit Git. |

**Le test de fin de journée.** Sans notes, en moins de 20 minutes :
> Une navbar responsive (logo à gauche, liens à droite, menu masqué sous 768px), une grille de 3 cartes qui devient 1 colonne sur mobile, un footer en 3 colonnes, et un bouton avec un `:hover` animé.

Si tu y arrives, le CSS est acquis. **Demain : Jour 8, Netlify + JavaScript.**

---

*Les questions que tu ne peux pas résoudre en 10 minutes : note-les et envoie-les-moi. On ne bloque pas seul.*
