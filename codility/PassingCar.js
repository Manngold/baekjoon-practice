function solution(A) {
  let answer = 0;
  let car = 0;
  for (const i of A) {
    if (i == 0) {
      car += 1;
    } else {
      answer += car * i;
    }
  }
  if (answer > 1000000000) {
    return -1;
  }
  return answer;
}
