import csv
import plotly.graph_objs as go
import plotly.offline as pyo
import time

def plot_live_chart(input_file):
    so = 1000 # Initialize starting value
    y = [so] # Initialize list to store values for y-axis
    fig = go.Figure() # Initialize a Figure object
    
    with open(input_file, 'r') as input_file:
        reader = csv.reader(input_file)
        header = next(reader) # Skip the header row
        
        for i in reader:
            row = i[0].split(';')
            s = row[11] # Get value from 11th column
            n = row[4] # Get value from 4th column
            k = row[9] # Get value from 9th column
            k = float(k) # Convert k to float
            
            if s != '' and n !='' : # Check if s and n are not empty
                s = float(s) # Convert s to float
                y.append(so) # Append current value of so to y
                s = s + k # Add k to s
                so = so + s # Update so with the new value
                
                fig.add_trace(go.Scatter(y=y)) # Add trace to the figure
                fig.update_layout(title='Live Chart', xaxis_title='Time', yaxis_title='Values') # Update the layout of the figure
                fig.update() # Update the figure without opening a new page
                time.sleep(1) # Wait for 1 second before updating the chart
        
input_file= 'C:/Users/delta2794900/Documents/kon2.csv'
plot_live_chart(input_file)
