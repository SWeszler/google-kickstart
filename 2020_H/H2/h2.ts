declare var require: any

function solution_bf(L:number, R:number) {
  let found: boolean = false;
  let counter: number = 0;

  for(L; L <= R; L++) {
    found = true;
    L.toString().split('').forEach((e, i) => {
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

let linesData: Array<string> = []
rl.on('line', (line:string) => {
  linesData.push(line)
}).on('close', () => {
  let T:number = +linesData[0]
  for(let i = 1; i <= T; i++) {
    const [L, R] = linesData[i].split(' ')
    console.log(`Case #${i}: ${solution(+L, +R)}`)
  }
})