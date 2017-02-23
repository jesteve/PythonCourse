import numpy as np
import vxi11 # python-vxi11 : communicates with VXI and LXI compatible devices

class LecroyScope(vxi11.Instrument):
    def fetchwaveform(self, channel):
        trc = self.ask_raw('C{0}:WF?'.format(channel))
        return self.decode(trc)

    def decode(self, trc):
        """Quick and dirty Lecroy TRC format decoder."""
        # See Lecroy manual p. 282
        start = trc.find('WAVEDESC')
        trc = trc[start:]
        nb_of_points   = np.fromstring(trc[60 :64 ], dtype=np.uint32)
        voltage_gain   = np.fromstring(trc[156:160], dtype=np.float32)
        voltage_offset = np.fromstring(trc[160:164], dtype=np.float32)
        horiz_interval = np.fromstring(trc[176:180], dtype=np.float32)
        horiz_offset   = np.fromstring(trc[180:188], dtype=np.float64)
        voltage = np.fromstring(trc[346:], dtype=np.int8, count=nb_of_points).astype(np.float)
        voltage *= voltage_gain
        voltage += voltage_offset
        time = np.arange(nb_of_points, dtype=np.float)
        time *= horiz_interval
        time += horiz_offset
        return time, voltage
