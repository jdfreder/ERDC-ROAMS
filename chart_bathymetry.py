import numpy as np

from chart import ChartBase

class BathymetryChart(ChartBase):
    def __init__(self, container):
        ChartBase.__init__(self, container, 'Bathymetry', 'Depth (m)', '')

    def fill(self, ballast_depth, data, uncert, update=False):
        data_len = len(data)
        ballast_line = [(i, ballast_depth) for i in range(data_len)]
        ymultiplier = np.array([(0., 1.) for i in range(data_len)])
        xmultiplier = np.array([(1., 0.) for i in range(data_len)])

        lower_bounds = (data - (uncert * ymultiplier * .5))
        half_uncert = uncert * (xmultiplier + ymultiplier * .5)
        data = data.tolist()
        lower_bounds = lower_bounds.tolist()
        half_uncert = half_uncert.tolist()

        if update:
            self.plot.set_layer('water', 
                values=lower_bounds)
            self.plot.set_layer('upper-uncert', 
                values=half_uncert)
            self.plot.set_layer('lower-uncert', 
                values=half_uncert)
            #664433
            self.plot.set_layer('data-line', 
                line=True,
                values=data)
            self.plot.set_layer('ballast-line', 
                line=True,
                values=ballast_line)
        else:
            self.plot.add_layer('water', 
                fill='none',
                values=lower_bounds)
            self.plot.add_layer('upper-uncert', 
                fill='#BBC2C4',
                values=half_uncert)
            self.plot.add_layer('lower-uncert', 
                fill='#BBC2C4',
                values=half_uncert)
            #664433
            self.plot.add_layer('data-line', 
                line=True,
                thickness=2,
                color='#000',
                values=data)
            self.plot.add_layer('ballast-line', 
                line=True,
                thickness=1,
                color='#0011FF',
                dashes='2,2',
                values=ballast_line)
