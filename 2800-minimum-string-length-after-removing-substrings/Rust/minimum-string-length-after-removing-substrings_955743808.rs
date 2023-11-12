impl Solution {
    pub fn min_length(s: String) -> i32 {
        let mut stack: Vec<char> = Vec::new();;

        for c in s.chars() {
            let l = stack.len();
            if l > 0 && ( (stack[l-1] == 'A' && c == 'B') || (stack[l-1] == 'C' && c == 'D') ){
                stack.pop();
            }
            else {
                stack.push(c);
            }
        }
        stack.len() as i32
    }
}