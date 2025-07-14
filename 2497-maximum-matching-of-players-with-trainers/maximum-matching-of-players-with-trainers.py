class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        counter = 0 
        trainers.sort()
        for i in players:
            if not trainers:
                break
            index = bisect.bisect_left(trainers, i)
            if len(trainers) > index:
                counter += 1
                trainers.pop(index)
        return counter
                
            
            
        