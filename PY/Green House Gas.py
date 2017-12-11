import pygal as pg
import csv
from pygal.style import DarkStyle
GHG2014 = []
GHG2013 = []
GHG2012 = []
GHG2011 = []
GHG2010 = []
STATE = []
def ghg_rate(obj):
    reader = csv.DictReader(obj, delimiter = ',')
    for line in reader:
        for i in line:
            if i == "State":
                STATE.append(line[i])
            if i == "GHG_Direct_Emissions_14_in_metric_tons":
                GHG2014.append(float(line[i]))
            if i == "GHG_Direct_Emissions_13_in_metric_tons":
                GHG2013.append(float(line[i]))
            if i == "GHG_Direct_Emissions_12_in_metric_tons":
                GHG2012.append(float(line[i]))
            if i == "GHG_Direct_Emissions_11_in_metric_tons":
                GHG2011.append(float(line[i]))
            if i == "GHG_Direct_Emissions_10_in_metric_tons":
                GHG2010.append(float(line[i]))
"""    for i in range(55):
        print(STATE[i], GHG2010[i], GHG2011[i], GHG2012[i], GHG2013[i], GHG2014[i])"""

def main():
    with open("../Data/Data.csv") as obj:
        ghg_rate(obj)
main()

def render():
    """ Render graph """
    #line_chart = pg.Line(x_label_rotation=30, style=DarkStyle)
    #line_chart.title = 'Toxics Release Inventory(in lbs)'
    #line_chart.x_labels = map(str, range(2010, 2014))


    """loop render file"""
    for i in range(55):
        line_chart = pg.Line(x_label_rotation=30, style=DarkStyle)
        line_chart.title = 'Green House Gas Emissions(in metric tons)'
        line_chart.x_labels = map(str, range(2010, 2014))
        line_chart.add(STATE[i], [GHG2010[i], GHG2011[i], GHG2012[i], GHG2013[i], GHG2014[i]])
        line_chart.render_to_file(('../GHG/State '+str(STATE[i])+'.svg'))

    """render"""
    #line_chart.render_to_file('../tmp/Overall country.svg')
    #line_chart.render_in_browser()

render()
