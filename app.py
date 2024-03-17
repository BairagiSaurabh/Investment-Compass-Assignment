import streamlit as st
import requests_html
import webbrowser

def main():
    # Set page title
    st.title("Custom Search Engine")

    # Language for Wikipedia
    language = 'en'

    # Prompt the user to input a search term
    search_term = st.text_input("Please enter your Search Query:")

    if search_term:
        # Establish a session for making HTTP requests
        session = requests_html.HTMLSession()

        # Construct the Wikipedia search URL
        search_url = f'https://{language}.wikipedia.org/w/index.php?search={search_term}&fulltext=1&ns0=1'

        # Send a GET request to Wikipedia search URL
        response = session.get(search_url)

        # Extract search results
        search_results = response.html.find('.mw-search-result')

        # Store URLs of search results
        urls = []

        # Display search results
        for index, result in enumerate(search_results):
            title = result.find('.mw-search-result-heading', first=True).text
            summary = result.find('.searchresult', first=True).text
            metadata = result.find('.mw-search-result-data', first=True).text
            urls.append(result.find('.mw-search-result-heading', first=True).absolute_links.pop())
            st.write(f'**{index}**. [{title}]({urls[-1]})')
            st.write(f'*{summary}*')
            st.write(f'_{metadata}_')

        # Prompt the user to select an article to open
        selected_index = st.number_input("Please select the number of the article you want to open:", 0, len(search_results)-1)

        if st.button("Open Article"):
            # Open the selected article in a web browser
            webbrowser.open(urls[selected_index])

if __name__ == "__main__":
    main()
