function solution(d, budget) {
    let answer = 0;
    let storage = 0;
    d = d.sort((a, b) => a - b);
    for (let i in d) {
        storage += d[i];
        if (storage <= budget) {
            answer += 1;
        } else {
            break;
        }
    }

    return answer;
}
