function solution(A) {
  const right = {};
  const left = {};
  let answer = 0;
  for (const i of A) {
    if (right[i]) {
      right[i] += 1;
    } else {
      right[i] = 1;
    }
  }
  const max = Math.max(...Object.values(right));
  let leader = 0;
  for (const i in right) {
    if (right[i] == max) {
      leader = i;
      break;
    }
  }
  let l = 0;
  let r = A.length;
  for (const i of A) {
    right[i] -= 1;
    r -= 1;
    if (left[i]) {
      left[i] += 1;
    } else {
      left[i] = 1;
    }
    l += 1;
    if (left[leader] > l / 2 && right[leader] > r / 2) {
      answer += 1;
    }
  }
  return answer;
}
