declare var require: any

function solution_bf(N:number, A:number[]) {
  console.log(A);
  return 0;
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
  for(let i = 1; i <= T * 2; i = i + 2) {
    const N = linesData[i];
    const A:number[] = linesData[i + 1].split(' ').map(item => +item)
    console.log(`Case #${(i + 1) / 2}: ${solution(+N, A)}`);
  }
})