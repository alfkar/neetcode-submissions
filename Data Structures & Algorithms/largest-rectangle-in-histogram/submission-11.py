class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        maxSize = 0
        for i, height in enumerate(heights):
            if not stack:
                stack.append(tuple((i, height)))
                maxSize=height
            else:
                (index, prevHeight) = stack[-1]
                print("prevHeight: ", prevHeight)
                print("index: ", index)
                print("currentHeight: ", height)
                print("i: ", i)
                print("len(heights): ", len(heights))
                if(height==prevHeight):
                    volume=prevHeight*(i-index+1)
                    maxSize=max(volume,maxSize)
                while(stack and height<prevHeight):
                    volume=prevHeight*(i-index)
                    print("Volume: ", volume)
                    maxSize=max(volume,maxSize)
                    if(stack[-1][1]<= height):
                        break
                    if(i == len(heights)-1):
                        index+=1
                        break
                    (index, prevHeight) = stack.pop()
                if(height>prevHeight):
                    stack.append(tuple((i,height)))
                elif prevHeight != height:
                    stack.append(tuple((index,height)))
            print("Stack: ", stack)
        end_Index=stack[-1][0]
        while stack:
            (index, height) = stack.pop()
            maxSize = max(maxSize, height)
            if stack:
                (prevIndex, prevHeight) = stack[-1]
                volume=min(height, prevHeight)*(end_Index-prevIndex+1)
                maxSize = max(maxSize, volume)
        return maxSize

