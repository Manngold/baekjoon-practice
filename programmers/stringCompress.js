function solution(s) {
  let answer = s.length;
  for (let i = 1; i < Math.floor(s.length / 2) + 1; i++) {
    let temp = '';
    let cnt = 1;
    let arr = [];
    for (let j = 0; j < s.length; j += i) {
      arr.push(s.slice(j, j + i));
    }
    for (let a = 0; a < arr.length; a++) {
      if (arr[a] == arr[a + 1]) {
        cnt += 1;
      } else {
        if (cnt == 1) {
          temp += arr[a];
        } else {
          temp += String(cnt) + arr[a];
          cnt = 1;
        }
      }
    }
    if (temp.length < answer) {
      answer = temp.length;
    }
  }
  return answer;
}
