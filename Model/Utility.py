import os
from pylab import *
import time

__author__ = 'kzhu'


class Utilities(object):

    def __init__(self):
        self.path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        today = time.strftime("%Y%m%d")
        self.chart_dir = self.path+'/Results'
        self.chart_file = self.chart_dir+'/report_'+today+'.png'


    def get_keys(self,dictionary,value):
        keys = []
        for key in dictionary:
            if dictionary[key] == value:
                keys.append(key)
        return keys

    def draw_report_pie_chart(self,fracs):
        figure(1, figsize=(6,6))
        ax = axes([0.1, 0.1, 0.8,0.8])
        colors = {'Passed':'lightgreen','Failed':'orangered','Error':'orange'}
        explode = {'Passed':0,'Failed':0,'Error':0}
        keys = self.get_keys(fracs,0)
        labels_fracs = {k: v for k, v in fracs.items() if k not in keys}
        labels_color = {k: v for k, v in colors.items() if k not in keys}
        labels_explode = {k: v for k, v in explode.items() if k not in keys}
        final_explode = labels_explode.values()
        final_colors = labels_color.values()
        final_fracs = labels_fracs.values()
        labels = labels_fracs.keys()
        pie(final_fracs, explode=final_explode, labels=labels,
                        autopct='%1.1f%%', shadow=False, startangle=90, colors=final_colors)
        title('Testing Report Summary')
        if os.path.isdir(self.chart_dir):
            savefig(self.chart_file)
        else:
            os.system("mkdir -p "+self.chart_dir)
            savefig(self.chart_file)
        return self.chart_file


if __name__ == "__main__":
    frasc = {'Passed':2,'Failed':2,'Error':1}
    instance = Utilities()
    instance.draw_report_pie_chart(frasc)
