let nombres= [1,2,3,4];
let doubles= nombres.map(n=>n*2);

console.log(doubles);
console.log(nombres);

let argent=[199,44,32,23];
let objeectif=argent.map(n=>{
    return n*2;
});
console.log(objeectif)
let clients = [
    { nom: "Ali", budget: 500 },
    { nom: "Sara", budget: 1200 }
];

let trouve = clients.find(client => client.nom === "Sara");

console.log(trouve); 
let clients = [
    { nom: "Ali", budget: 500 },
    { nom: "Sara", budget: 1200 },
    { nom: "Tom", budget: 300 }
];

let riches = clients.filter(client => client.budget > 400);

console.log(riches);  



