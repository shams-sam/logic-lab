import sys
n, m = map(int, raw_input().strip().split())
v1, v2 = map(int, raw_input().strip().split())
x, y = map(int, raw_input().strip().split())
route_map = {}
distance_map = {}
def get_edge_name(x, y):
    if x > y:
        x, y = y, x
    return str(x) + '_' + str(y)
def get_edge_distance(x,y):
    edge_name = get_edge_name(x,y)
    if edge_name not in distance_map:
        return 0
    else:
        return distance_map[edge_name][0]
def bike_allowed(x,y):
    edge_name = get_edge_name(x,y)
    if edge_name in distance_map:
        return distance_map[edge_name][1]
    else:
        return -1
for _ in xrange(m):
    r1, r2, d1, b1 = map(int, raw_input().strip().split())
    route_map[r1] = route_map.get(r1, [])
    route_map[r1].append(r2)
    route_map[r2] = route_map.get(r2, [])
    route_map[r2].append(r1)
    distance_map[get_edge_name(r1, r2)] = [d1, b1]

def get_min_bike_time(x, y, dist_acc=0, visited_nodes=[]):
    if x not in route_map or x == y:
        return sys.maxsize
    visited_nodes.append(x)
    dist_direct = sys.maxsize
    if y in route_map[x] and bike_allowed(x,y) == 0:
        dist_direct = dist_acc + get_edge_distance(x,y)
    if True:
        dist = [dist_direct]
        for elem in route_map[x]:
            if bike_allowed(x, elem) == 0 and elem not in visited_nodes:
                dist.append(get_min_bike_time(elem, y, dist_acc + get_edge_distance(x, elem), visited_nodes))
            else:
                continue
        return (min(dist) if len(dist) else sys.maxsize)

def get_min_cycle_time(x, y, dist_acc=0, visited_nodes=[]):
    if x not in route_map or x == y:
        return sys.maxsize
    visited_nodes.append(x)
    dist_direct = sys.maxsize
    if y in route_map[x]:
        dist_direct = dist_acc + get_edge_distance(x,y)
    if True:
        dist = [dist_direct]
        for elem in route_map[x] :
            if bike_allowed(x, elem) != -1 and elem not in visited_nodes:
                dist.append(get_min_cycle_time(elem, y, dist_acc + get_edge_distance(x, elem), visited_nodes))
            else:
                continue
        return (min(dist) if len(dist) else sys.maxsize)

cycle = get_min_cycle_time(x,y)
bike = get_min_bike_time(x,y)

cycle_time = cycle/float(v1)
bike_time = bike/float(v2)
print '------------------'
print bike, cycle
print bike_time, cycle_time

