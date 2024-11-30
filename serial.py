"""Python serial number generator."""

class SerialGenerator:
    """
    Starts new generator sequence starting with a number
    """
    #set defined class variables here
    def __init__(self, start=0):
        self.start = start
        self.next = start

    def generate(self):
        """
        Returns initial value then starts sequencing by 1

        """
        self.next = self.next + 1
        return self.next - 1

    def reset(self):
        """
        Resets starting sequence back to original number value
        """
        self.next = self.start
        return self.next






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

