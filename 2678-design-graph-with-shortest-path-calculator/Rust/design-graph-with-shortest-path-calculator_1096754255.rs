use std::collections::{HashMap, HashSet, BinaryHeap};
use std::cmp::Reverse;

struct Graph {
    graph: HashMap<i32, HashSet<(i32, i32)>>,
    n: i32,
}

impl Graph {
    fn new(n: i32, edges: Vec<Vec<i32>>) -> Self {
        let mut graph = HashMap::new();
        for edge in edges {
            let (src, dest, weight) = (edge[0], edge[1], edge[2]);

            graph.entry(src)
                .or_insert_with(HashSet::new)
                .insert((dest, weight));
        }
        Graph { graph, n }
    }

    fn add_edge(&mut self, edge: Vec<i32>) {
        let (src, dest, weight) = (edge[0], edge[1], edge[2]);
        self.graph.entry(src)
                .or_insert_with(HashSet::new)
                .insert((dest, weight));
    }
    
    fn shortest_path(&self, node1: i32, node2: i32) -> i32 {
        let mut dist: Vec<i32> = vec![i32::MAX; self.n as usize];
        dist[node1 as usize] = 0;

        // Reverse to use min heap
        let mut heap = BinaryHeap::from(vec![Reverse((0, node1))]);

        while !heap.is_empty() {
            let Reverse((curr_dist, curr_node)) = heap.pop().unwrap();

            if curr_node == node2 {
                return curr_dist;
            }
            if let Some(neighbours) = self.graph.get(&curr_node) {  

                for &(neigh, edge_weight) in neighbours.iter() {
                    let cand_dist = curr_dist + edge_weight;

                    if cand_dist < dist[neigh as usize] {
                        dist[neigh as usize] = cand_dist;
                        heap.push(Reverse((cand_dist, neigh)));
                    }
                }
            }
        }

        return -1;



    }
}



