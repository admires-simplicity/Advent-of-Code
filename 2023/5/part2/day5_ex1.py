seed_str = "79 14 55 13"

seed_to_soil_str = """50 98 2
52 50 48"""

soil_to_fertilizer_str = """0 15 37
37 52 2
39 0 15"""

fertilizer_to_water_str = """49 53 8
0 11 42
42 0 7
57 7 4"""

water_to_light_str = """88 18 7
18 25 70"""

light_to_temperature_str = """45 77 23
81 45 19
68 64 13"""

temperature_to_humidity_str = """0 69 1
1 0 69"""

humidity_to_location_str = """60 56 37
56 93 4"""

#seed_to_soil = [(0, 0), (50, 52), (98, 50), (100, 100)]
#print(seed_to_soil)

def swap_in_list(lst, i, j):
    li, lj = lst[i], lst[j]
    lst[i], lst[j] = lj, li

def ints_str_to_tuple(ints):
    ints = ints.split(' ')
    ints = list(map(int, ints))
    #swap_in_list(ints, 0, 1)
    return tuple(ints)

def spec_to_table(dst_to_src_str):
    entries = dst_to_src_str.split('\n')
    entries = list(map(ints_str_to_tuple, entries))
    entries.sort()
    return entries

def lookup(table, i):
    def get_translation_tuple(acc):
        if acc >= len(table):
            return False
        
        S, D, R = table[acc]
        if i >= S and i <= S + R - 1:
            return table[acc]

        return get_translation_tuple(acc + 1)
    
    translation_tuple = get_translation_tuple(0)
    if translation_tuple:
        S, D, R = translation_tuple
        return i + (D - S)
    else:
        return i
    
#def lookup_test():
#    assert(lookup(seed_to_soil_table, 0) == 0)
#    assert(lookup(seed_to_soil_table, 20) == 20)
#    assert(lookup(seed_to_soil_table, 49) == 49)
#    assert(lookup(seed_to_soil_table, 50) == 52)
#    assert(lookup(seed_to_soil_table, 53) == 55)
#    assert(lookup(seed_to_soil_table, 97) == 99)
#    assert(lookup(seed_to_soil_table, 98) == 50)
#    assert(lookup(seed_to_soil_table, 99) == 51)
#    assert(lookup(seed_to_soil_table, 100) == 100)
#
#    assert(lookup(fertilizer_to_water_table, 0) == 42)
#    assert(lookup(fertilizer_to_water_table, 6) == 48)
#    assert(lookup(fertilizer_to_water_table, 7) == 57)
#    assert(lookup(fertilizer_to_water_table, 10) == 60)
#    assert(lookup(fertilizer_to_water_table, 11) == 0)
#    assert(lookup(fertilizer_to_water_table, 52) == 41)
#    assert(lookup(fertilizer_to_water_table, 53) == 49)
#    assert(lookup(fertilizer_to_water_table, 60) == 56)
#    assert(lookup(fertilizer_to_water_table, 61) == 61)
#
#
#
#seed_to_soil_table = spec_to_table(seed_to_soil_str)
#soil_to_fertilizer_table = spec_to_table(soil_to_fertilizer_str)
#fertilizer_to_water_table =  spec_to_table(fertilizer_to_water_str)
#water_to_light_table = spec_to_table(water_to_light_str)
#light_to_temperature_table = spec_to_table(light_to_temperature_str)
#temperature_to_humidity_table = spec_to_table(temperature_to_humidity_str)
#humidity_to_location_table = spec_to_table(humidity_to_location_str)
#
#print(seed_to_soil_table)
#print(fertilizer_to_water_table)
#
#lookup_test()
#
#def seed_to_location(seed):
#    return lookup(humidity_to_location_table,
#                lookup(temperature_to_humidity_table,
#                    lookup(light_to_temperature_table,
#                        lookup(water_to_light_table,
#                            lookup(fertilizer_to_water_table,
#                                 lookup(soil_to_fertilizer_table,
#                                    lookup(seed_to_soil_table,
#                                        seed)))))))




#ALL OF THE NAMES BELOW ARE BACKWARDS BECAUSE I JUST COPY-PASTED

seed_to_soil_table = spec_to_table(seed_to_soil_str)
soil_to_fertilizer_table = spec_to_table(soil_to_fertilizer_str)
fertilizer_to_water_table =  spec_to_table(fertilizer_to_water_str)
water_to_light_table = spec_to_table(water_to_light_str)
light_to_temperature_table = spec_to_table(light_to_temperature_str)
temperature_to_humidity_table = spec_to_table(temperature_to_humidity_str)
humidity_to_location_table = spec_to_table(humidity_to_location_str)

def location_to_seed(location):
    return lookup(seed_to_soil_table,
                lookup(soil_to_fertilizer_table,
                    lookup(fertilizer_to_water_table,
                        lookup(water_to_light_table,
                            lookup(light_to_temperature_table,
                                lookup(temperature_to_humidity_table,
                                    lookup(humidity_to_location_table,
                                        location)))))))



seed_ranges = list(map(int, seed_str.split(' ')))

def seed_in_seeds(seed):
    for i in range(0, len(seed_ranges), 2):
        if seed in range(seed_ranges[i], seed_ranges[i]+seed_ranges[i+1]):
            return True
    return False

## SANITY CHECK:
#print(location_to_seed(46))
#
#location_to_seed = list(map(location_to_seed, list(range(0, 100))))
#location_in_seed_list = list(map(seed_in_seeds, location_to_seed))
#
#good_locations = len(list(filter(None, location_in_seed_list)))
#print(f"good_locations = {good_locations}")
#
#print(location_to_seed)
#print(location_in_seed_list)
#
#for i in range(0, 100):
#    print(f"location {i} has seed {location_to_seed[i]} and whether or not it is in the seed list is {location_in_seed_list[i]}")


i = 0
while not seed_in_seeds(location_to_seed(i)):
    i += 1
print(f"lowest location with a seed in the seed range list is {i}")


    
            



