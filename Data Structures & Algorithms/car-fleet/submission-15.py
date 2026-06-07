class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack = []
        pos_speed = sorted(zip(position,speed,[0]*len(position)),reverse=True)
        for i, (pos,speed,seconds) in enumerate(pos_speed):
            seconds = (target-pos)/speed
            if not stack:
                stack.append(tuple((pos,speed,seconds)))
            else:
                (infront_pos, infront_speed,infront_seconds)=stack[-1]
                if(infront_seconds >= seconds):
                    pos=infront_pos
                    seconds=infront_seconds
                    stack.pop()
                    stack.append(tuple((pos,speed,seconds)))
                else:
                    stack.append(tuple((pos,speed,seconds)))
        return len(stack) 