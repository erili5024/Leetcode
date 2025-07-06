class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = Counter(tuple(seq) for seq in grid)
        transposed = list(zip(*grid))
        columns = Counter(tuple(seq) for seq in transposed)
        matching = set(rows.keys()) & set(columns.keys())
        counter = sum(rows[key] * columns[key] for key in matching)
        return counter



        