import tkinter as tk
from tkinter import messagebox
from ImageParser import YandexImage, Size

def start_search():
    query = query_entry.get()
    num_results = int(num_results_entry.get())
    size = size_var.get()

    yandex_image = YandexImage()
    results = yandex_image.search(query, sizes=size)

    if results:
        for i, result in enumerate(results[:num_results]):
            print(f"Result {i + 1}:")
            print(f"Title: {result.title}")
            print(f"Description: {result.description}")
            print(f"Domain: {result.domain}")
            print(f"URL: {result.url}")
            print(f"Size: {result.size}")
            print(f"Preview URL: {result.preview.url}\n")
    else:
        messagebox.showinfo("No Results", "No images found for this query.")

# Создание GUI
root = tk.Tk()
root.title("Yandex Image Search")

tk.Label(root, text="Query:").grid(row=0, column=0)
query_entry = tk.Entry(root, width=40)
query_entry.grid(row=0, column=1)

tk.Label(root, text="Number of Images:").grid(row=1, column=0)
num_results_entry = tk.Entry(root, width=5)
num_results_entry.insert(0, "5")
num_results_entry.grid(row=1, column=1)

tk.Label(root, text="Image Size:").grid(row=2, column=0)
size_var = tk.StringVar(value="large")
tk.OptionMenu(root, size_var, "large", "medium", "small").grid(row=2, column=1)

tk.Button(root, text="Search", command=start_search).grid(row=3, column=0, columnspan=2)

root.mainloop()
