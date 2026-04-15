from wordcloud import WordCloud
from urlextract import URLExtract
import pandas as pd
from collections import Counter
import emoji

extract = URLExtract()



def fetch_stats(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['users'] == selected_user]

    df = df.dropna(subset=['messages'])

    num_messages = df.shape[0]

    # words 
    words = df['messages'].astype(str).str.split().sum()

    # media
    media_message = df['messages'].str.contains('<Media omitted>', na=False).sum()

    # links
    links = df['messages'].apply(lambda x: extract.find_urls(str(x))).sum()

    return num_messages, len(words), media_message, len(links)
                                                        
# MOST CHATTY USERS
def fetch_most_chatty_users(df):

    x = df['users'].value_counts().head()

    percent_df = (
        (df['users'].value_counts() / df.shape[0]) * 100
    ).round(2).reset_index()

    percent_df.columns = ['name', 'percent']

    return x, percent_df


# WORDCLOUD
def create_wordcloud(selected_user, df):

    with open('stop_hinglish.txt', 'r') as f:
        stop_words = set(f.read().split())

    if selected_user != 'Overall':
        df = df[df['users'] == selected_user]

    df = df[
        (df['users'] != 'group_notification') &
        (df['messages'] != '<Media omitted>\n')
    ]

    messages = df['messages'].dropna().astype(str)

    def clean_message(message):
        return " ".join([
            word for word in message.lower().split()
            if word not in stop_words
        ])

    cleaned = messages.apply(clean_message)

    wc = WordCloud(
        width=500,
        height=500,
        min_font_size=10,
        background_color='white'
    )

    return wc.generate(cleaned.str.cat(sep=" "))


# MOST COMMON WORDS
def most_common_words(selected_user, df):

    with open('stop_hinglish.txt', 'r') as f:
        stop_words = set(f.read().split())

    if selected_user != 'Overall':
        df = df[df['users'] == selected_user]

    df = df[
        (df['users'] != 'group_notification') &
        (df['messages'] != '<Media omitted>\n')
    ]

    words = (
        df['messages']
        .dropna()
        .astype(str)
        .str.lower()
        .str.split()
        .explode()
    )

    words = words[~words.isin(stop_words)]

    most_common_df = pd.DataFrame(
        words.value_counts().head(20)
    ).reset_index()

    most_common_df.columns = ['word', 'count']

    return most_common_df


# EMOJI ANALYSIS
def emoji_helper(selected_user, df):

    if selected_user != "Overall":
        df = df[df['users'] == selected_user]

    df = df.dropna(subset=['messages'])

    emojis = (
        df['messages']
        .astype(str)
        .apply(lambda x: [c for c in x if emoji.is_emoji(c)])
        .explode()
        .dropna()
    )

    emoji_df = pd.DataFrame(
        emojis.value_counts()
    ).reset_index()

    emoji_df.columns = ['emoji', 'count']

    return emoji_df


# MONTHLY TIMELINE
def monthly_timeline(selected_user, df):

    if selected_user != "Overall":
        df = df[df['users'] == selected_user]


    if 'month_num' not in df.columns:
        df['month_num'] = df['date'].dt.month

    timeline = (
        df.groupby(['year', 'month_num', 'month'])['messages']
        .count()
        .reset_index()
    )

    timeline = timeline.sort_values(['year', 'month_num'])

    timeline['time'] = timeline['month'] + "-" + timeline['year'].astype(str)

    return timeline