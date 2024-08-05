import requests
import customtkinter as ctk
from tkinter import filedialog, messagebox, scrolledtext
import threading
import json
import os

# File to store the API key
API_KEY_FILE = "api_key.json"
# Global variable to store recommendations
global_recommendations = []

def load_api_key():
    """Load API key from file."""
    if os.path.exists(API_KEY_FILE):
        with open(API_KEY_FILE, 'r') as file:
            data = json.load(file)
            return data.get('api_key', '')
    return ''

def save_api_key(api_key):
    """Save API key to file."""
    with open(API_KEY_FILE, 'w') as file:
        json.dump({'api_key': api_key}, file)

def get_similar_tracks(track_name, artist_name, api_key, limit=10):
    """Fetch similar tracks from Last.fm API."""
    params = {
        'method': 'track.getsimilar',
        'track': track_name,
        'artist': artist_name,
        'api_key': api_key,
        'format': 'json',
        'limit': limit
    }
    response = requests.get('https://ws.audioscrobbler.com/2.0/', params=params)
    data = response.json()
    return data.get('similartracks', {}).get('track', [])

def save_playlist(tracks, file_path):
    """Save the playlist to a text file."""
    with open(file_path, 'w') as file:
        for track in tracks:
            title = track.get('name')
            artist = track.get('artist', {}).get('name')
            file.write(f"{title} - {artist}\n")

def run_recommendations():
    """Run recommendations on a separate thread."""
    def task():
        global global_recommendations
        api_key = api_key_entry.get()
        track_name = track_entry.get()
        artist_name = artist_entry.get()
        num_songs = int(num_songs_entry.get())

        if not api_key or not track_name or not artist_name or num_songs <= 0:
            messagebox.showerror("Input Error", "Please provide valid inputs.")
            return

        similar_tracks = get_similar_tracks(track_name, artist_name, api_key, num_songs)
        global_recommendations = similar_tracks
        display_recommendations(similar_tracks)

    threading.Thread(target=task).start()

def display_recommendations(tracks):
    """Display recommendations in the text box."""
    result_text.config(state=ctk.NORMAL)
    result_text.delete(1.0, ctk.END)
    for track in tracks:
        title = track.get('name')
        artist = track.get('artist', {}).get('name')
        result_text.insert(ctk.END, f"{title} - {artist}\n")
    result_text.config(state=ctk.DISABLED)

def save_recommendations():
    """Save recommendations to a text file."""
    if not global_recommendations:
        messagebox.showerror("Save Error", "No recommendations to save.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                           filetypes=[("Text files", "*.txt")])
    if file_path:
        save_playlist(global_recommendations, file_path)
        messagebox.showinfo("Success", "Playlist saved successfully.")

def save_key():
    """Save the API key."""
    api_key = api_key_entry.get()
    if api_key:
        save_api_key(api_key)
        messagebox.showinfo("Success", "API key saved.")

# Set up the GUI
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Playlist Recommender")
app.geometry("600x500")

# Create and place widgets
api_key_label = ctk.CTkLabel(app, text="API Key:")
api_key_label.pack(pady=5)
api_key_entry = ctk.CTkEntry(app, placeholder_text="Enter your Last.fm API key")
api_key_entry.pack(pady=5)
api_key_entry.insert(0, load_api_key())

save_key_button = ctk.CTkButton(app, text="Save Key", command=save_key)
save_key_button.pack(pady=5)

track_label = ctk.CTkLabel(app, text="Track Name:")
track_label.pack(pady=5)
track_entry = ctk.CTkEntry(app)
track_entry.pack(pady=5)

artist_label = ctk.CTkLabel(app, text="Artist Name:")
artist_label.pack(pady=5)
artist_entry = ctk.CTkEntry(app)
artist_entry.pack(pady=5)

num_songs_label = ctk.CTkLabel(app, text="Number of Songs:")
num_songs_label.pack(pady=5)
num_songs_entry = ctk.CTkEntry(app)
num_songs_entry.pack(pady=5)

run_button = ctk.CTkButton(app, text="Run", command=run_recommendations)
run_button.pack(pady=10)

save_button = ctk.CTkButton(app, text="Save", command=save_recommendations)
save_button.pack(pady=10)

result_frame = ctk.CTkFrame(app)
result_frame.pack(pady=10, fill=ctk.BOTH, expand=True)

result_text = scrolledtext.ScrolledText(result_frame, wrap='word', height=15, width=70, bg="#2E2E2E", fg="#FFFFFF", insertbackground='white')
result_text.pack(fill=ctk.BOTH, expand=True)
result_text.config(state=ctk.DISABLED)

app.mainloop()

