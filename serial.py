"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    
    """Initialize start to be equal to zero, and next to be zero as well"""
    def __init__(self, start = 0):
        self.start = start
        self.next = start
    
    """Display message to indicate what start and nexts current values are"""
    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.next}>"
    
    """When called, add 1 to the start value"""
    def generate(self):
        self.next += 1
        return self.next
        
    """When called, it resets the next value back to start value"""
    def reset(self):
        self.next = self.start



