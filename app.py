import streamlit as st
import preprocessor
import helper
import matplotlib.pyplot as plt

st.sidebar.title("Whatsapp Chat Analyser")

uploaded_file = st.sidebar.file_uploader("Choose a file")

# DATA SOURCE
if uploaded_file is not None:
    data = uploaded_file.getvalue().decode("utf-8")
else:
    st.info("No file uploaded. Using sample chat data.")
    with open("sample_chat.txt", "r", encoding="utf-8") as f:
        data = f.read()


# PREPROCESS
df = preprocessor.preprocess(data)

# user list
if 'users' not in df.columns:
    st.error("Preprocessing failed: 'users' column missing")
    st.stop()

user_list = (
    df.loc[df['users'] != 'group_notification', 'users']
    .dropna()
    .unique()
    .tolist()
)

user_list.sort()
user_list.insert(0, "Overall")


selected_user = st.sidebar.selectbox("Show analysis wrt", user_list)


if st.sidebar.button("Show Analysis"):

    st.title("Top Statistics")

    num_messages, words, media_message, link = helper.fetch_stats(selected_user, df)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.header("Total Messages")
        st.title(num_messages)

    with col2:
        st.header("Total Words")
        st.title(words)
    
    with col3:
        st.header("Media shared")
        st.title(media_message)

    with col4:
        st.header("Links shared")
        st.title(link)

    # timeline
    st.title("Monthly Timeline")

    timeline = helper.monthly_timeline(selected_user, df)

    fig, ax = plt.subplots()
    ax.plot(timeline['time'], timeline['messages'], color='green')
    ax.set_ylabel("Message Count")
    ax.set_xlabel("Month")

    plt.xticks(rotation='vertical')
    plt.tight_layout()

    st.pyplot(fig)


    # MOST BUSY USERS
    if selected_user == "Overall":
        st.title("Most Chatty Users")

        x, new_df = helper.fetch_most_chatty_users(df)

        fig, ax = plt.subplots()

        col1, col2 = st.columns(2)

        with col1:
            ax.bar(x.index, x.values, color='red')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.dataframe(new_df)


    # WORDCLOUD
    st.title("WordCloud")

    df_wc = helper.create_wordcloud(selected_user, df)

    fig, ax = plt.subplots()
    ax.imshow(df_wc)
    ax.axis("off")

    st.pyplot(fig)

    # MOST COMMON WORDS
    st.title("Most Common Words")

    most_common_df = helper.most_common_words(selected_user, df)

    fig, ax = plt.subplots()
    ax.barh(most_common_df['word'], most_common_df['count'])

    st.pyplot(fig)

    # EMOJI ANALYSIS
    st.title("Emoji Analysis")

    emoji_df = helper.emoji_helper(selected_user, df)

    col1, col2 = st.columns(2)

    with col1:
        st.dataframe(emoji_df)

    with col2:
        fig, ax = plt.subplots()
        fig, ax = plt.subplots()

        ax.pie(
            emoji_df['count'].head(),
            labels=emoji_df['emoji'].head(),
            autopct="%0.2f"
        )

        st.pyplot(fig)
