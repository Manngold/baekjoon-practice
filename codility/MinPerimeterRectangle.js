function solution(N) {
  const answers = [];
  let cnt = 1;
  while (true) {
    if (N / cnt > cnt && N % cnt == 0) {
      answers.push((N / cnt + cnt) * 2);
    } else if (N / cnt == cnt && N % cnt == 0) {
      answers.push((cnt + cnt) * 2);
    } else if (N / cnt < cnt) {
      break;
    }
    cnt++;
  }
  return Math.min(...answers);
}
