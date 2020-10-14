function solution(N) {
  const answer = [];
  let cnt = 1;
  while (true) {
    if (N / cnt > cnt && N % cnt == 0) {
      answer.push(cnt);
      answer.push(N / cnt);
    } else if (N / cnt == cnt && N % cnt == 0) {
      answer.push(cnt);
    } else if (N / cnt < cnt) {
      break;
    }
    cnt++;
  }
  return answer.length;
}
