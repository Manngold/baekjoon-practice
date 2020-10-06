function solution(A) {
  A = A.sort((x, y) => x - y);
  let one = A[0] * A[1] * A[A.length - 1];
  let two = A[A.length - 1] * A[A.length - 2] * A[A.length - 3];
  return Math.max(one, two);
}
