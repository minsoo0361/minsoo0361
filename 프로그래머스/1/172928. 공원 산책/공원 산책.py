def solution(park, routes):
    answer = []
    H = len(park)
    W = len(park[0])
    
    s_i, s_j = -1, -1
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                s_i, s_j = i, j
                break
        if s_i != -1:
            break
    
    four_direction = {'N' : (-1, 0), 'S' : (1, 0), 'W' : (0, -1), 'E' : (0, 1)}
    
    for route in routes:
        direction, di = route.split()
        distance = int(di)    
        dx, dy = four_direction[direction]
        temp_x, temp_y = s_i, s_j
        can_move = True
    
        
        for _ in range(distance):
            nx, ny = temp_x + dx, temp_y + dy
            
            if not (0 <= nx < H and 0 <= ny < W):
                can_move = False
                break
            
            if park[nx][ny] == 'X':
                can_move =  False
                break
            
                
            temp_x, temp_y = nx, ny
            
        if can_move:
            s_i, s_j = temp_x, temp_y
    
    return [s_i, s_j]