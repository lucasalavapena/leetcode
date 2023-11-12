use std::collections::{HashSet};
impl Solution {
    pub fn num_buses_to_destination(routes: Vec<Vec<i32>>, source: i32, target: i32) -> i32 {
        let mut dist_from_source = vec![501 as i16; 1000001];
        dist_from_source[source as usize] = 0;
        let mut visited = HashSet::new();
        let mut count = 0;
        
        while visited.len() < routes.len() && count < routes.len() {
            for route_idx in 0..routes.len() {
                if visited.contains(&route_idx) {
                    continue;
                }

                let mut min_dist_to_route = 501 as i16;
                for bus in routes[route_idx].iter() {
                    min_dist_to_route = std::cmp::min(min_dist_to_route, dist_from_source[*bus as usize] + 1);
                }
                for bus in routes[route_idx].iter() {
                    dist_from_source[*bus as usize] = std::cmp::min(dist_from_source[*bus as usize], min_dist_to_route);
                }
                if min_dist_to_route < 501 {
                    visited.insert(route_idx);
                }
            }
            count += 1;
        }
        if dist_from_source[target as usize] == 501 {
            -1
        } else {
            dist_from_source[target as usize] as i32
        }
    }
}