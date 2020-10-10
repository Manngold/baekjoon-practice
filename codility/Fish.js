// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A, B) {
  const up = [];
  const down = [];
  for (let i = 0; i < A.length; i++) {
    const fish = A[i];
    const d = B[i];
    if (d == 0) {
      while (down.length > 0) {
        const last = down.pop();
        if (last > fish) {
          down.push(last);
          break;
        }
      }
      if (down.length == 0) {
        up.push(fish);
      }
    } else if (d == 1) {
      while (up.length > 0) {
        const last = up.pop();
        if (last > fish) {
          up.push(last);
          break;
        }
      }
      if (up.length == 0) {
        down.push(fish);
      }
    }
  }
  return up.length + down.length;
}
