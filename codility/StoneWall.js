function solution(H) {
    let count = 0
    const stack = []
    for(const i of H){
        while(stack.length > 0 && stack[stack.length - 1] > i){
            stack.pop()
        }
        if(stack.length == 0 || stack[stack.length - 1] < i){
            stack.push(i)
            count++
        }
    }
    return count
}