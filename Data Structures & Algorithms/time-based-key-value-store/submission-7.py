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
            entries = self.NAME_MAP[key]
            lo = 0
            hi = len(entries)-1
            while lo < hi:
                mid = (lo+hi+1)//2
                if entries[mid][1] <= timestamp:
                    lo = mid
                else:
                    hi = mid - 1
            return entries[hi][0] if entries[hi][1] <= timestamp else ""
        else:
            return ""