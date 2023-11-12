use std::collections::HashSet;

impl Solution {
    pub fn maximum_number_of_string_pairs(words: Vec<String>) -> i32 {
        let (count, _) = words.into_iter().fold((0, HashSet::new()), |(count, mut set), word| {
            let reversed_word: String = word.chars().rev().collect();
            if set.contains(&reversed_word) {
                set.remove(&reversed_word);
                (count + 1, set)
            } else {
                set.insert(word);
                (count, set)
            }
        });

        count
    }
}