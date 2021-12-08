# sentiment-analysis-web-app

Short and simple streamlit web app for sentiment analysis, containerized.
This app was few tested with seleniumbase.

Update : tests do not work anymore. One day it works, the next day it does not... Magic of computers...

## Launch the app

cd to the project location and run

    - docker-compose up
  
## Make analysis 

Enter in the text section a sentence and click analyse to get the result sentiment of your phrase

## When you are done

    - docker-compose down

# Details

If you cancel the docker while building the image (like you do Crtl C). You will need to run :

    - docker-compose down
    - docker-compose up --build