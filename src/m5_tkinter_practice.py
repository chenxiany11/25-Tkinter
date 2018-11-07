"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Xianying Chen.
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # done: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------
    window = tkinter.Tk()

    # ------------------------------------------------------------------
    #done: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------
    frame = ttk.Frame(window, padding=100)
    frame.grid()

    # ------------------------------------------------------------------
    # done: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------
    button = ttk.Button(frame, text='print')
    button.grid()

    # ------------------------------------------------------------------
    # done: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------
    button['command'] = lambda: print_things()

    def print_things():
        print('Gao Qi Yue shi SB')

    button.grid()

    # ------------------------------------------------------------------
    # done: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------
    entry = ttk.Entry(frame)
    entry.grid()
    button2 = ttk.Button(frame, text='ok?')
    button2.grid()
    button2['command'] = lambda: whether_ok()

    def whether_ok():
        if entry.get() == 'ok':
            print('Hello')
        else:
            print('Goodbye')

    # ------------------------------------------------------------------
    # done: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################
    button3 = ttk.Button(frame, text='print n times')
    button3.grid()
    entry2 = ttk.Entry(frame)
    entry2.grid()
    button3['command'] = lambda: print_n_times()

    def print_n_times():
        for k in range(int(entry2.get())):
            print(entry.get())

    # ------------------------------------------------------------------
    # done: 8. As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------
    window.mainloop()

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
