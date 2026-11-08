let produits = [
    { nom: "Clavier", prix: 50, stock: true },
    { nom: "Souris", prix: 25, stock: false },
    { nom: "Écran", prix: 200, stock: true },
    { nom: "Câble", prix: 10, stock: true }
];

let noms=produits.map(n=>n.nom);
console.log(noms)


let produits = [
    { nom: "Clavier", prix: 50, stock: true },
    { nom: "Souris", prix: 25, stock: false },
    { nom: "Écran", prix: 200, stock: true },
    { nom: "Câble", prix: 10, stock: true }
];

let garder=produits.filter(p=>p.prix>50)


let produits = [
    { nom: "Clavier", prix: 50, stock: true },
    { nom: "Souris", prix: 25, stock: false },
    { nom: "Écran", prix: 200, stock: true },
    { nom: "Câble", prix: 10, stock: true }
];

let nom1=produits
.map(n=>n.nom)
.filter(n=>n.prix)
.filter(n=>n.stock===true)

