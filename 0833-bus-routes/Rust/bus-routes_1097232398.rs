// use std::collections::{VecDeque, HashSet, HashMap};


// impl Solution {
//     pub fn num_buses_to_destination(routes: Vec<Vec<i32>>, source: i32, target: i32) -> i32 {
//         let mut q = VecDeque::from([(source as usize, )]);
        
//         let mut bus_stops_to_route_idxs: HashMap<usize, Vec<usize>> = HashMap::new();
//         // we need seen for routes and buslocations if I am correct
//         // routes is obvious
//         // bus stops kinda too

//         // let mut seen_bus_stops = HashSet::new();
//         let mut seen_buses: HashSet<usize> = HashSet::new();
//         // seen_bus_stops.insert(source);

//         let mut steps = -1;

//         for (i, route) in routes.iter().enumerate() {
//             for bus in route {
//                 let bus_usize = *bus as usize;
//                 if let Some(values) = bus_stops_to_route_idxs.get_mut(&bus_usize) {
//                     values.push(i);
//                 } else {
//                     bus_stops_to_route_idxs.insert(bus_usize, vec![i]);
//                 }
//             }
//         }
//         let target_usize = target as usize;

//         while !q.is_empty() {
//             let q_len = q.len();
//             steps += 1;
//             for _ in 0..q_len {
//                 let current_loc = q.pop_front().unwrap();
//                 println!("{current_loc:?}");

//                 if current_loc == target_usize{
//                     return steps;
//                 }

//                 for route_idx in bus_stops_to_route_idxs.get(&current_loc) {
//                     // let valuesxx = bus_stops_to_route_idxs.get(&current_loc);
//                     // println!("{route_idx:?}");
//                     // println!("{valuesxx:?}");
//                     // for 
//                     for elem in route_idx {
//                         // println!("{elem:?}");
//                         let elem_usize = *elem as usize;
//                         for new_bus_stop in &routes[elem_usize] {
//                             if !seen_buses.contains(&elem) &&  !seen_bus_stops.contains(&new_bus_stop) {
//                                 seen_buses.insert(elem_usize);
//                                 seen_bus_stops.insert(*new_bus_stop);
//                                 q.push_back(*new_bus_stop as usize);
//                             }
//                         }
//                     }
//                 }
//             }

//         }
//         -1
//     }
// }

use std::collections::{HashSet, HashMap, VecDeque};


impl Solution {
    pub fn num_buses_to_destination(routes: Vec<Vec<i32>>, source: i32, target: i32) -> i32 {
        let mut q = VecDeque::new();
        q.push_back(source);

        let mut seen_routes = HashSet::new();
        let mut bus_stop_to_route_idx = HashMap::new();

        for (i, route) in routes.iter().enumerate() {
            for &bus_stop in route.iter() {
                bus_stop_to_route_idx.entry(bus_stop)
                    .or_insert_with(Vec::new)
                    .push(i);
            }
        }

        let mut steps = -1;
        while !q.is_empty() {
            let q_len = q.len();
            steps += 1;
            for _ in 0..q_len {
                if let Some(current_loc) = q.pop_front() {
                    if current_loc == target {
                        return steps;
                    }

                    if let Some(route_indices) = bus_stop_to_route_idx.get(&current_loc) {
                        for &route_idx in route_indices {
                            if !seen_routes.contains(&route_idx) {
                                for &bus_stop in &routes[route_idx] {
                                    q.push_back(bus_stop);
                                }

                                seen_routes.insert(route_idx);
                            }
                        }
                    }
                }
            }
        }

        -1
    }
}