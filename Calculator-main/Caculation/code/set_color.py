import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class PlotApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Interactive Plot")
        self.geometry("800x600")

        # Create a figure and a subplot
        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)

        # Plotting some sample data
        self.x = np.linspace(-10, 10, 100)
        self.y = np.sin(self.x)
        self.line, = self.ax.plot(self.x, self.y)

        # Set the initial limits for the plot
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-1.5, 1.5)

        # Center the plot around (0,0)
        self.ax.spines['left'].set_position('center')
        self.ax.spines['bottom'].set_position('center')
        self.ax.spines['right'].set_color('none')
        self.ax.spines['top'].set_color('none')

        self.ax.xaxis.set_ticks_position('bottom')
        self.ax.yaxis.set_ticks_position('left')

        # Add grid for better visualization
        self.ax.grid(True)

        # Create the canvas widget and pack it
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill=tk.BOTH, expand=True)

        # Bind mouse events to the canvas
        self.canvas_widget.bind("<Button-1>", self.on_press)
        self.canvas_widget.bind("<B1-Motion>", self.on_drag)
        self.canvas_widget.bind("<ButtonRelease-1>", self.on_release)
        self.canvas_widget.bind("<MouseWheel>", self.on_scroll)

        self.is_dragging = False
        self.prev_x = None
        self.prev_y = None

    def on_press(self, event):
        self.is_dragging = True
        self.prev_x = event.x
        self.prev_y = event.y

    def on_drag(self, event):
        if self.is_dragging:
            dx = event.x - self.prev_x
            dy = event.y - self.prev_y

            widget_width = self.canvas_widget.winfo_width()
            widget_height = self.canvas_widget.winfo_height()

            xlim = self.ax.get_xlim()
            ylim = self.ax.get_ylim()

            x_range = xlim[1] - xlim[0]
            y_range = ylim[1] - ylim[0]

            self.ax.set_xlim(xlim[0] - dx * x_range / widget_width,
                             xlim[1] - dx * x_range / widget_width)
            self.ax.set_ylim(ylim[0] + dy * y_range / widget_height,
                             ylim[1] + dy * y_range / widget_height)

            self.canvas.draw_idle()

            self.prev_x = event.x
            self.prev_y = event.y

    def on_release(self, event):
        self.is_dragging = False

    def on_scroll(self, event):
        scale_factor = 1.1
        if event.delta > 0:
            self.zoom(scale_factor)
        elif event.delta < 0:
            self.zoom(1 / scale_factor)

    def zoom(self, factor):
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()

        x_center = (xlim[1] + xlim[0]) / 2
        y_center = (ylim[1] + ylim[0]) / 2

        x_range = (xlim[1] - xlim[0]) * factor
        y_range = (ylim[1] - ylim[0]) * factor

        self.ax.set_xlim(x_center - x_range / 2, x_center + x_range / 2)
        self.ax.set_ylim(y_center - y_range / 2, y_center + y_range / 2)

        self.canvas.draw_idle()

if __name__ == "__main__":
    app = PlotApp()
    app.mainloop()
