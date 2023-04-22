class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        box_types_sorted = sorted(boxTypes, key=lambda x: x[1], reverse = True)
        res = 0
        
        for boxes, units_per_box in box_types_sorted:
            possible_boxes = min(truckSize, boxes)
            truckSize -= possible_boxes
            res += possible_boxes * units_per_box
            
            if truckSize == 0:
                return res
        return res