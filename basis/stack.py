class Stack:
    def __init__(self):
        self.frames = []

    def push(self, frame):
        self.frames.append(frame)

    def pop(self):
        return self.frames.pop()

    def __getitem__(self, variable):
        for frame in self.frames[::-1]:
            if variable in frame:
                return frame[variable]

class Frame:
    def __init__(self):
        self._variable_map = {}

    def __setitem__(self, variable_name, val):
        self._variable_map[variable_name] = val

    def __getitem__(self, variable_name):
        return self._variable_map[variable_name]

    def __contains__(self, variable_name):
        return variable_name in self._variable_map
