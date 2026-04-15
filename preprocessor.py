import re
import pandas as pd

def preprocess(data):
    # pattern for WhatsApp datetime
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'
    
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    # dataframe
    df = pd.DataFrame({
        'user_message': messages,
        'message_date': dates
    })

    # convert to datetime
    df['message_date'] = pd.to_datetime(
        df['message_date'], 
        format='%d/%m/%y, %H:%M - ', 
        errors='coerce'
    )

    df.rename(columns={'message_date': 'date'}, inplace=True)

    # USER + message
    df[['users', 'messages']] = df['user_message'].str.extract(
        r'^([^:]+):\s(.*)', expand=True
    )

    # handle group notifications
    df['users'].fillna('group_notification', inplace=True)
    df['messages'].fillna(df['user_message'], inplace=True)

    df.drop(columns=['user_message'], inplace=True)

    # TIME FEATURES
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    # PERIOD 
    df['period'] = df['hour'].apply(
        lambda h: f"{h:02d}-00" if h == 23 
        else f"00-{h+1:02d}" if h == 0 
        else f"{h:02d}-{h+1:02d}"
    )

    # VALIDATION
    if 'users' not in df.columns:
        raise ValueError("users column not created — parsing failed")

    return df