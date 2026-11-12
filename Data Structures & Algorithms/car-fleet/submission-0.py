class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. Compute (pos, time) pairs
        cars = [
            (p, (target - p) / s)
            for p, s in zip(position, speed)
        ]

        # 2) sort by starting position, descending 
        cars.sort(reverse=True, key=lambda x: x[0])

        fleets = 0
        slowest = 0.0

        # 3) scan and count fleets
        for _, time in cars:
            if time > slowest:
                fleets += 1
                slowest = time
                # This car starts a new fleet
            # otherwise it joins the fleet with arrival time = slowest

        return fleets



