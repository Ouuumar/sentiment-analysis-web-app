FROM seleniumbase/seleniumbase

WORKDIR /app

COPY . . 

CMD ["pytest", "test_api.py", "--browser=chrome",  "--headless"]
