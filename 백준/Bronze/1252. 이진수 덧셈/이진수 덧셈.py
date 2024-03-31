a, b = map(str, input().split())
int_a = int(a, 2)
int_b = int(b, 2)
c = int_a + int_b
bin_c = bin(int(c))
print(bin_c[2:])
