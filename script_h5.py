import time
import tables
from lecroy.scope import LecroyScope
# Open scope connection
scope = LecroyScope('localhost')
npoints = 2048
# Define the data structure
class ScopeTrace(tables.IsDescription):
    run_number = tables.Int64Col()
    date_time = tables.Float64Col()
    time = tables.Float64Col( shape=(npoints,) )
    voltage = tables.Float64Col( shape=(npoints,) )
# Open hdf5 file
h5file = tables.open_file('dataset.h5', mode = 'w')
table = h5file.create_table('/', 'dataset', ScopeTrace)
trace = table.row
# Acquire and save the data
for i in range(10):
    x,y = scope.fetchwaveform(1)
    trace['run_number'] = i
    trace['date_time'] = time.time()
    trace['time'] = x[:npoints]
    trace['voltage'] = y[:npoints]
    trace.append()
# Close the file
table.flush()
h5file.close()
scope.close()
