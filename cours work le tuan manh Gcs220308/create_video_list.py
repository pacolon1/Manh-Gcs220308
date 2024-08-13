import tkinter as tk
import tkinter.scrolledtext as tkst
import pygame
import video_library as lib
import font_manager as fonts

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", content)

class CreateVideoList:
    def __init__(self, window):
        self.sound_player = pygame.mixer
        self.sound_player.init()
        window.geometry("750x550")
        window.title("Create Video List")

        # Set modern colors
        self.bg_color = "#1E1E1E"         # Darker background
        self.fg_color = "#E0E0E0"         # Lighter text color
        self.button_color = "#4A90E2"     # Soft blue for buttons
        self.button_hover_color = "#357ABD"  # Darker blue for hover

        # Configure window
        window.configure(bg=self.bg_color)

        # Initialize playlist and total plays
        self.playlist = []
        self.total_plays = 0

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Label and input for video number
        enter_lbl = tk.Label(window, text="Enter Video Number", bg=self.bg_color, fg=self.fg_color,
                             font=("Helvetica", 11))
        enter_lbl.grid(row=0, column=0, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=5, font=("Helvetica", 11), bg="#2A2A2A", fg=self.fg_color, borderwidth=0)
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)

        # Buttons
        add_btn = tk.Button(window, text="Add to Playlist", command=self.add_to_playlist,
                            bg=self.button_color, fg=self.fg_color, font=("Helvetica", 11, "bold"),
                            relief="flat", height=2, width=18, borderwidth=0)
        add_btn.grid(row=0, column=2, padx=10, pady=10)
        add_btn.bind("<Enter>", lambda e: self.on_button_hover(add_btn))
        add_btn.bind("<Leave>", lambda e: self.on_button_leave(add_btn))

        play_selected_btn = tk.Button(window, text="Play Selected", command=self.play_selected,
                             bg=self.button_color, fg=self.fg_color, font=("Helvetica", 11, "bold"),
                             relief="flat", height=2, width=18, borderwidth=0)
        play_selected_btn.grid(row=1, column=0, padx=10, pady=10)
        play_selected_btn.bind("<Enter>", lambda e: self.on_button_hover(play_selected_btn))
        play_selected_btn.bind("<Leave>", lambda e: self.on_button_leave(play_selected_btn))

        reset_btn = tk.Button(window, text="Reset Playlist", command=self.reset_playlist,
                              bg=self.button_color, fg=self.fg_color, font=("Helvetica", 11, "bold"),
                              relief="flat", height=2, width=18, borderwidth=0)
        reset_btn.grid(row=1, column=1, padx=10, pady=10)
        reset_btn.bind("<Enter>", lambda e: self.on_button_hover(reset_btn))
        reset_btn.bind("<Leave>", lambda e: self.on_button_leave(reset_btn))

        reset_plays_btn = tk.Button(window, text="Reset Plays", command=self.reset_plays,
                                    bg=self.button_color, fg=self.fg_color, font=("Helvetica", 11, "bold"),
                                    relief="flat", height=2, width=18, borderwidth=0)
        reset_plays_btn.grid(row=1, column=2, padx=10, pady=10)
        reset_plays_btn.bind("<Enter>", lambda e: self.on_button_hover(reset_plays_btn))
        reset_plays_btn.bind("<Leave>", lambda e: self.on_button_leave(reset_plays_btn))

        # ScrolledText widget for playlist
        self.playlist_txt = tkst.ScrolledText(window, width=50, height=12, wrap="none",
                                             bg="#2A2A2A", fg=self.fg_color, font=("Helvetica", 11), borderwidth=0)
        self.playlist_txt.grid(row=2, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Status label
        self.status_lbl = tk.Label(window, text="", bg=self.bg_color, fg=self.fg_color, font=("Helvetica", 11))
        self.status_lbl.grid(row=3, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Sound control buttons
        self.stop_button = tk.Button(window, text="Stop Song", command=self.stop_sound,
                                     bg=self.button_color, fg=self.fg_color, font=("Helvetica", 11, "bold"),
                                     relief="flat", height=2, width=18, borderwidth=0)
        self.stop_button.grid(row=4, column=0, padx=10, pady=10)
        self.stop_button.bind("<Enter>", lambda e: self.on_button_hover(self.stop_button))
        self.stop_button.bind("<Leave>", lambda e: self.on_button_leave(self.stop_button))

    def play_selected(self):
        try:
            selected_text = self.playlist_txt.get("sel.first", "sel.last").strip()
            if not selected_text:
                self.status_lbl.configure(text="No song selected.")
                return

            song_index = int(selected_text.split(".")[0]) - 1  # Extract the index from the selected text
            video_num = self.playlist[song_index]
            mp3_file = lib.get_mp3_file(video_num)  # Get the correct MP3 file path

            if mp3_file:
                self.sound_player.music.load(mp3_file)
                self.sound_player.music.play()
                self.status_lbl.configure(text=f"Playing: {mp3_file}")

                # Increment the play count
                lib.increment_play_count(video_num)

                # Update the playlist display with the new play count
                self.update_playlist_display()
            else:
                self.status_lbl.configure(text="MP3 file not found.")
        except pygame.error as e:
            self.status_lbl.configure(text=f"Error: {e}")
        except tk.TclError:
            self.status_lbl.configure(text="No song selected.")

    def stop_sound(self):
        self.sound_player.music.stop()
        self.status_lbl.configure(text="Song stopped.")

    def add_to_playlist(self):
        video_num = self.input_txt.get()
        name = lib.get_name(video_num)
        if name is not None:
            self.playlist.append(video_num)
            self.update_playlist_display()
            self.status_lbl.configure(text=f"Added {name} to the playlist.")
        else:
            self.status_lbl.configure(text=f"Video {video_num} not found.")

    def reset_playlist(self):
        self.playlist = []
        self.total_plays = 0
        set_text(self.playlist_txt, "")
        self.status_lbl.configure(text="Playlist has been reset.")

    def reset_plays(self):
        for video_num in self.playlist:
            lib.reset_play_count(video_num)
        self.update_playlist_display()
        self.status_lbl.configure(text="Play counts have been reset.")

    def update_playlist_display(self):
        playlist_str = "\n".join([f"{i+1}. {lib.get_name(video)} ({lib.get_play_count(video)} plays)" for i, video in enumerate(self.playlist)])
        set_text(self.playlist_txt, playlist_str)

    def on_button_hover(self, button):
        button.configure(bg=self.button_hover_color)

    def on_button_leave(self, button):
        button.configure(bg=self.button_color)

if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    CreateVideoList(window)
    window.mainloop()
