import math

"""
Flatland is a country with a number of cities, some of which have space stations. 
Cities are numbered consecutively and each has a road of  length connecting it to the next city. 
It is not a circular route, so the first city doesn't connect with the last city. 
Determine the maximum distance from any city to its nearest space station.

"""


def flatland_space_station_distance(cities_count, space_station_list):
    space_station_list.sort()
    max_dist = space_station_list[0]
    last = cities_count - 1
    i = 0

    while i < len(space_station_list) - 1:
        max_dist = max(max_dist, math.floor((space_station_list[i + 1] - space_station_list[i]) / 2))
        i += 1
    if space_station_list[i] < last:
        max_dist = max(max_dist, last - space_station_list[i])
    return max_dist


if __name__ == '__main__':
    nm = input().split()

    cities = int(nm[0])
    space_station_count = int(nm[1])
    space_stations = list(map(int, input().rstrip().split()))

    result = flatland_space_station_distance(cities, space_stations)

    print(result)
