'use strict';

function solution_bf(L, R) {
  let found
  let counter = 0

  for(L; L <= R; L++) {
    found = true;
    [...L.toString()].forEach((e, i) => {
      if ((i + 1) % 2 !== +e % 2) {
        found = false
      }
    })
    if(found) counter++
  }

  return counter
}





let solution = solution_bf

const { stdin, stdout } = require('process')
const readline = require('readline')
const rl = readline.createInterface({
  input: stdin,
  output: stdout,
  terminal: false
})

let linesData = []
rl.on('line', line => {
  linesData.push(line)
}).on('close', () => {
  let T = +linesData[0]
  for(let i = 1; i <= T; i++) {
    const [L, R] = linesData[i].split(' ')
    console.log(`Case #${i}: ${solution(+L, +R)}`)
  }
})