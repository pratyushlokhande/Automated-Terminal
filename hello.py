from math import radians
t1=radians(int(input('Enter Latitude of 1st point : ')))
g1=radians(int(input('Enter Longitude of 1st point : ')))
t2=radians(int(input('Enter Latitude of 2nd point : ')))
g2=radians(int(input('Enter Longitude of 2nd point : ')))
d=6371.01*arccos(sin(t1)*sin(t2)*+cos(t1)*cos(t2)*cos(g1-g2))
print('Distanc between the two points : %.2f'%d)