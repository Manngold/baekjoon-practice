function solution(S) {
  const stack = [];
  for (const i of S) {
    if (i === '(' || i === '{' || i === '[') {
      stack.push(i);
    } else {
      const last = stack.pop();
      if (i === ')' && last === '(') {
        continue;
      } else if (i === '}' && last === '{') {
        continue;
      } else if (i === ']' && last === '[') {
        continue;
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
