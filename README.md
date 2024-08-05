# SongRadioGUI

## Overview

Playlist Recommender is a Python application that helps you discover similar tracks to a given song using the Last.fm API. It features a simple graphical user interface (GUI) built with `customtkinter` for ease of use. The application allows users to input a song and artist name, specify the number of similar tracks to retrieve, view recommendations, and save them to a text file. It also supports persistent storage of your Last.fm API key.

Made it to have a similar experience to a "song radio" on Qobuz importing the playlist via Soundiiz.

## Features

- **Input Fields**: Enter the song name, artist name, and number of songs to retrieve.
- **Recommendations**: Fetch and display similar tracks based on your input.
- **Save**: Save the list of recommended tracks to a text file.
- **API Key Management**: Save and load your Last.fm API key to avoid re-entering it each time you use the application.

## Installation

1. **Clone the Repository** (or download the source code):

    ```bash
    git clone https://github.com/SeidSmatti/SongRadioGUI.git
    cd SongRadioGUI
    ```

2. **Install Dependencies**:

    Ensure you have Python installed, then install the required packages using pip:

    ```bash
    pip install customtkinter requests
    ```

3. Make sure you have tkinter installed :
   
   For Mac OS
   ```sh
   brew install python-tk
   ```

   For Linux (Debian based)
   ```
   sudo apt-get install python3-tk
   ```

   For Windows

   Usually comes pre-installed with Python, if not see the [official documentation](https://tkdocs.com/tutorial/install.html)
   


## Usage

1. **Run the Application**:

    Execute the Python script to launch the GUI:

    ```bash
    python SongRadioGUI.py
    ```

2. **Configure API Key**:

    - Enter your Last.fm API key in the "API Key" field.
    - Click the "Save Key" button to store the API key for future use.

3. **Input Track and Artist**:

    - Enter the name of the track and artist in the respective fields.
    - Specify the number of similar tracks you want to retrieve.

4. **Retrieve Recommendations**:

    - Click the "Run" button to fetch similar tracks based on your input.
    - The recommendations will be displayed in the text box.

5. **Save Recommendations**:

    - Click the "Save" button to save the list of recommended tracks to a text file.
    - Choose a location and filename for the text file in the file dialog that appears.

## Files

- `SongRadioGUI.py`: The main Python script for the application.
- `api_key.json`: A JSON file used to store the Last.fm API key (automatically created and managed by the application).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

