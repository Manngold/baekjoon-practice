// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A, B) {
  const answer = [];
  const stack = [];
  for (let i = 0; i < A.length; i++) {
    const fish = A[i];
    const d = B[i];
    if (d == 0) {
      while (stack.length > 0) {
        const down = stack.pop();
        if (down > fish) {
          stack.push(down);
          break;
        }
      }
      if (stack.length == 0) {
        answer.push(fish);
      }
    } else {
      stack.push(fish);
    }
  }
  return answer.length + stack.length;
}
