from math import gcd

input_data = open('input.txt', 'r')
data = input_data.read()
data = data.split()

a = int(data[0])
b = int(data[1])


ans = str((a * b) // gcd(a, b))# gcd  - наибольший общий делитель

output_data = open('output.txt', 'w')
output_data.write(ans)

input_data.close()
output_data.close()