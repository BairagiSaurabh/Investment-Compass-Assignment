# Wikipedia Search App

This Streamlit app allows users to search for articles on Wikipedia based on a keyword. The app retrieves search results from Wikipedia and displays them along with a brief summary and metadata for each article. Users can select an article from the search results and open it in a web browser to read more.

## Features:
- Input field to enter a search keyword
- Displays search results with titles, summaries, and metadata
- Interactive selection of articles to open in a web browser
- Customized appearance with a black background and white text for better readability

## Usage:
1. Enter a keyword in the input field and press Enter or click on the "Search" button.
2. The app will retrieve search results from Wikipedia and display them.
3. Scroll through the search results to find the desired article.
4. Click on the "Open Article" button to open the selected article in a web browser.

## Dependencies:
- Streamlit
- Requests-HTML
- Webbrowser

## How to Run:
1. Install the required dependencies using pip:
    ```
    pip install streamlit requests-html
    ```
2. Run the Streamlit app with the following command:
    ```
    streamlit run wikipedia_search_app.py
    ```
3. The app will open in your default web browser, allowing you to interact with it.

