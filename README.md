To check the working of the application:

- Install the requirements for the project using "pip install -r requirements.txt" (<- Without the quotes)

- Run the application using the command:
        "python manage.py runserver" (<- Without the quotes)
        Make sure you're at the level of the manage.py file.

- Here we've used the Django REST Framework since we don't have a UI to populate.
  So it would be useful to use POSTMAN or another similar tool to check the working.

- Both, the successful and unsuccessful URLs are GET requests so you'll not need to include anything in the body of
  the request.


Working:
    1. Successful GET request
       URL: http://127.0.0.1:8000/weather/get_weather_data_successful

    2. Unsuccessful GET request
       URL: http://127.0.0.1:8000/weather/get_weather_data_unsuccessful


- I have added "print" statements to the code to show the repeated attempts in working,
  so please keep an eye on the terminal in order to verify the retry attempts.


Email: kunkulol.apurva@gmail.com

