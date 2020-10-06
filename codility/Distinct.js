function solution(A) {
  let dic = {};
  for (const i of A) {
    if (dic[i]) {
      dic[i] += 1;
    } else {
      dic[i] = 1;
    }
  }
  return Object.keys(dic).length;
}
