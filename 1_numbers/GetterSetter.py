class TraceLine(object):
    def __init__(self, fieldnames, values):
        self._fields = dict(zip(fieldnames, values))

    def __getattr__(self, name):
            return self._fields[name]

    def setattr(self, key, value):
        self.__setattr__(self, key, value)

    @_fields.setter
    def x(self, value):
        print("setter of x called")
        self._fields = value


line = TraceLine(['time', 'cpuload', 'memory_use'], ['15:09:32.001', '97%', '282M'])
print line.cpuload
line.cpuload = "101%"
print line.cpuload
line.something = "something"
print line.something

setattr(line, "setProp", "qqq")
