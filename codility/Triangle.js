// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
  A = A.sort((x, y) => x - y);
  let answer = 0;
  for (let i = A.length - 2; i >= 1; i--) {
    const r = A[i + 1];
    const p = A[i];
    const q = A[i - 1];

    if (r < p + q && p < q + r && q < r + p) {
      answer += 1;
      break;
    }
  }
  return answer;
}
