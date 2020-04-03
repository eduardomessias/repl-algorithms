def binary_gap(n):
    f = format (n, 'b')

    # Binary gap
    g = 0
    b = 0

    for i in range (0, len(f) - 1):
        if f[i] == '0':
            g = g + 1
        else:
            if g > b:
                b = g

            g = 0
        
        i = i + 1

    return b