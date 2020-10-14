function solution(A) {
  let partSum = 0;
  let maxSum = -1000000;
  for (const i of A) {
    maxSum = Math.max(maxSum, partSum + i);
    partSum = Math.max(0, partSum + i);
  }
  return maxSum;
}
