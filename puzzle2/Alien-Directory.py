from collections import defaultdict, deque

def alien_order(words):
    # Step 1: Build graph and in-degree map
    graph = defaultdict(set)
    in_degree = defaultdict(int)
    
    # Initialize in-degree for all unique characters
    for word in words:
        for char in word:
            in_degree[char] = 0

    # Step 2: Compare adjacent words to create edges
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        min_len = min(len(word1), len(word2))

        for j in range(min_len):
            if word1[j] != word2[j]:
                # Add edge word1[j] -> word2[j]
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].add(word2[j])
                    in_degree[word2[j]] += 1
                break
        else:
            # Edge case: word1 longer and word2 is prefix — invalid
            if len(word1) > len(word2):
                return ""

    # Step 3: Topological sort using BFS (Kahn's algorithm)
    queue = deque([char for char in in_degree if in_degree[char] == 0])
    result = []

    while queue:
        char = queue.popleft()
        result.append(char)

        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If result includes all characters, return as string
    if len(result) == len(in_degree):
        return ''.join(result)
    else:
        return ""  # Cycle detected or invalid input

# Hardcoded alien dictionary input
words = ["wrt", "wrf", "er", "ett", "rftt"]

# Run and print the alien alphabet order
order = alien_order(words)
print("Alien Alphabet Order:", order)
