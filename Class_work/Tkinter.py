
import os
import glob
import threading
import time
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

try:
    import pygame
except ImportError:
    raise ImportError("pygame is required. Install with: pip install pygame")


try:
    from mutagen.mp3 import MP3
    MUTAGEN_AVAILABLE = True
except Exception:
    MUTAGEN_AVAILABLE = False

class MusicPlayer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Music Player")
        self.geometry("600x380")
        self.resizable(False, False)

        pygame.mixer.init()

        self.playlist = []
        self.current_index = None
        self.is_paused = False
        self.track_length = 0.0  
        self.updating_slider = False

        self.create_widgets()
        self.updater_job = None

    def create_widgets(self):
      
        left = ttk.Frame(self, padding=(10,10))
        left.pack(side="left", fill="both", expand=False)

        ttk.Label(left, text="Playlist").pack(anchor="w")
        self.listbox = tk.Listbox(left, width=35, height=18)
        self.listbox.pack(side="left", fill="y")
        self.listbox.bind('<Double-Button-1>', self.on_double_click)

        scrollbar = ttk.Scrollbar(left, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="left", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

       
        right = ttk.Frame(self, padding=(10,10))
        right.pack(side="right", fill="both", expand=True)

      
        self.current_var = tk.StringVar(value="No track selected")
        ttk.Label(right, textvariable=self.current_var, wraplength=300).pack(anchor="w", pady=(0,10))


        self.progress_var = tk.DoubleVar(value=0)
        self.progress_slider = ttk.Scale(right, from_=0, to=100, orient="horizontal",
                                         variable=self.progress_var, command=self.on_seek)
        self.progress_slider.pack(fill="x", padx=(0,10))

     
        time_frame = ttk.Frame(right)
        time_frame.pack(fill="x", pady=(2,8))
        self.time_elapsed_var = tk.StringVar(value="00:00")
        self.time_total_var = tk.StringVar(value="/ 00:00")
        ttk.Label(time_frame, textvariable=self.time_elapsed_var).pack(side="left")
        ttk.Label(time_frame, textvariable=self.time_total_var).pack(side="left")

   
        controls = ttk.Frame(right)
        controls.pack(pady=(6,10))

        btn_prev = ttk.Button(controls, text="⏮ Prev", command=self.prev_track)
        btn_prev.grid(row=0, column=0, padx=5)
        btn_play = ttk.Button(controls, text="▶ Play", command=self.play_track)
        btn_play.grid(row=0, column=1, padx=5)
        btn_pause = ttk.Button(controls, text="⏸ Pause/Resume", command=self.pause_resume)
        btn_pause.grid(row=0, column=2, padx=5)
        btn_stop = ttk.Button(controls, text="⏹ Stop", command=self.stop_track)
        btn_stop.grid(row=0, column=3, padx=5)
        btn_next = ttk.Button(controls, text="⏭ Next", command=self.next_track)
        btn_next.grid(row=0, column=4, padx=5)

       
        vol_frame = ttk.Frame(right)
        vol_frame.pack(fill="x", pady=(6,10))
        ttk.Label(vol_frame, text="Volume").pack(anchor="w")
        self.volume_var = tk.DoubleVar(value=0.8)
        volume_slider = ttk.Scale(vol_frame, from_=0.0, to=1.0, orient="horizontal",
                                  variable=self.volume_var, command=self.on_volume_change)
        volume_slider.pack(fill="x")
        pygame.mixer.music.set_volume(self.volume_var.get())

      
        bottom = ttk.Frame(right)
        bottom.pack(side="bottom", fill="x", pady=(10,0))
        ttk.Button(bottom, text="Load Folder", command=self.load_folder).pack(side="left", padx=5)
        ttk.Button(bottom, text="Remove Selected", command=self.remove_selected).pack(side="left", padx=5)
        ttk.Button(bottom, text="Clear Playlist", command=self.clear_playlist).pack(side="left", padx=5)

    def load_folder(self):
        folder = filedialog.askdirectory()
        if not folder:
            return
    
        patterns = ("*.mp3", "*.wav", "*.ogg", "*.flac")
        added = 0
        for pat in patterns:
            for filepath in glob.glob(os.path.join(folder, pat)):
                if filepath not in self.playlist:
                    self.playlist.append(filepath)
                    self.listbox.insert("end", os.path.basename(filepath))
                    added += 1
        if added == 0:
            messagebox.showinfo("No files", "No supported audio files found in that folder.")
        else:
            messagebox.showinfo("Loaded", f"Added {added} files to playlist.")

    def play_track(self, index=None):
        if index is None:
       
            selection = self.listbox.curselection()
            if selection:
                index = selection[0]
            elif self.current_index is not None:
                index = self.current_index
            else:
                if self.playlist:
                    index = 0
                else:
                    messagebox.showinfo("No tracks", "Playlist is empty. Load a folder first.")
                    return

        if index < 0 or index >= len(self.playlist):
            return

        path = self.playlist[index]
        try:
            pygame.mixer.music.load(path)
        except Exception as e:
            messagebox.showerror("Playback error", f"Could not load file:\n{e}")
            return

        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(self.volume_var.get())
        self.current_index = index
        self.listbox.selection_clear(0, "end")
        self.listbox.selection_set(index)
        self.listbox.activate(index)
        self.current_var.set(os.path.basename(path))
        self.is_paused = False

      
        self.track_length = 0.0
        if MUTAGEN_AVAILABLE and path.lower().endswith(".mp3"):
            try:
                audio = MP3(path)
                self.track_length = float(audio.info.length)
            except Exception:
                self.track_length = 0.0
        else:
       
            self.track_length = 0.0


        self.updating_slider = True
        self.progress_var.set(0)
        self.time_elapsed_var.set("00:00")
        if self.track_length > 0:
            self.time_total_var.set("/ " + self.format_time(self.track_length))
        else:
            self.time_total_var.set("/ 00:00")

        self.updating_slider = False
      
        self.schedule_updater()

    def schedule_updater(self):
        if self.updater_job:
            self.after_cancel(self.updater_job)
        self.updater_job = self.after(500, self.update_progress)

    def update_progress(self):
      
        if pygame.mixer.music.get_busy():
           
            pos_ms = pygame.mixer.music.get_pos()
            if pos_ms < 0:
             
                pos = 0.0
            else:
                pos = pos_ms / 1000.0
            if self.track_length > 0:
                percent = (pos / self.track_length) * 100
                if percent > 100:
                    percent = 100
                self.updating_slider = True
                self.progress_var.set(percent)
                self.updating_slider = False
                self.time_elapsed_var.set(self.format_time(pos))
            else:
             
                try:
                    prev = float(self.progress_var.get())
                except Exception:
                    prev = 0.0
           
                self.time_elapsed_var.set(self.format_time(pos))

        else:
          
            if not self.is_paused and self.current_index is not None:
              
                self.next_track()

        self.schedule_updater()

    def pause_resume(self):
        if pygame.mixer.music.get_busy():
            if not self.is_paused:
                pygame.mixer.music.pause()
                self.is_paused = True
            else:
                pygame.mixer.music.unpause()
                self.is_paused = False

    def stop_track(self):
        pygame.mixer.music.stop()
        self.is_paused = False
        self.progress_var.set(0)
        self.time_elapsed_var.set("00:00")

    def next_track(self):
        if not self.playlist:
            return
        if self.current_index is None:
            next_idx = 0
        else:
            next_idx = (self.current_index + 1) % len(self.playlist)

        self.play_track(next_idx)

    def prev_track(self):
        if not self.playlist:
            return
        if self.current_index is None:
            prev_idx = 0
        else:
            prev_idx = (self.current_index - 1) % len(self.playlist)
        self.play_track(prev_idx)

    def on_volume_change(self, _=None):
        v = self.volume_var.get()
        pygame.mixer.music.set_volume(float(v))

    def on_double_click(self, event):
        sel = self.listbox.curselection()
        if sel:
            self.play_track(sel[0])

    def on_seek(self, value):
        
        if self.updating_slider:
            return
        if self.current_index is None:
            return
        try:
            percent = float(value)
        except Exception:
            return
        if self.track_length and self.track_length > 0:
            seek_time = (percent / 100.0) * self.track_length
            try:
               
                path = self.playlist[self.current_index]
                pygame.mixer.music.load(path)
                pygame.mixer.music.play(start=seek_time)
                if self.is_paused:
                    pygame.mixer.music.pause()
            
                self.time_elapsed_var.set(self.format_time(seek_time))
            except Exception as e:
             
                print("Seek not supported by this backend:", e)
        else:
           
            pass

    def remove_selected(self):
        sel = self.listbox.curselection()
        if not sel:
            return
        idx = sel[0]
        path = self.playlist.pop(idx)
        self.listbox.delete(idx)
        if self.current_index == idx:
            self.stop_track()
            self.current_index = None
            self.current_var.set("No track selected")
        elif self.current_index is not None and idx < self.current_index:
            self.current_index -= 1

    def clear_playlist(self):
        self.stop_track()
        self.playlist.clear()
        self.listbox.delete(0, "end")
        self.current_index = None
        self.current_var.set("No track selected")

    @staticmethod
    def format_time(seconds):
        try:
            seconds = int(seconds)
        except Exception:
            seconds = 0
        m = seconds // 60
        s = seconds % 60
        return f"{m:02d}:{s:02d}"

    def on_close(self):
        try:
            if self.updater_job:
                self.after_cancel(self.updater_job)
        except Exception:
            pass
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        self.destroy()

if __name__ == "__main__":
    app = MusicPlayer()
    app.protocol("WM_DELETE_WINDOW", app.on_close)
    app.mainloop()
