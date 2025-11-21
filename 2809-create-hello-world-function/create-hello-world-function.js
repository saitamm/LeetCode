/**
 * @return {Function}
 */
var createHelloWorld = function() {
    const message = 'Hello World'
    return function(...args) {
        return message
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */