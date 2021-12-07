from re import S
import streamlit as st

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
 
sid_obj = SentimentIntensityAnalyzer()


def sentiment_scores(sentence):

    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)
     
    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
        return("Positive")
 
    elif sentiment_dict['compound'] <= - 0.05 :
        return("Negative")
 
    # else
    return("Neutral")
    

def main():

    st.title("Enabling sentiment analysis")
    st.subheader("Welcome ! Here we are, make machine learning works")

    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        with st.form(key='nlpForm'):
            raw_text = st.text_area(label="Enter your text here")
            submit_button = st.form_submit_button(label="Analyze")

        with st.container():
            st.info('Results')
            st.write(sentiment_scores(raw_text))

    
    else:
        st.subheader("About")


if __name__ == '__main__':
    main()