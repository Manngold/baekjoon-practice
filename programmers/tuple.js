function solution(s) {
    var answer = [];

    s = s.slice(1, s.length - 1);

    let mode = false;
    let stack = [];

    for (let i of s) {
        if (mode) {
            if (i === ",") continue;
            else if (i === "}") {
                if (stack.length > answer.length) {
                    while (answer) {
                        answer.pop();
                    }
                    while (stack) {
                        answer.push(stack.pop());
                    }
                    mode = false;
                } else {
                    while (stack) {
                        stack.pop();
                    }
                    mode = false;
                }
            } else {
                stack.push(i);
            }
        } else {
            if (i === "{") mode = true;
        }
    }
    return answer;
}
