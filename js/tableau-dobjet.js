let clients = [
{nom:'aly',metier:'dev' ,age:19},
{nom:'argent',metier:'sdf',age:29},
{nom:'mark',metier:'passant',age:49},
{nom:'paul',metier:'bricoleur',age:59},

];
for (let client of clients){if(client.age < 50) {
    console.log(`c'est moi ${client.nom} ravis de faire votre connaissance je suis ${client.metier} et j'ai ${client.age}`
);}}




console.log(clients[1]);
console.log(clients[0].nom);