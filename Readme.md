# Readme 

This readme will showcase use of Sample Mood detection project in which 
we have a keras's saved model in python. We will be using that to create REST Api to deploy in production.

## Setting up virtual environment
You must have Python 3.6 installed on your system.

Install the virtual environment

    $ pip install virtualenv

Create the virtual environment

    $ virtualenv -p python3.6 venv

Activate virtual environment

    $ source venv/bin/activate

Install the requirements by using the below command:

    $ pip install -r requirements.txt

## Running the program
You can run the program from command line using below command from the root of the project directory.

    $ python src/main.py
    
Program output:
```text
 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 120-061-301
```
Now our server is running on localhost at 5000 port.

.Sample Input
```json
{
	"text": "great i am liking it"
}
```

.Output
```json
{
    "anger": 7.112710922956467,
    "disgust": 3.1775277107954025,
    "fear": 12.434638291597366,
    "guilt": 2.8116755187511444,
    "joy": 56.977683305740356,
    "sadness": 13.96680623292923,
    "shame": 3.2702498137950897
}
```
