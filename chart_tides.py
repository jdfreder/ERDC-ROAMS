from chart import ChartBase
from math import pi, sin

class TideChart(ChartBase):
    def __init__(self, container):
        ChartBase.__init__(self, container, ylabel='', xlabel='', height=200, width=1300)

    def fill(self, start, period=12., tide_count=12., update=False):
        data = [(i/200.*period*tide_count, (sin(i/period*2.*pi) + 1.)/2.) for i in range(200)]
        window_data = [(start, 0.), (start, 1.)]
        if update:
            self.plot.set_layer('window',
                values=window_data)
            self.plot.set_layer('windowborder',
                values=window_data)
            self.plot.set_layer('value',
                line=True,
                values=data)
        else:
            self.plot.add_layer('window',
                fill='none',
                values=window_data)
            self.plot.add_layer('windowborder',
                line=True,
                color='#E31C79',
                thickness=4,
                values=window_data)
            self.plot.add_layer('value',
                line=True,
                thickness=1,
                color='#000',
                values=data)
     