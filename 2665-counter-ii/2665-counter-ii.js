var createCounter = function(init) {

    let counter = init;

    return {
        increment : function(){
            counter++;
            return counter;
        },
        decrement : function(){
            counter--;
            return counter;
        },
        reset : function(){
            counter = init;
            return counter;
        },
        getValue : function(){
            return counter;
        }

    }
    
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */