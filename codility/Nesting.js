function solution(S) {
  const stack = [];
  for (const i of S) {
    if (i == '(') {
      stack.push(i);
    } else {
      if (stack.length > 0) {
        stack.pop();
      } else {
        return 0;
      }
    }
  }
  if (stack.length > 0) {
    return 0;
  } else {
    return 1;
  }
}
