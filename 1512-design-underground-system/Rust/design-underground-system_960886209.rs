use std::collections::HashMap;

struct UndergroundSystem {
    checked_in: HashMap<i32, (String, i32)>,
    total: HashMap<(String, String), i32>,
    times: HashMap<(String, String), i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl UndergroundSystem {

    fn new() -> Self {
        Self{
                checked_in: HashMap::new(),
                total: HashMap::new(),
                times: HashMap::new(), 
        }
    }
    
    fn check_in(&mut self, id: i32, station_name: String, t: i32) {
        self.checked_in.insert(id, (station_name, t));
    }
    
    fn check_out(&mut self, id: i32, station_name: String, t: i32) {
        let (start_station, start_time) = &self.checked_in[&id];
        let key = (start_station.to_string(), station_name);
        self.total.entry(key.clone()).and_modify(|c| *c += t-start_time).or_insert(t-start_time);
        self.times.entry(key.clone()).and_modify(|c| *c += 1).or_insert(1);
    }
    
    fn get_average_time(&self, start_station: String, end_station: String) -> f64 {
        let key = (start_station, end_station);
        self.total[&key] as f64/self.times[&key] as f64
    }
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * let obj = UndergroundSystem::new();
 * obj.check_in(id, stationName, t);
 * obj.check_out(id, stationName, t);
 * let ret_3: f64 = obj.get_average_time(startStation, endStation);
 */