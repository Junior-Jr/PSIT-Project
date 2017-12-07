import pygal as pg
import csv
from pygal.style import DarkStyle
TRI2014 = []
TRI2013 = []
TRI2012 = []
TRI2011 = []
TRI2010 = []
STATE = []
def tri_rate(obj):
    reader = csv.DictReader(obj, delimiter = ',')
    for line in reader:
        for i in line:
            if i == "State":
                STATE.append(line[i])
            if i == "TRI_Air_Emissions_14_in_lbs":
                TRI2014.append(float(line[i]))
            if i == "TRI_Air_Emissions_13_in_lbs":
                TRI2013.append(float(line[i]))
            if i == "TRI_Air_Emissions_12_in_lbs":
                TRI2012.append(float(line[i]))
            if i == "TRI_Air_Emissions_11_in_lbs":
                TRI2011.append(float(line[i]))
            if i == "TRI_Air_Emissions_10_in_lbs":
                TRI2010.append(float(line[i]))
"""    for i in range(55):
        print(STATE[i], TRI2010[i], TRI2011[i], TRI2012[i], TRI2013[i], TRI2014[i])"""

def main():
    with open("../Data/Data.csv") as obj:
        tri_rate(obj)
main()

def render():
    """ Render graph """
    #line_chart = pg.Line(x_label_rotation=30, style=DarkStyle)
    #line_chart.title = 'Toxics Release Inventory(in lbs)'
    #line_chart.x_labels = map(str, range(2010, 2014))


    """add line"""
    for i in range(55):
        line_chart = pg.Line(x_label_rotation=30, style=DarkStyle)
        line_chart.title = 'Toxics Release Inventory(in lbs)'
        line_chart.x_labels = map(str, range(2010, 2014))
        line_chart.add(STATE[i], [TRI2010[i], TRI2011[i], TRI2012[i], TRI2013[i], TRI2014[i]])
        line_chart.render_to_file(('../TRI/State '+str(STATE[i])+'.svg'))

    """render"""
    #line_chart.render_to_file('../tmp/Overall country.svg')
    #line_chart.render_in_browser()

render()