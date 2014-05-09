from chart import ChartBase

class CurrentChart(ChartBase):
    def __init__(self, container):
        ChartBase.__init__(self, container, 'Current Magitude', 'Magnitude (m/s)', '')

    def fill(self, data, update=False):
        positive = [[i , -max(v[1],0)] for i, v in enumerate(data)]
        negative = data.tolist()

        if update:
            self.plot.set_layer('negative', 
                values=negative)

            self.plot.set_layer('positive', 
                values=positive)

            self.plot.set_layer('value', 
                line=True,
                values=data)
        else:
            self.plot.add_layer('negative', 
                fill='#FE5000',
                values=negative)

            self.plot.add_layer('positive', 
                fill='#C4D600',
                values=positive)

            self.plot.add_layer('value', 
                line=True,
                color='#000',
                thickness=2,
                values=data)
        