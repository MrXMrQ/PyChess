import tkinter as tk

def create_grid(window, rows, cols):
        # Labels for the top row (A-H)
    for col in range(1, cols + 1):
        label = tk.Label(master=window, text=chr(64 + col), bg='Gray')
        label.grid(row=0, column=col, sticky="nsew")
        window.grid_columnconfigure(col, weight=1)

    # Labels for the left column (1-8)
    for row in range(1, rows + 1):
        label = tk.Label(master=window, text=str(row), bg='Gray')
        label.grid(row=row, column=0, sticky="nsew")
        window.grid_rowconfigure(row, weight=1)

    # Extra configuration for the 0th row and column
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    # Create the 8x8 grid
    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            frame = tk.Frame(
                master=window,
            )
            frame.grid(row=row, column=col, sticky="nsew")
            label = tk.Label(master=frame, text=f"{row},{chr(col + 64)}", fg='Gray')
            label = create_color_scheme(row, col, label)
            label.pack(expand=True, fill='both')

def create_color_scheme(row, col, label):
    if (row % 2 == col % 2): 
        label.configure(bg='lightgray') 
    else: 
        label.configure(bg='black') 
    
    return label

def create_window(title, minW, minH, maxW, maxH, rows, cols):
    window = tk.Tk()
    window.title(title)
    window.minsize(minW,minH)
    window.maxsize(maxW, maxH)

    create_grid(window, rows, cols)

    return window