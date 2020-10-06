function solution(A) {
  let answer = 0;
  let min = (A[0] + A[1]) / 2;
  let three = 0;
  let two = 0;

  for (let i = 2; i < A.length; i++) {
    three = (A[i] + A[i - 1] + A[i - 2]) / 3;
    two = (A[i] + A[i - 1]) / 2;

    if (three < min) {
      min = three;
      answer = i - 2;
    }
    if (two < min) {
      min = two;
      answer = i - 1;
    }
  }

  return answer;
}
