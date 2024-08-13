import tkinter as tk
import tkinter.scrolledtext as tkst

import video_library as lib
import font_manager as fonts

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", content)

class UpdateVideos:
    def __init__(self, window):
        self.window = window
        self.window.geometry("750x350")
        self.window.title("Update Videos")

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
                                    relief="flat", height=2, width=18)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)
        list_videos_btn.bind("<Enter>", lambda e: self.on_button_hover(list_videos_btn))
        list_videos_btn.bind("<Leave>", lambda e: self.on_button_leave(list_videos_btn))

        # Label and input for video number
        enter_lbl = tk.Label(self.window, text="Enter Video Number", bg=self.bg_color, fg=self.fg_color,
                             font=("Helvetica", 11))
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(self.window, width=5, font=("Helvetica", 11), bg="#2A2A2A", fg=self.fg_color, borderwidth=0)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # Button to update video details
        update_video_btn = tk.Button(self.window, text="Update Video", command=self.update_video_clicked,
                                     bg=self.button_color, fg=self.fg_color, font=("Helvetica", 11, "bold"),
                                     relief="flat", height=2, width=18)
        update_video_btn.grid(row=0, column=3, padx=10, pady=10)
        update_video_btn.bind("<Enter>", lambda e: self.on_button_hover(update_video_btn))
        update_video_btn.bind("<Leave>", lambda e: self.on_button_leave(update_video_btn))

        # Label and input for new rating
        rating_lbl = tk.Label(self.window, text="Enter New Rating", bg=self.bg_color, fg=self.fg_color,
                              font=("Helvetica", 11))
        rating_lbl.grid(row=1, column=1, padx=10, pady=10)

        self.rating_txt = tk.Entry(self.window, width=5, font=("Helvetica", 11), bg="#2A2A2A", fg=self.fg_color, borderwidth=0)
        self.rating_txt.grid(row=1, column=2, padx=10, pady=10)

        # ScrolledText widget for displaying messages
        self.list_txt = tkst.ScrolledText(self.window, width=50, height=12, wrap="none",
                                         bg="#2A2A2A", fg=self.fg_color, font=("Helvetica", 11), borderwidth=0)
        self.list_txt.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # Status label
        self.status_lbl = tk.Label(self.window, text="", bg=self.bg_color, fg=self.fg_color, font=("Helvetica", 11))
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # Initial call to populate video list
        self.list_videos_clicked()

    def update_video_clicked(self):
        key = self.input_txt.get()
        new_rating = self.rating_txt.get()
        if key and new_rating:
            if key in lib.library:
                lib.set_rating(key, int(new_rating))
                name = lib.get_name(key)
                play_count = lib.get_play_count(key)
                update_message = f"Video {name} updated to rating {new_rating} with {play_count} plays."
                set_text(self.list_txt, update_message)
            else:
                set_text(self.list_txt, f"Video {key} not found")
        else:
            set_text(self.list_txt, "Invalid input. Please enter a valid video number and rating.")
        self.status_lbl.configure(text="Update Video button was clicked!")

    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")

    def on_button_hover(self, button):
        button.configure(bg=self.button_hover_color)

    def on_button_leave(self, button):
        button.configure(bg=self.button_color)

if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    UpdateVideos(window)
    window.mainloop()
