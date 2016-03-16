#!/usr/bin/env python3
#
# mystack.py


class myStack(list):
    def __init__(self):
        super().__init__()

    def pop(self, index=None):
        if hasattr(super, 'pop'):
            super().pop(index)
        else:
            pop_index = -1
            if index:
                pop_index = index
            retval = self[pop_index]
            del self[pop_index]
            return retval

    def push(self, x):
        self.append(x)

    def isempty(self):
        if len(self) > 1:
            return False
        return True

    def peek(self):
        return self[-1]

