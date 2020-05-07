function solution(participant, completion) {
    let answer = "";

    participant = participant.sort();
    completion = completion.sort();
    console.log(participant, completion);
    for (let i in participant) {
        if (participant[i] !== completion[i]) {
            answer = participant[i];
            break;
        }
    }

    return answer;
}
