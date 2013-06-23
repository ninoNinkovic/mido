"""
Base classes for MIDI I/O.

There are no base classes for ports yet. They will
be refactored out of the portmidi module.
"""

class Device(dict):
    """
    PortMidi device.
    """
    def __init__(self, name, input, output, **kw):
        self.name = name
        self.input = input
        self.output = output
        for (name, value) in kw.items():
            setattr(self, name, value)

    def __repr__(self):
        args = []
        for (name, value) in self.__dict__.items():
            if not name.startswith('_'):
                arg = '%s=%r' % (name, value)
                args.append(arg)

        args = ', '.join(args)

        return 'Device(%s)' % args

def make_device_query(get_all_devices):
    """
    Create a query function for devices.

    Takes a function that returns all devices, and
    returns a function that can be called to filters
    these. The returned function calls get_all_devices()
    on each invocation.
    """

    def get_devices(**query):
        """
        Somewhat experimental function to get device info
        as a list of Device objects.
        """

        # Todo: raise exception on illegal query arguments
        # Todo: explain query in docstring

        devices = []

        for dev in get_all_devices():
            for (name, value) in query.items():
                if hasattr(dev, name):
                    if getattr(dev, name) != value:
                        break
            else:
                devices.append(dev)

        return devices

    return get_devices