function solution(A) {
  const obj = {};
  for (const i in A) {
    if (obj[A[i]]) {
      obj[A[i]][0] += 1;
    } else {
      obj[A[i]] = [1, i];
    }
  }
  let max = 0;
  let idx = 0;
  for (const i in obj) {
    if (obj[i][0] > max) {
      max = obj[i][0];
      idx = obj[i][1];
    }
  }
  if (max > A.length / 2) {
    return Number(idx);
  } else {
    return -1;
  }
}
