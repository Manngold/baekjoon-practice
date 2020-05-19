function solution(board, moves) {
    let answer = 0;
    let temp = [];

    for (let i in moves) {
        const t = moves[i] - 1;

        for (let j in board) {
            if (board[j][t]) {
                temp.push(board[j][t]);
                board[j][t] = 0;
                break;
            }
        }
    }
    let i = 0;
    while (i < temp.length - 1) {
        let next = i + 1;
        if (temp[i] === temp[next]) {
            temp.splice(i, 2);
            i = 0;
            answer += 2;
            continue;
        } else {
            i += 1;
        }
    }
    return answer;
}
