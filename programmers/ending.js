function solution(n, words) {
    let answer = [];
    let simChecker = [];
    let turn = 1;
    let num = 1;
    for (let i in words) {
        const word = words[i];
        const isValid = simChecker.find((element) => element === word);
        const lastWord = simChecker[simChecker.length - 1];
        if (isValid) {
            answer = [num, turn];
            break;
        } else {
            if (
                simChecker.length !== 0 &&
                lastWord[lastWord.length - 1] !== word[0]
            ) {
                answer = [num, turn];
                break;
            } else {
                simChecker.push(word);
                if (num + 1 > n) {
                    turn += 1;
                    num = 1;
                } else {
                    num += 1;
                }
            }
        }
    }

    if (answer.length === 0) {
        answer = [0, 0];
    }

    return answer;
}
