
from stackedarea import StackedAreaWidget
from IPython.html.widgets import ContainerWidget, HTMLWidget

class ChartBase(object):

    def __init__(self, container, caption=None, ylabel='', xlabel='', height=300, width=900):
        cell_header = HTMLWidget(value=('<h3 class="chart-header">' + caption + '</h3>' if caption is not None else ''))
        yaxis = HTMLWidget(value=ylabel)
        area_chart = StackedAreaWidget(width=width, height=height, hide_xaxis=xlabel=='')
        chart_columns = ContainerWidget(children=[yaxis, area_chart])
        chart_columns.set_css('width', '100%')
        xaxis = HTMLWidget(value=xlabel)
        chart = ContainerWidget(children=[chart_columns, xaxis])
        
        container.children = container.children + tuple([cell_header, chart])
        
        chart_columns.remove_class('vbox')
        chart_columns.add_class('hbox align-center center')
        xaxis.add_class('x axis-label')
        yaxis.add_class('y axis-label pack-center')
        area_chart.add_class('area-chart')
        chart.add_class('pack-center center chart-area')
        
        self.plot = area_chart

    def fill(self, update=False):
        raise NotImplementedError()
