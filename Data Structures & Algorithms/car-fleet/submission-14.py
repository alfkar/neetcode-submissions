class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack = []
        pos_speed = sorted(zip(position,speed,[0]*len(position)),reverse=True)
        print("Start speed: ", pos_speed)
        for i, (pos,speed,seconds) in enumerate(pos_speed):
            print("-------- Index: ",i,"--------")
            print("Pos: ",pos," Speed: ", speed, " Seconds: ",seconds)
            print("Stack: ",stack)
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
                    print("1 Appended: ", stack[-1])
                else:
                    print("2 Appended: ", stack[-1])
                    stack.append(tuple((pos,speed,seconds)))
        return len(stack) 