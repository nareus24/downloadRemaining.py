import tkinter as tk

def calculate_download_time():
    download_size = float(download_size_entry.get()) * 1024  # convert GB to MB
    download_speed = float(download_speed_entry.get())  # convert MB/s to GB/s
    download_time = download_size / download_speed / 60  # convert to minutes
    output_label.config(text=f"{download_time:.2f} minutes")

# Create the main window
root = tk.Tk()
root.title("Download Time Calculator")
root.geometry("270x75")

# Create the input widgets
download_size_label = tk.Label(root, text="Download Size (GB): ")
download_size_label.grid(row=0, column=0, sticky="nsew")
download_size_entry = tk.Entry(root)
download_size_entry.grid(row=0, column=1, sticky="nsew")

download_speed_label = tk.Label(root, text="Download Speed (MB/s): ")
download_speed_label.grid(row=1, column=0, sticky="nsew")
download_speed_entry = tk.Entry(root)
download_speed_entry.grid(row=1, column=1, sticky="nsew")

calculate_button = tk.Button(root, text="Calculate", command=calculate_download_time)
calculate_button.grid(row=2, column=0, sticky="nsew")

# Create the output label
output_label = tk.Label(root, text="")
output_label.grid(row=2, column=1, sticky="nsew")

# Start the GUI event loop
root.mainloop()
