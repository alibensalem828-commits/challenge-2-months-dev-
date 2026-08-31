let produits = [
    { nom: "Clavier", prix: 50, stock: true },
    { nom: "Souris", prix: 25, stock: false },
    { nom: "Écran", prix: 200, stock: true },
    { nom: "Câble", prix: 10, stock: true }
];

let noms=produits.map(n=>n.nom);
console.log(noms)