color = {
    'black' : 0,
    'brown' : 1,
    'red' : 2,
    'orange' : 3,
    'yellow' : 4,
    'green' : 5,
    'blue' : 6,
    'violet' : 7,
    'grey' : 8,
    'white' : 9
}
N = 3
arr= []
for i in range(N):
    arr.append(color[input()])
print((10 * arr[0]  + arr[1]) * (10**arr[2]))
