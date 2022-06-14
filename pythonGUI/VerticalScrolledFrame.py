from tkinter import *

class VerticalScrolledFrame(Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling

    """

    def __init__(self, parent, bg, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)

        # create a canvas object and a vertical scrollbar for scrolling it

        canvas = Canvas(self, bd=0, highlightthickness=0, bg=bg)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        self.canvasheight = 2000

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas, height=self.canvasheight, bg=bg)
        interior_id = canvas.create_window(0, 0, window=interior, anchor=NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())

        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())

        canvas.bind('<Configure>', _configure_canvas)

        self.offset_y = 0

        def on_press(evt):
            self.offset_y = evt.y_root

        def on_touch_scroll(evt):
            if evt.y_root - self.offset_y < 0:
                evt.delta = -1
            else:
                evt.delta = 1
            # canvas.yview_scroll(-1*(evt.delta), 'units') # For MacOS
            canvas.yview_scroll(int(-1 * (evt.delta / 120)), 'units')  # For windows

        self.bind("<Enter>", lambda _: self.bind_all('<Button-1>', on_press), '+')
        self.bind("<Leave>", lambda _: self.unbind_all('<Button-1>'), '+')
        self.bind("<Enter>", lambda _: self.bind_all('<B1-Motion>', on_touch_scroll), '+')
        self.bind("<Leave>", lambda _: self.unbind_all('<B1-Motion>'), '+')
        self.bind("<Leave>", lambda _: self.unbind_all('<B1-Motion>'), '+')
