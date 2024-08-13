import tkinter as tk
import tkinter.scrolledtext as tkst

import video_library as lib
import font_manager as fonts

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", content)

class CheckVideos:
    def __init__(self, window):
        self.window = window
        self.window.geometry("750x350")
        self.window.title("Check Videos")

        # Set modern colors
        self.bg_color = "#1E1E1E"         # Darker background
        self.fg_color = "#E0E0E0"         # Lighter text color
        self.button_color = "#4A90E2"     # Soft blue for buttons
        self.button_hover_color = "#357ABD"  # Darker blue for hover

        # Configure window
        self.window.configure(bg=self.bg_color)
        
        # Configure fonts
        fonts.configure()

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Button to list all videos
        list_videos_btn = tk.Button(self.window, text="List All Videos", command=self.list_videos_clicked,
                                    bg=self.button_color, fg=self.fg_color, font=("Helvetica", 11, "bold"),
                                    relief="flat", height=2, width=18, borderwidth=0)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)
        list_videos_btn.bind("<Enter>", lambda e: self.on_button_hover(list_videos_btn))
        list_videos_btn.bind("<Leave>", lambda e: self.on_button_leave(list_videos_btn))

        # Label and input for video number
        enter_lbl = tk.Label(self.window, text="Enter Video Number", bg=self.bg_color, fg=self.fg_color,
                             font=("Helvetica", 11))
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(self.window, width=5, font=("Helvetica", 11), bg="#2A2A2A", fg=self.fg_color, borderwidth=0)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # Button to check video details
        check_video_btn = tk.Button(self.window, text="Check Video", command=self.check_video_clicked,
                                    bg=self.button_color, fg=self.fg_color, font=("Helvetica", 11, "bold"),
                                    relief="flat", height=2, width=18, borderwidth=0)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)
        check_video_btn.bind("<Enter>", lambda e: self.on_button_hover(check_video_btn))
        check_video_btn.bind("<Leave>", lambda e: self.on_button_leave(check_video_btn))

        # ScrolledText widget for list of videos
        self.list_txt = tkst.ScrolledText(self.window, width=50, height=12, wrap="none",
                                         bg="#2A2A2A", fg=self.fg_color, font=("Helvetica", 11), borderwidth=0)
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Text widget for video details
        self.video_txt = tk.Text(self.window, width=26, height=8, wrap="none",
                                 bg="#2A2A2A", fg=self.fg_color, font=("Helvetica", 11), borderwidth=0)
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        # Status label
        self.status_lbl = tk.Label(self.window, text="", bg=self.bg_color, fg=self.fg_color, font=("Helvetica", 11))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # Initial call to populate video list
        self.list_videos_clicked()

    def check_video_clicked(self):
        key = self.input_txt.get()
        name = lib.get_name(key)
        if name is not None:
            singer = lib.get_singer(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            season = lib.get_season(key)
            video_details = f"{name}\n{singer}\nSeason: {season}\nRating: {rating}\nPlays: {play_count}"
            set_text(self.video_txt, video_details)
        else:
            set_text(self.video_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Check Video button was clicked!")

    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")

    def on_button_hover(self, button):
        button.configure(bg=self.button_hover_color)

    def on_button_leave(self, button):
        button.configure(bg=self.button_color)

if __name__ == "__main__":
    window = tk.Tk()        # Create a Tk object
    app = CheckVideos(window)  # Open the CheckVideos GUI
    window.mainloop()       # Run the main loop, reacting to button presses, etc
