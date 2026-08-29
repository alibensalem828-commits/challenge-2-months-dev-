    `let fruits = ["pomme","fraises",'orange'];

console.log(fruits[fruits.length-1]);
console.log(fruits.length);

fruits.push("legume",'banani');
fruits.unshift('banane','poire');
fruits.pop();
fruits.shift();
console.log(fruits.includes("ALI"));
console.log(fruits.indexOf('pomme'));
fruits.unshift('fruit1',"fruit2","fruit3")
fruits.push("fruits-1","fruit-2")
fruit.splice(0,3);
console.log(fruits);`




let fruits=['pomme','poire','orange','banane'];
for(let fruit of fruits){console.log(`les ${fruit} cest bon` );}







let nombre=[2,3,5,6,7,8];
nombre.forEach(n =>{
    
    console.log(n*2);
    return n*2;
})

