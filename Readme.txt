Do a POST request at "http://127.0.0.1:8000/lstm/"

Sample request:
{
    "text":"I am an entrepreneur at heart. I love building new businesses and teams and creating value for stakeholders and consumers. And I have done this regardless of the success or failure I have achieved through the decades. I believe strongly that neither success nor failure are permanent aspects of life and as we learn to let go of failures, so we should learn to let go of past success. Eventually, I am a kind of person, who would want to see myself having trying everything I have wanted to do, never regretting of letting go of a chance. I am generally social, like to lead from the front and fond of constantly learning new things with every turn of the page of my life. ",
    "ques":5
}    

Here ques is question number and text is response to the answer

Sample Response:
{
    "status": "succes",
    "rank": "Below Average"
}

How to start the server:
1. Change the directory into project folder
2. type: "py manage.py runserver"

Packages to be installed:
1. django
2. tensorflow
3. nltk