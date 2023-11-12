impl Solution {
    pub fn check_straight_line(coordinates: Vec<Vec<i32>>) -> bool {

        let x1 = coordinates[0][0];
        let y1 = coordinates[0][1];
        let x2 = coordinates[1][0];
        let y2 = coordinates[1][1];

        let run = (x2 - x1);
        if run == 0 {
            let all_first_elements_are_zero = coordinates.iter().all(|coord| coord[0] == x1);
            if all_first_elements_are_zero {
                return true;
            }
            else {
                return false;
            }
        }
        let m: f64 = (y2 - y1) as f64 / (run) as f64;
        let c: f64 = y1 as f64 - m * x1 as f64;
        let line_fn = |x| m * x + c;

        let remaining_coords = coordinates.iter().skip(2);
        for coord in remaining_coords {
            if (line_fn(coord[0] as f64) != coord[1] as f64) {
                return false;
            }
        }
        return true;
    }
}