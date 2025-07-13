filename = input() + ".txt"
data = open(filename).read().split('\n\n')

seeds, *maps = data
seeds = tuple(map(int,seeds.split()[1:]))
conv = lambda x : [tuple(map(int, y.split())) for y in x.split('\n')[1:]]
seed_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc = tuple(map(conv,maps))

def location(seed):
    def getsoil(seed):
        for a, b, c in seed_soil:
            if b <= seed <= b + c:
                return seed + a - b
        return seed
    
    soil = getsoil(seed)
    
    def getfert(soil):
        for a, b, c in soil_fert:
            if b <= soil <= b + c:
                return soil + a - b
        return soil
    
    fert = getfert(soil)
    
    def getwater(fert):
        for a, b, c in fert_water:
            if b <= fert <= b + c:
                return fert + a - b
        return fert
    
    water = getwater(fert)
    
    def getlight(water):
        for a, b, c in water_light:
            if b <= water <= b + c:
                return water + a - b
        return water
    
    light = getlight(water)
    
    def gettemp(light):
        for a, b, c in light_temp:
            if b <= light <= b + c:
                return light + a - b
        return light
    
    temp = gettemp(light)
    
    def gethumid(temp):
        for a, b, c in temp_humid:
            if b <= temp <= b + c:
                return temp + a - b
        return temp
    
    humid = gethumid(temp)
    
    for a, b, c in humid_loc:
        if b <= humid <= b + c:
            return humid + a - b
    return humid

print(min(location(seed) for seed in seeds))
