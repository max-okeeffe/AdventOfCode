from collections import deque

filename = input() + ".txt"
connections = open(filename).read().split('\n')

low, high, off, on = 0, 1, 0, 1

class flipflop:
    def __init__(self, name):
        self.name = name
        self.state = off

    def receive(self, module, pulse):
        if pulse == low:
            if self.state == on:
                self.state = off
                return low
            self.state = on
            return high
        
class conjunction:
    def __init__(self, name):
        self.name = name
        self.inputs = {}

    def add(self, module):
        self.inputs[module.name] = low

    def receive(self, module, pulse):
        self.inputs[module.name] = pulse
        if all(self.inputs[name] == high for name in self.inputs.keys()):
            return low
        return high
    
class broadcast():
    def __init__(self, name):
        self.name = name

modules, outputs = {}, {}
for connection in connections:
    name, vals = connection.split(' -> ')
    vals = vals.split(', ')
    if name[0] == '%':
        name = name[1:]
        module = flipflop(name)
    elif name[0] == '&':
        name = name[1:]
        module = conjunction(name)
    else:
        name = 'broadcaster'
        module = broadcast(name)

    modules[name] = module
    outputs[name] = vals

for key, val in modules.items():
    for nei in outputs[key]:
        if nei not in modules.keys():
            continue
        elif isinstance(modules[nei], conjunction):
            modules[nei].add(val)

Q, pulses = deque(), {low : 0, high : 0}
for _ in range(1000):
    pulses[low] += 1

    for val in outputs['broadcaster']:
        Q.append(('broadcaster', val, low))
        pulses[low] += 1

    while Q:
        oldname, newname, pulse = Q.popleft()
        if newname not in modules:
            continue
        newpulse = modules[newname].receive(modules[oldname], pulse)
        if newpulse is not None:
            for nei in outputs[newname]:
                Q.append((newname, nei, newpulse))
                pulses[newpulse] += 1

print(pulses[low] * pulses[high])
