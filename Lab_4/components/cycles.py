def cycles(array: list[int]):
    m = array.copy()
    result = []
    
    while True:
        cycle = []

        i = next((i for i, j in enumerate(m) if j), -1)
        if i == -1:
            break
        
        x = m[i]
        m[i] = None
        while x not in cycle:
            cycle.append(x)
            m[x - 1] = None
            x = array[x - 1]
        result.append(cycle)
    return result