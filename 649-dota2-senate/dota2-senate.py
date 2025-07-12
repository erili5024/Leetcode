class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        Rqueue = deque()
        Dqueue = deque()
        i = 0
        while i < len(senate):
            if senate[i] == 'R':
                Rqueue.append(i)
            if senate[i] =='D':
                Dqueue.append(i)
            i+= 1
        while Dqueue and Rqueue:
            if Dqueue[0] < Rqueue[0]:
                Rqueue.popleft()
                tempD = Dqueue.popleft()
                Dqueue.append(tempD + n)
            elif Rqueue[0] < Dqueue[0]:
                Dqueue.popleft()
                tempR = Rqueue.popleft()
                Rqueue.append(tempR + n)
        if Rqueue:
            return "Radiant"
        elif Dqueue:
            return "Dire"


        