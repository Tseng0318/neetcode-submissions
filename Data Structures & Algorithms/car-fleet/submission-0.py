class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
                # 1. Pair up positions and compute times
        cars = []
        for p, s in zip(position, speed):
            time = (target - p) / s
            cars.append((p, time))
        
        # 2. Sort by position descending (closest to target first)
        cars.sort(key=lambda x: x[0], reverse=True)
        
        # 3. Walk through, counting fleets
        fleets = 0
        leading_time = 0   # time of the most recent fleet ahead
        
        for p, t in cars:
            # if t > leading_time, this car starts a new fleet
            # update leading_time accordingly
            if t > leading_time:
                fleets += 1
                leading_time = t
        
        return fleets
        