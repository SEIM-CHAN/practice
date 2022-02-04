"use strict";

const array = ['a', 'b', 'c'];

const x = array.join("");

// console.log(x);

const array = ['a', 'b', 'c'];
let str = '';
const count = array.length;
for(var i = 0; i < count; i++) {
    str += array[i];
    console.log(str)
}