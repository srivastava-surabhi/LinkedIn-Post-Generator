import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]


# Main app layout
def main():
    st.title("LinkedIn Post Generator")

    # About section in the sidebar
    st.sidebar.title("About")
    st.sidebar.info("""
        This app generates LinkedIn posts based on selected topics, length, and language.
        Choose your preferences from the dropdown menus and click 'Generate' to create your post.

        **Libraries Used:**
        - **streamlit**: For building the UI
        - **few_shot**: Custom library for few-shot learning
        - **post_generator**: Custom library for generating posts

        Made with ❤️ by Surabhi.
    """)

    # Create three columns for the dropdowns
    col1, col2, col3 = st.columns(3)

    fs = FewShotPosts()
    tags = fs.get_tags()
    with col1:
        # Dropdown for Topic (Tags)
        selected_tag = st.selectbox("Topic", options=tags)

    with col2:
        # Dropdown for Length
        selected_length = st.selectbox("Length", options=length_options)

    with col3:
        # Dropdown for Language
        selected_language = st.selectbox("Language", options=language_options)

    # Center the Generate button
    st.write("")
    st.write("")
    col4, col5, col6 = st.columns([1, 2, 1])
    with col5:
        # Generate Button
        if st.button("Generate"):
            with st.spinner('Generating your post...'):
                post = generate_post(selected_length, selected_language, selected_tag)
            st.success("Your LinkedIn post is ready!")
            st.write(post)


# Run the app
if __name__ == "__main__":
    main()
