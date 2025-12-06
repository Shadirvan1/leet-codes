/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    d = s.trim()
    data = d.split(" ")
    n = data.length - 1
     le = data[n] 
     return le.length

};