function direbonjour(a) {
    console.log("bonjour");
    while(a<15){
        a++;console.log(a)
    }
}
direbonjour(10);
function bonjour(nom){
    console.log(`hi ${nom}`);

}
bonjour('ali');
function saluer(prenom) {
  console.log(`$(prenom)`);
}

saluer("Alice");   
saluer("Karim");   
function afficheDouble(n) {
    console.log(n * 2);   
}
function renvoieDouble(n) {
    return n * 2;         
}
renvoieDouble(2);
afficheDouble(2);
const test = x => {
    if(x<18){return "mineur";   }
    else{
        return "majeur"
    }
}
console.log(test(19));

let addition= n => 
    console.log(n*2);
addition(3);
const addition1=n => {
    return n/3;
};  
const max=(a, b) => {if(a<b)
    return b;
    else 
    return a;
}
console.log(max(3,4))