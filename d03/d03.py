def m_dist(p2, p1=(0,0)):

    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


if __name__ == "__main__":

    #chains = [['R8','U5','L5','D3'], ['U7','R6','D4','L4']]
    #chains = [['R8','U2', 'L10'], ['R7','U3', 'R3']]

    chains = list()

    # Read the chains from the input file
    with open('input.data') as i:
        cs = i.readlines()
        for c in cs:
            x = c.split(',')
            chains.append(x)
    
    # Override with sample chains
    #chains = [['R8','U5','L5','D3'], ['U7','R6','D4','L4']]
    
    # Manhattan mapped chains
    grid_chains = list()

    # Map chains
    for chain in chains:
        pointer = (0,0)
        grid_chain = list()
        for link in chain:
            direction = link[0]
            length = int(link[1:])
            
            # Move Right
            if direction == 'R':
                y = pointer[1]
                x = pointer[0]
                for m in range(1, length + 1):
                    cursor = (x + m,y)
                    grid_chain.append(cursor)
                # Update new pointer position
                pointer = cursor

            # Move Left
            if direction == 'L':
                y = pointer[1]
                x = pointer[0]
                for m in range(1, length + 1):
                    cursor = (x - m,y)
                    grid_chain.append(cursor)
                # Update new pointer position
                pointer = cursor
            
            # Move Up
            if direction == 'U':
                y = pointer[1]
                x = pointer[0]
                for m in range(1, length + 1):
                    cursor = (x,y + m)
                    grid_chain.append(cursor)
                # Update new pointer position
                pointer = cursor
            
            # Move Down
            if direction == 'D':
                y = pointer[1]
                x = pointer[0]
                for m in range(1, length + 1):
                    cursor = (x,y - m)
                    grid_chain.append(cursor)
                # Update new pointer position
                pointer = cursor

        grid_chains.append(grid_chain)

    c1 = grid_chains[0]
    c2 = grid_chains[1]

    print("Length of chain 1", len(c1))
    print("Length of chain 2", len(c2))

    #print("Chain 1 is", c1)
    #print("Chain 2 is", c2)

    intersections = set(c1).intersection(c2)

    closest_intersection = min([m_dist(i) for i in intersections])

    run_to_intersections = list()
    for intersection in intersections:
        w1_run = c1.index(intersection) + 1
        w2_run = c2.index(intersection) + 1
        run_to_intersections.append(w1_run + w2_run)
        print("Run to intersection", i, "is", w1_run + w2_run)

    #print(grid_chains)
    print("Intersection points between first 2 chains", intersections)
    print("Closest intersection is", closest_intersection)
    print("Shortest combined length to the intersection is", min(run_to_intersections))