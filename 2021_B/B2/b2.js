"use strict";
function solution_bf(N, A) {
    console.log(A);
    return 0;
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
    for (var i = 1; i <= T * 2; i = i + 2) {
        var N = linesData[i];
        var A = linesData[i + 1].split(' ').map(function (item) { return +item; });
        console.log("Case #" + (i + 1) / 2 + ": " + solution(+N, A));
    }
});
