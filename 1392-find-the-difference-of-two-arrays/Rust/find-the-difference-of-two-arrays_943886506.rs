use std::collections::HashSet;
use std::iter::FromIterator;

impl Solution {
    pub fn find_difference(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<Vec<i32>> {
        let a: HashSet<_> = HashSet::from_iter(nums1);
        let b: HashSet<_> = HashSet::from_iter(nums2);
        
            vec![
                Vec::from_iter(&a - &b),
                Vec::from_iter(&b - &a),
        ]
    }
}