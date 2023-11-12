impl Solution {
    pub fn make_smallest_palindrome(s: String) -> String {
        let mut bytes = s.as_bytes().to_vec();
        let mut left = 0;
        let mut right = s.len() - 1;
        
        while left < right {
            let byte = bytes[left].min(bytes[right]);
            bytes[left] = byte;
            bytes[right] = byte;
            left += 1;
            right -= 1;
        }
        String::from_utf8(bytes).unwrap()
    }
}