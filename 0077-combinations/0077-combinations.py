class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []  # List to store all combinations
        combination = []  # Temporary list for current combination
    
        # Backtracking function
        def backtrack(start):
            # Base case: combination complete
            if len(combination) == k:
                result.append(combination.copy())
                return
            
            # Explore numbers from 'start' to 'n'
            for num in range(start, n + 1):
                combination.append(num)
                # Recurse with next starting number (num + 1)
                backtrack(num + 1)
                # Backtrack
                combination.pop()
        
        # Start recursion from 1
        backtrack(1)
        return result