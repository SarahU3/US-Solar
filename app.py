from flask import Flask, render_template, request, redirect
import os
import requests
import pandas as pd
import numpy as np
import geopandas as gpd
from bokeh.embed import components
from bokeh.plotting import figure, output_file, show
from bokeh.palettes import Greens8 as palette
from bokeh.models import ColumnDataSource, GeoJSONDataSource, HoverTool, LinearColorMapper
import bokeh.layouts

county_df = pd.read_pickle('county_data.pkl')



# --- Set up Flask ---
app  = Flask(__name__)
app.debug = True
app.vars={} # change this - need stateless architecture

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index', methods=['GET','POST'])
def index():
    if request.method == 'POST':
	#provide requested state plots

    else:
	#request was GET, provide a plot of California
	 # --- Create graph ---
    p = figure(#plot_width=500, plot_height=400)

    script, div = components(p)
    return render_template('index.html', script=script, div=div, tickersym=app.vars['tickerinput'])

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
