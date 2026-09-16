function createCounter (n){

    function dummy(){
        return n++;
    }

    return dummy;

}

console.log(createCounter());