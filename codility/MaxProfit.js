function solution(A) {
  let answer = 0;
  let min = A[0];
  for (let i = 1; i < A.length; i++) {
    if (A[i] - min > answer) {
      answer = A[i] - min;
    }
    min = Math.min(min, A[i]);
  }
  return answer;
}
