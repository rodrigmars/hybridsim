from config import configuration, join
import tkinter as tk


def centred(root, x: int, y: int) -> tuple:

    window_width = x
    window_height = y

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    return x_cordinate, y_cordinate


def main():

    config = configuration()

    print(f"back_stage:{config.get('back_stage')}")

    print(f"tank_a:{config.get('tank_a')}")

    print(f"tank_b:{config.get('tank_b')}")

    print(f"tank_c:{config.get('tank_c')}")

    root = tk.Tk()

    root.title("hybrid-sim")

    window_width = 250

    window_height = 519

    x_cordinate, y_cordinate = centred(root, window_width, window_height)

    root.geometry(
        f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

    root.resizable(False, False)

    canvas = tk.Canvas(root, width=window_width,
                       height=window_height, highlightthickness=0)

    canvas.pack()

    back_stage = tk.PhotoImage(file=config['back_stage'])

    canvas.create_image(0, 0, image=back_stage, anchor=tk.NW)

    start_button = tk.PhotoImage(
        file=join(config['root_images'], 'start_button.png'))
    stop_button = tk.PhotoImage(
        file=join(config['root_images'], 'stop_button.png'))

    btn_start = canvas.create_image(82, 10, image=start_button, anchor=tk.NW)

    def click_start_event(event):
        canvas.itemconfig(btn_start, image=stop_button)

    # canvas.tag_bind(btn_start, '<Configure>', resize_)
    canvas.tag_bind(btn_start, '<ButtonRelease-1>', click_start_event)

    # tk.Button(canvas, text= 'teste', image = start_button).pack(side = tk.TOP)

    root.mainloop()


if __name__ == "__main__":

    main()
