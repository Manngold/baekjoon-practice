function checker(arr, answers) {
    let i = 0;
    let cnt = 0;
    for (let k in answers) {
        if (arr[i] === answers[k]) cnt += 1;
        i += 1;
        if (i === arr.length) {
            i = 0;
        }
    }
    if (cnt) {
        return cnt;
    } else {
        return 0;
    }
}

function solution(answers) {
    let answer = [];

    let one = [1, 2, 3, 4, 5];
    let two = [2, 1, 2, 3, 2, 4, 2, 5];
    let three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

    const oneA = checker(one, answers);
    const twoA = checker(two, answers);
    const threeA = checker(three, answers);
    const max = Math.max(oneA, twoA, threeA);

    if (oneA === max) answer.push(1);
    if (twoA === max) answer.push(2);
    if (threeA === max) answer.push(3);

    return answer;
}
