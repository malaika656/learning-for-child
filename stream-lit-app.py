import streamlit as st
import random

# Title and Sidebar
st.title("Advanced Kids Learning App")
st.sidebar.header("Learning Modules")
module = st.sidebar.selectbox("Choose a module", ["Vocabulary Builder", "Story Time", "Educational Videos"])

# Vocabulary Builder with Quiz Mode
if module == "Vocabulary Builder":
    st.header("Vocabulary Builder")
    vocab_words = {
        "Cat": "A small domesticated carnivorous mammal.",
        "Elephant": "A large herbivorous mammal with a trunk.",
        "Ocean": "A large body of salt water covering most of Earth's surface.",
        "Sun": "The star at the center of our solar system.",
        "Mountain": "A large natural elevation of Earth's surface."
    }

    mode = st.radio("Choose a mode:", ["Learn Words", "Take a Quiz"])
    
    if mode == "Learn Words":
        # Display random word or allow manual selection
        if st.button("Show a Random Word"):
            random_word = random.choice(list(vocab_words.keys()))
            st.subheader(f"Word: {random_word}")
            st.write(f"Definition: {vocab_words[random_word]}")
        word = st.selectbox("Or, Choose a Word to Learn", list(vocab_words.keys()))
        st.subheader(f"Word: {word}")
        st.write(f"Definition: {vocab_words[word]}")
    
    elif mode == "Take a Quiz":
        # Randomly ask for definitions of words
        word = random.choice(list(vocab_words.keys()))
        st.write(f"What is the definition of '{word}'?")
        
        user_answer = st.text_input("Your Answer:")
        if st.button("Submit"):
            correct_answer = vocab_words[word]
            if user_answer.lower() in correct_answer.lower():
                st.success("Correct!")
            else:
                st.error(f"Wrong. The correct definition is: {correct_answer}")

# Story Time with Images and Read-Aloud Simulation
elif module == "Story Time":
    st.header("Story Time")
    stories = {
        "The Little Red Riding Hood": {
            "text": """
            Once upon a time, there was a little girl who wore a red hood. She went to visit her grandmother, 
            but on her way, she met a wolf who tried to trick her...
            """,
            "image": "https://example.com/red_riding_hood.jpg"
        },
        "The Tortoise and the Hare": {
            "text": """
            A hare made fun of a slow-moving tortoise. The tortoise challenged the hare to a race, and through 
            steady progress, the tortoise won the race...
            """,
            "image": "https://example.com/tortoise_hare.jpg"
        }
    }

    story = st.selectbox("Pick a Story to Read", list(stories.keys()))
    st.subheader(f"Story: {story}")
    st.write(stories[story]["text"])
    
    # Display story image
    st.image(stories[story]["image"], caption=story)

    # Simulate Read-Aloud functionality
    if st.button("Listen to the Story"):
        st.info("Playing story audio... (Simulation)")

# Educational Videos with Search Capability
elif module == "Educational Videos":
    st.header("Educational Videos for Kids")
    st.write("Watch fun and educational videos!")
    
    videos = {
        "ABC Song": "https://www.youtube.com/embed/75p-N9YKqNo",
        "Counting Numbers": "https://www.youtube.com/embed/0TgLtF3PMOc",
        "Planet Song": "https://www.youtube.com/embed/ZHAqT4hXnMw",
        "Shapes Song": "https://www.youtube.com/embed/RNUZBHlRH4Y",
    }
    
    # Search feature
    search_term = st.text_input("Search for a video (e.g., ABC, Numbers, Planets):")
    
    if search_term:
        found_videos = {title: url for title, url in videos.items() if search_term.lower() in title.lower()}
        if found_videos:
            video_choice = st.selectbox("Choose a video to watch", list(found_videos.keys()))
            st.video(found_videos[video_choice])
        else:
            st.error("No videos found with that search term. Please try again.")
    else:
        video_choice = st.selectbox("Choose a video to watch", list(videos.keys()))
        st.video(videos[video_choice])

# Deploy by running: streamlit run app.py
