function fizzbuzz() {
    for(let n=1 ;n<=100;n++) 
        {
        if(n%5===0 && n%3===0) {
            console.log('fizzbuzz');} 
        else if(n%5===0){
            console.log('buzz');}
        else if(n%3===0){
            console.log("fizz");}
        else {
            console.log(n);}
        
    }
}
fizzbuzz()