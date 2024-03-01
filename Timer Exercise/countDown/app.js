function countDown(num){
   const time = setInterval(function(){
    num--;
    if(num <= 0){
        clearInterval(time);
        console.log("DONE!");
    }
    else{
        console.log(num);
    }
   },1000)
}