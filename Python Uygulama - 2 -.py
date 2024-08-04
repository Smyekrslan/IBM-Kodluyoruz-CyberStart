
points = [(1, 2), (4, 6), (5, 8), (3, 7)]

#Öklid Formülü
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
    return distance

# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)


min_distance = min(distances)

print("Tüm nokta çiftleri arasındaki mesafeler:", distances)
print("Minimum mesafe:", min_distance)
