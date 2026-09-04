/**
 * @param {Object} obj
 * @return {Function}
 */
Function.prototype.bindPolyfill = function(obj) {
  var fn = this;
  return function() {
    return fn.apply(obj, arguments);
  };
};