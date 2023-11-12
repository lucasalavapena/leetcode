// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;

impl Solution {
    pub fn largest_values(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        if root.is_none() {
            return vec![];
        }
        let mut q = VecDeque::from(vec![root.unwrap()]);;
        let mut res = Vec::new();

        while !q.is_empty() {
            let q_len = q.len();
            let mut curr_max = i32::MIN;

            for _ in 0..q_len {
                let node = q.pop_front().unwrap();
                let node_ref = node.borrow();
                curr_max = curr_max.max(node_ref.val);

                if let Some(left) = node_ref.left.clone() {
                    q.push_back(left);
                }
                if let Some(right) = node_ref.right.clone() {
                    q.push_back(right);
                }
            }

            res.push(curr_max);
        }

        res
    }
}