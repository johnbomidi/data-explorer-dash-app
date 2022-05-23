## Welcome to Data Explorer App Blog

Here are some great resources that were used to build this app!

### Dash Documentation

The dash documentation is quite thorough.  RTFM!

#### Upload
[Dash upload component](https://dash.plotly.com/dash-core-components/upload) <br />
The first example to drop in data file and displaying it as a table was the starting point for this app.

#### Layout
[Dash Layout](https://dash.plotly.com/layout) <br />
The layout of the app is a good reference

![image](https://user-images.githubusercontent.com/37553132/161395361-b8efae32-28c3-466e-9865-6daafdc13fea.png)

####

![image](https://user-images.githubusercontent.com/37553132/161395555-874f8afe-61ea-4597-927e-d99b01fb5695.png)


#### Dropdown
[Dash core components: Dropdown](https://dash.plotly.com/dash-core-components/dropdown) <br />
The tutorial has a good introduction to the dropdown components for selecting the index and columns to explore as two separate dropdowns.

#### Basic and Advanced Callbacks
[Dash basic callbacks](https://dash.plotly.com/basic-callbacks) <br />
The upload and dropdown examples had some callback logic introduced already.  The tuturial helped further on chained callbacks to use output of the index to change the dropdown for available columns to plot.

[Dash advanced callbacks](https://dash.plotly.com/advanced-callbacks) <br />
Circular callback in advanced section of callbacks was used for range and slider synchronization.  Datetime were In order to keep the slider simple, no ticks were used and the length was matched to the index or dataframe length.  There are some examples online in the dash forums, if the ticks are important. 

#### And then the plotting
[Plotly line plots](https://plotly.com/python/line-charts/) <br />
A list of traces with scattergl - which is great for large data sets - was the best way to plot all the selected columns against the selected index.  The ylabel was also assigned into the layout. <br />

### Dash Extension Package
[Dash extensions](https://www.dash-extensions.com/) <br />
Dash can be imported from the enrich module, and used.  Besides input, output and state, serversideoutput can be used to make the data handling very efficient. <br />
[Dash extensions: ServersideOutputTransform, memoize=true](https://www.dash-extensions.com/transforms/serverside-output-transform) <br />
memoize=true comes in handy, to memoize the output of a callback.  For example, when the same file is read in, repeated parsing is avoided.  The only missing thing would be to periodically clean that cache when fielsystemstore is used - there may be some ugly implementations out there, or it may have to be deleted periodically.

### Cookiecutter for the dash app
[Cookiecutter template](https://github.com/chrisvoncsefalvay/cookiecutter-dash)

### Useful blog
[Statworx: step by step tutorial](https://www.statworx.com/en/content-hub/blog/how-to-build-a-dashboard-in-python-plotly-dash-step-by-step-tutorial/)<br />
The plotting and the style are great <br />
[Code for the tutorial](https://github.com/STATWORX/blog/tree/master/DashApp)

