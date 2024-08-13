import tkinter as tk
import font_manager as fonts
from check_videos import CheckVideos
from create_video_list import CreateVideoList
from update_videos import UpdateVideos

class VideoPlayerApp:
    def __init__(self, root):
        self.root = root  # Assign root to an instance variable
        self.root.geometry("520x150")
        self.root.title("Video Player")

        # Configure custom fonts
        fonts.configure()

        # Set modern colors
        self.bg_color = "#2E2E2E"
        self.fg_color = "#FFFFFF"
        self.button_color = "#007BFF"
        self.button_hover_color = "#0056b3"

        self.root.configure(bg=self.bg_color)

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Header label
        self.header_lbl = tk.Label(self.root, text="Select an option by clicking one of the buttons below",
                                   bg=self.bg_color, fg=self.fg_color, font=("Helvetica", 12, "bold"))
        self.header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Buttons
        self.check_videos_btn = tk.Button(self.root, text="Check Videos", command=self.check_videos_clicked,
                                          bg=self.button_color, fg=self.fg_color, font=("Helvetica", 10, "bold"),
                                          relief="flat", height=2, width=15)
        self.check_videos_btn.grid(row=1, column=0, padx=10, pady=10)
        self.check_videos_btn.bind("<Enter>", lambda e: self.on_button_hover(self.check_videos_btn))
        self.check_videos_btn.bind("<Leave>", lambda e: self.on_button_leave(self.check_videos_btn))

        self.create_video_list_btn = tk.Button(self.root, text="Create Video List", command=self.create_video_list_clicked,
                                               bg=self.button_color, fg=self.fg_color, font=("Helvetica", 10, "bold"),
                                               relief="flat", height=2, width=15)
        self.create_video_list_btn.grid(row=1, column=1, padx=10, pady=10)
        self.create_video_list_btn.bind("<Enter>", lambda e: self.on_button_hover(self.create_video_list_btn))
        self.create_video_list_btn.bind("<Leave>", lambda e: self.on_button_leave(self.create_video_list_btn))

        self.update_videos_btn = tk.Button(self.root, text="Update Videos", command=self.update_videos_clicked,
                                           bg=self.button_color, fg=self.fg_color, font=("Helvetica", 10, "bold"),
                                           relief="flat", height=2, width=15)
        self.update_videos_btn.grid(row=1, column=2, padx=10, pady=10)
        self.update_videos_btn.bind("<Enter>", lambda e: self.on_button_hover(self.update_videos_btn))
        self.update_videos_btn.bind("<Leave>", lambda e: self.on_button_leave(self.update_videos_btn))

        # Status label
        self.status_lbl = tk.Label(self.root, text="", bg=self.bg_color, fg=self.fg_color, font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    def check_videos_clicked(self):
        self.status_lbl.configure(text="Check Videos button was clicked!")
        CheckVideos(tk.Toplevel(self.root))  # Open in a new Toplevel window

    def create_video_list_clicked(self):
        self.status_lbl.configure(text="Create Video List button was clicked!")
        # Open CreateVideoList in a new Toplevel window
        new_window = tk.Toplevel(self.root)
        CreateVideoList(new_window)
        new_window.mainloop()

    def update_videos_clicked(self):
        self.status_lbl.configure(text="Update Videos button was clicked!")
        UpdateVideos(tk.Toplevel(self.root))  # Open in a new Toplevel window

    def on_button_hover(self, button):
        button.configure(bg=self.button_hover_color)

    def on_button_leave(self, button):
        button.configure(bg=self.button_color)

if __name__ == "__main__":
    window = tk.Tk()
    app = VideoPlayerApp(window)
    window.mainloop()
