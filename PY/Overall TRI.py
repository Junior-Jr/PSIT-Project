import pygal as pg
import csv
from pygal.style import DarkStyle
TRI2014 = 0
TRI2013 = 0
TRI2012 = 0
TRI2011 = 0
TRI2010 = 0
def tri_rate(obj):
    reader = csv.DictReader(obj, delimiter = ',')
    for line in reader:
        for i in line:
            if i == "TRI_Air_Emissions_14_in_lbs":
                global TRI2014
                TRI2014 += (float(line[i]))
            if i == "TRI_Air_Emissions_13_in_lbs":
                global TRI2013
                TRI2013 +=(float(line[i]))
            if i == "TRI_Air_Emissions_12_in_lbs":
                global TRI2012
                TRI2012 +=(float(line[i]))
            if i == "TRI_Air_Emissions_11_in_lbs":
                global TRI2011
                TRI2011 +=(float(line[i]))
            if i == "TRI_Air_Emissions_10_in_lbs":
                global TRI2010
                TRI2010 +=(float(line[i]))
"""    for i in range(55):
        print(STATE[i], GHG2010[i], GHG2011[i], GHG2012[i], GHG2013[i], GHG2014[i])"""

def main():
    with open("../Data/Data.csv") as obj:
        tri_rate(obj)
main()

def render():
    """ Render graph """
    line_chart = pg.Line(x_label_rotation=30, style=DarkStyle)
    line_chart.title = ('Overall Toxics Release Inventory in USA(in lbs)')
    line_chart.x_labels = map(str, range(2010, 2014))
    line_chart.add('Summary', [TRI2010, TRI2011, TRI2012, TRI2013, TRI2014])

    """add line n render"""
    #for i in range(55):
    #    line_chart = pg.Line(x_label_rotation=30, style=DarkStyle)
    #    line_chart.title = 'Green House Gas Emissions(in metric tons)'
    #    line_chart.x_labels = map(str, range(2010, 2014))
    #    line_chart.add(STATE[i], [GHG2010[i], GHG2011[i], GHG2012[i], GHG2013[i], GHG2014[i]])
    

    """render"""
    line_chart.render_to_file('../TRI/Overall country.svg')
    #line_chart.render_in_browser()

render()
