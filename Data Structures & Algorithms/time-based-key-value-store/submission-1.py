class TimeMap:

    def __init__(self):
        self.time_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        values = self.time_map.get(key, [])
        values.append((timestamp, value))
        self.time_map[key] = values

        

    def get(self, key: str, timestamp: int) -> str:
        values = self.time_map.get(key, [])
        if not values:
            return ""

        l, r = 0, len(values) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if values[mid][0] == timestamp:
                return values[mid][1]
            elif timestamp < values[mid][0]:
                r = mid - 1
            else:
                l = mid + 1

        return values[r][1] if r >=0 else ""                
        
