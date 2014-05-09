from chart import ChartBase

class WavesChart(ChartBase):
    def __init__(self, container):
        ChartBase.__init__(self, container, 'Wave Height', 'Height (m)', 'Distance (m)')


    def fill(self, data, update=False):
        data = data.tolist()

        if update:
            self.plot.set_layer('water', 
                values=data)
            self.plot.set_layer('value',
                line=True,
                values=data)
        else:
            self.plot.add_layer('water', 
                fill='#00A9CE',
                values=data)
            self.plot.add_layer('value',
                line=True,
                thickness=2,
                color='#000',
                values=data)

        self.plot._scale = [(self.plot._scale[0][0], self.plot._scale[0][1]), (max(1.,self.plot._scale[1][0]), self.plot._scale[1][1])]
