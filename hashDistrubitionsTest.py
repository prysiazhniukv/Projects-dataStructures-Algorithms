from collections import Counter
from string import printable

def distribute(items, num_containers, hash_function=hash):
    return Counter([hash_function(item) % num_containers for item in items])

def plot(histogram):
    for key in sorted(histogram):
        count = histogram[key]
        padding = (max(histogram.values()) - count) * " "
        print(f"{key:3} {'■' * count}{padding} ({count})")

plot(distribute(printable, num_containers=4))

#You can use the num_containers to pick the amount of containers (array indexie's you would like
# in order to test the pythond default has function effectivness.)