def solution(brown, yellow):
    for i in range(1, yellow+1):
        if (yellow % i) == 0:
            garo = yellow / i
            sero = i
        if sero > garo:
            break
        if (garo+2) * (sero+2) == brown + yellow:
            return [garo+2, sero+2]