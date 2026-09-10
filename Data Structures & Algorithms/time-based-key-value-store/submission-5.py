class TimeMap:
    NAME_MAP = {}
    def __init__(self):
        self.NAME_MAP = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.NAME_MAP.get(key, []):
            self.NAME_MAP[key].append([value,timestamp])
        else:
            self.NAME_MAP[key] = [[value,timestamp]]
    def get(self, key: str, timestamp: int) -> str:
        if self.NAME_MAP.get(key, None):
            lo = 0
            hi = len(self.NAME_MAP[key])-1
            while lo < hi:
                mid = (lo+hi)//2
                if self.NAME_MAP[key][mid][1] >= timestamp:
                    hi = mid
                else:
                    lo = mid + 1
            if self.NAME_MAP[key][hi][1] <= timestamp:
                return self.NAME_MAP[key][hi][0]
            elif self.NAME_MAP[key][hi-1][1] <= timestamp:
                return self.NAME_MAP[key][hi-1][0]
            else:
                return ""
        else:
            return ""

