
import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Page title and layout options
ui.page_opts(
    title="My Interactive Random Histogram App",
    fillable=True
)

# Sidebar with slider input
with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 20)

# Reactive plot that updates with slider input
@render.plot(alt="A histogram showing random data distribution")
def histogram():
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(437)
    plt.hist(x, input.selected_number_of_bins(), density=True)
