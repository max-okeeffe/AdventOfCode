from collections import deque
from math import lcm

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

"""
For rx to be sent a low pulse, we require zp to send a low pulse.
Since zp is a conjunction module, we need all its inputs to be remembered as high.
Its inputs are sb, nd, ds, and hf. We find the minimum i such that after i button presses, each of them is high.
If you choose a large enough output you get
'ds 3733
sb 3797
hf 3877
nd 3917'.
Trying the lcm gets the right answer.
"""

Q, minvals = deque(), {}
for i in range(100000):

    for val in outputs['broadcaster']:
        Q.append(('broadcaster', val, low))

    while Q:
        oldname, newname, pulse = Q.popleft()
        if newname not in modules:
            continue
        elif oldname in ('sb', 'nd', 'ds', 'hf') and pulse:
            if oldname not in minvals:
                minvals[oldname] = i+1
        else:
            newpulse = modules[newname].receive(modules[oldname], pulse)
            if newpulse is not None:
                for nei in outputs[newname]:
                    Q.append((newname, nei, newpulse))

    if len(minvals) == 4:
        break

print(lcm(*minvals.values()))
