impl Solution {
    pub fn make_smallest_palindrome(s: String) -> String {
        let end = s.len();
        let mut s_vec: Vec<char> = s.chars().collect();

        for i in 0..end/2 {
            if s_vec[i] != s_vec[end - i - 1] {
                let smaller = std::cmp::min(s_vec[i], s_vec[end - i - 1]);
                s_vec[i] = smaller;
                s_vec[end - i - 1] = smaller;
            }
        } 

        s_vec.into_iter().collect()
    }
}