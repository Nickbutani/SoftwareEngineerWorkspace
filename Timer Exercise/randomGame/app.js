function randomGame(){
    let num;
    let mult = 0;
    const game = setInterval(function(){
        num = Math.random();
        mult++;
        if(num > .75){
            clearInterval(game);
            console.log(num);
            console.log("It took "+ mult + " try") 
        }
        else{
            console.log(num);
        }
    }, 1000)
}