impl Solution {
    pub fn buy_choco(prices: Vec<i32>, money: i32) -> i32 {
        let mut first = 100;
        let mut second = 100;

        for p in prices {
            if p < first {
                second = first;
                first = p;
            }
            else if p < second {
                second = p;
            }
        }

        let remaining = money - first - second;
        if remaining >= 0 {
            return remaining; 
        }
        return money;
    }
}