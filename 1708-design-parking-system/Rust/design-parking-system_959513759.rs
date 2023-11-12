struct ParkingSystem {
    remaining: [i32; 3]
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl ParkingSystem {

    fn new(big: i32, medium: i32, small: i32) -> Self {
        let remaining: [i32; 3] = [big, medium, small];
        Self{remaining}
    }
    
    fn add_car(&mut self, car_type: i32) -> bool {
        let idx = (car_type -1) as usize;
        if self.remaining[idx] > 0 {
            self.remaining[idx] -= 1;
            return true;
        }
        return false;
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * let obj = ParkingSystem::new(big, medium, small);
 * let ret_1: bool = obj.add_car(carType);
 */