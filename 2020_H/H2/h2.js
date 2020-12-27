"use strict";
function solution_bf(L, R) {
    var found = false;
    var counter = 0;
    for (L; L <= R; L++) {
        found = true;
        [L.toString()].forEach(function (e, i) {
            if ((i + 1) % 2 !== +e % 2) {
                found = false;
            }
        });
        if (found)
            counter++;
    }
    return counter;
}
var solution = solution_bf;
var _a = require('process'), stdin = _a.stdin, stdout = _a.stdout;
var readline = require('readline');
var rl = readline.createInterface({
    input: stdin,
    output: stdout,
    terminal: false
});
var linesData = [];
rl.on('line', function (line) {
    linesData.push(line);
}).on('close', function () {
    var T = +linesData[0];
    for (var i = 1; i <= T; i++) {
        var _a = linesData[i].split(' '), L = _a[0], R = _a[1];
        console.log("Case #" + i + ": " + solution(+L, +R));
    }
});
