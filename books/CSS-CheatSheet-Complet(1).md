# 📘 CSS — La Doc Complète (version "je teste tout")

> Copie-colle chaque bloc dans ton `.css`, change les valeurs, regarde ce qui bouge. C'est comme ça qu'on retient.

---

## 1. SYNTAXE DE BASE (pour éviter tes erreurs actuelles)

```css
selecteur {
    propriete: valeur;   /* toujours un point-virgule à la fin, PAS un deux-points */
}
```

⚠️ Erreurs classiques (celles que tu as eues) :
- `p , {` → virgule sans rien après = erreur. Écris `p {` ou `p, div {`
- `color: red :` → deux-points au lieu de point-virgule. Écris `color: red;`
- Une accolade `{` ouverte sans `}` fermée = tout le reste plante.

---

## 2. SÉLECTEURS (comment cibler un élément)

| Sélecteur | Exemple | Cible |
|---|---|---|
| Élément | `p {}` | tous les `<p>` |
| Classe | `.special {}` | tous les `class="special"` |
| ID | `#header {}` | l'élément `id="header"` |
| Universel | `* {}` | absolument tout |
| Groupé | `h1, h2, p {}` | tous ceux listés |
| Descendant | `nav li {}` | tout `li` dans un `nav` (peu importe la profondeur) |
| Enfant direct | `nav > li {}` | seulement les `li` enfants directs de `nav` |
| Frère adjacent | `h1 + p {}` | le `p` juste après un `h1` |
| Frères généraux | `h1 ~ p {}` | tous les `p` après un `h1` |
| Attribut | `input[type="text"] {}` | inputs avec cet attribut |
| Attribut contient | `a[href*="pdf"] {}` | href qui contient "pdf" |

### Pseudo-classes (état de l'élément)
```css
a:hover {}        /* souris dessus */
a:active {}       /* pendant le clic */
a:visited {}      /* lien déjà visité */
input:focus {}    /* champ actif */
input:disabled {} /* champ désactivé */
li:first-child {}
li:last-child {}
li:nth-child(2) {}       /* le 2e */
li:nth-child(odd) {}     /* impairs */
li:nth-child(even) {}    /* pairs */
li:nth-child(3n) {}      /* tous les multiples de 3 */
p:not(.special) {}       /* tous SAUF ceux avec .special */
```

### Pseudo-éléments (créer/cibler une partie)
```css
p::before { content: "→ "; }   /* insère du contenu avant */
p::after { content: " ✔"; }    /* insère du contenu après */
p::first-line {}
p::selection {}                 /* texte sélectionné par l'utilisateur */
input::placeholder {}
```

---

## 3. LE BOX MODEL (la base de tout layout)

```css
div {
    width: 200px;
    height: 100px;
    padding: 10px;        /* espace intérieur, entre le contenu et la bordure */
    border: 2px solid black;
    margin: 20px;          /* espace extérieur, entre la bordure et les autres éléments */
    box-sizing: border-box; /* ⭐ TRÈS utile : width inclut padding+border, plus simple à calculer */
}
```

Raccourcis directionnels :
```css
padding: 10px;                  /* les 4 côtés */
padding: 10px 20px;             /* haut/bas 10px, gauche/droite 20px */
padding: 10px 20px 5px 15px;    /* haut droite bas gauche (sens horaire) */
padding-top: 10px;
padding-right: 10px;
padding-bottom: 10px;
padding-left: 10px;
/* même logique pour margin */
```

---

## 4. DISPLAY & POSITION (comment les éléments s'organisent)

```css
display: block;        /* prend toute la largeur, saut de ligne (div, p) */
display: inline;       /* colle aux autres, pas de width/height possible (span, a) */
display: inline-block; /* comme inline mais accepte width/height */
display: none;         /* disparaît complètement (ne prend plus de place) */
display: flex;         /* voir section 5 */
display: grid;         /* voir section 6 */
```

```css
position: static;      /* comportement normal, par défaut */
position: relative;    /* décalé par rapport à SA position normale */
position: absolute;    /* sorti du flux, positionné par rapport au parent positionné le plus proche */
position: fixed;       /* collé à l'écran, ne bouge pas au scroll */
position: sticky;      /* colle quand on scroll jusqu'à un point donné */

top: 0; right: 0; bottom: 0; left: 0;  /* utilisé avec absolute/fixed/sticky */
z-index: 10;  /* qui passe devant qui (plus grand = devant) */
```

---

## 5. FLEXBOX (alignement en ligne/colonne — le plus utilisé aujourd'hui)

```css
.container {
    display: flex;
    flex-direction: row;      /* row | row-reverse | column | column-reverse */
    justify-content: center;  /* alignement horizontal : flex-start | center | flex-end | space-between | space-around | space-evenly */
    align-items: center;      /* alignement vertical : flex-start | center | flex-end | stretch */
    flex-wrap: wrap;          /* les éléments passent à la ligne si pas de place */
    gap: 20px;                /* espace entre les éléments, plus propre que margin */
}

.item {
    flex: 1;           /* grandit pour remplir l'espace dispo (équivalent) */
    flex-grow: 1;      /* facteur de grandissement */
    flex-shrink: 1;    /* facteur de rétrécissement */
    flex-basis: 200px; /* taille de départ avant grow/shrink */
    align-self: flex-end; /* override align-items pour CET élément seul */
}
```

---

## 6. GRID (grille 2D — lignes ET colonnes)

```css
.container {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;      /* 3 colonnes égales */
    grid-template-columns: repeat(3, 1fr);   /* raccourci identique */
    grid-template-rows: 100px auto 50px;
    gap: 20px;                               /* espace lignes + colonnes */
    row-gap: 10px;
    column-gap: 20px;
}

.item {
    grid-column: 1 / 3;   /* de la ligne 1 à la ligne 3 (span 2 colonnes) */
    grid-row: 2 / 4;
    grid-column: span 2;  /* raccourci : occupe 2 colonnes */
}
```

---

## 7. TYPOGRAPHIE (texte)

```css
font-family: "Helvetica", Arial, sans-serif;  /* liste de secours si la 1ère n'existe pas */
font-size: 16px;         /* px, em, rem, % */
font-weight: bold;       /* normal | bold | 100 à 900 */
font-style: italic;
line-height: 1.5;        /* espace entre les lignes, souvent sans unité = multiplicateur */
text-align: center;      /* left | right | center | justify */
text-decoration: underline; /* none | underline | line-through */
text-transform: uppercase;  /* lowercase | capitalize */
letter-spacing: 2px;
word-spacing: 4px;
white-space: nowrap;     /* empêche le retour à la ligne */
text-overflow: ellipsis; /* affiche "..." si texte trop long (avec overflow:hidden) */
```

---

## 8. COULEURS & FONDS

```css
color: red;                    /* couleur du texte */
color: #ff0000;                /* hexadécimal */
color: rgb(255, 0, 0);
color: rgba(255, 0, 0, 0.5);   /* avec transparence (alpha) */
color: hsl(0, 100%, 50%);

background-color: cadetblue;
background-image: url("image.jpg");
background-size: cover;        /* couvre tout sans déformer */
background-position: center;
background-repeat: no-repeat;

opacity: 0.5;  /* transparence de TOUT l'élément (contenu inclus) */
```

---

## 9. BORDURES & ARRONDIS

```css
border: 2px solid black;       /* épaisseur style couleur */
border-radius: 10px;           /* coins arrondis */
border-radius: 50%;            /* cercle parfait si width = height */
border-top: 1px dashed grey;   /* juste un côté */
box-shadow: 2px 2px 10px rgba(0,0,0,0.3); /* x y flou couleur */
outline: 1px solid blue;       /* contour, ne prend pas de place (utile en debug) */
```

---

## 10. UNITÉS (lesquelles utiliser)

| Unité | C'est quoi |
|---|---|
| `px` | pixel fixe |
| `%` | relatif au parent |
| `em` | relatif à la taille de police du PARENT |
| `rem` | relatif à la taille de police RACINE (html) — plus prévisible, ⭐ recommandé |
| `vw` / `vh` | % de la largeur/hauteur de la fenêtre (viewport) |
| `fr` | fraction, utilisé en grid |
| `auto` | calculé automatiquement |

---

## 11. TRANSITIONS & ANIMATIONS

```css
/* Transition : anime un changement d'état (ex: hover) */
button {
    transition: background-color 0.3s ease-in-out;
}
button:hover {
    background-color: darkred;
}

/* Animation : boucle/séquence autonome */
@keyframes rebond {
    0%   { transform: translateY(0); }
    50%  { transform: translateY(-20px); }
    100% { transform: translateY(0); }
}
div {
    animation: rebond 1s infinite;
}
```

---

## 12. TRANSFORM (déplacer/tourner/zoomer sans casser le layout)

```css
transform: translate(20px, 10px); /* déplace */
transform: rotate(45deg);         /* tourne */
transform: scale(1.5);            /* zoom x1.5 */
transform: skew(10deg);           /* incline */
transform: translateX(50%);
```

---

## 13. VARIABLES CSS (custom properties)

```css
:root {
    --couleur-principale: cadetblue;
    --espacement: 16px;
}

div {
    color: var(--couleur-principale);
    padding: var(--espacement);
}
```

---

## 14. MEDIA QUERIES (responsive / mobile)

```css
/* Par défaut = mobile-first, puis on ajoute pour grand écran */
.container {
    flex-direction: column;
}

@media (min-width: 768px) {
    .container {
        flex-direction: row;   /* changement à partir de 768px */
    }
}

@media (max-width: 480px) {
    body { font-size: 14px; } /* pour petits écrans uniquement */
}
```

---

## 15. AUTRES TRUCS PRO UTILES

```css
cursor: pointer;              /* main au survol (liens/boutons custom) */
overflow: hidden;             /* cache ce qui dépasse */
overflow: auto;               /* scrollbar si besoin */
visibility: hidden;           /* invisible MAIS garde sa place (contrairement à display:none) */
object-fit: cover;            /* pour <img>, comme background-size */
filter: blur(5px);            /* flou, luminosité, etc. */
filter: grayscale(100%);
backdrop-filter: blur(10px);  /* flou de ce qu'il y a DERRIÈRE (effet verre) */
aspect-ratio: 16 / 9;         /* garde un ratio fixe */
scroll-behavior: smooth;      /* scroll fluide vers les ancres */
```

---

## 16. ORDRE DE PRIORITÉ (specificity) — pourquoi ton style ne s'applique pas

Du plus faible au plus fort :
1. `p {}` — élément
2. `.classe {}` — classe
3. `#id {}` — id
4. `style="..."` inline dans le HTML
5. `!important` — force tout, à utiliser en dernier recours seulement

```css
p { color: blue !important; } /* gagne contre tout sauf un autre !important plus précis */
```

---

## 🧪 Comment tester vite (pour toi, dans VS Code)

1. Ouvre ton fichier `.html` avec l'extension **Live Server** → ça recharge auto à chaque sauvegarde.
2. Isole un bloc de test dans un `<div class="test">` séparé pour pas casser le reste.
3. Utilise l'inspecteur du navigateur (`F12` → onglet Elements) pour éditer le CSS EN DIRECT et voir l'effet avant de le copier dans ton fichier.
## commentaire du css 
/* commentaire */
