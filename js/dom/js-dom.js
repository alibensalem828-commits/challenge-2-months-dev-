console.log("bonjour")


let titre = document.querySelector("#titre")
titre.textContent="jai change le titre avec js !"

let liste = document.querySelector("#liste")
liste.textContent='liste de la recherche queyselector'
let item=document.createElement("li") ;
liste.append(item)
let produits = [
    { nom: "Clavier", prix: 50 },
    { nom: "Souris", prix: 25 },
    { nom: "Écran", prix: 200 }
];

let liste = document.querySelector("#liste");

produits.forEach(produit => {
    let item = document.createElement("li");             // 1. CRÉER (un <li> par produit)
    item.textContent = `${produit.nom} : ${produit.prix} €`;  // 2. REMPLIR avec les infos
    liste.append(item);                                   // 3. ACCROCHER dans la liste
});