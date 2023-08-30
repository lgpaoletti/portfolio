from flask import Flask, render_template, request, redirect
app = Flask(__name__) #we create our app
#print(__name__) #__main__

#this gives us some extra tools to build the server
#everytime we hit / (the route) we define a function called hello_world
#@app.route('/<username>/<int:post_id>')  
#def hello_world(username=None, post_id=None): #default parameter
    #per accedere ad username passiamo da html, praticamente legge cosa mettiamo nell'url
    #idem con il post_id
    #print(url_for('static', filename='bolt.ico') )->static/bolt.ico
    #return render_template('./index.html', name=username, post_id=post_id) #per runnare un file HTML dobbiamo creare una cartella dentro la cartella del server, in modo da scrivere ./file.html


#To run the application you can either use the flask command or python’s -m switch with Flask. 
#Before you can do that you need to tell your terminal the application to work with by exporting the FLASK_APP environment variable
#CMD: C:\path\to\app>set FLASK_APP=hello.py
#PowerShell: C:\path\to\app> $env:FLASK_APP = "hello.py"
#then we must enter: python -m flask run
#the output will the us: 
# * Serving Flask app 'server.py'
# * Debug mode: off
#WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
# * Running on http://127.0.0.1:5000, THIS IS OUR WEBSITE

#everytime we want to re-run the code, we must do CTRL+C and repeat flask run

#per evitare che ogni cambiamento non sia notato finchè non chiudiamo la run
#set FLASK_ENV=development
#set FLASK_DEBUG=1
#flask run

#@app.route('/blog')  
#def blog():
    #return 'These are my thoughts on blogs'

#ora se faccio: http://127.0.0.1:5000/blog mi esce questa frase

#@app.route('/blog/2020/dogs')  
#def blog2():
    #return 'This is Pedro Pedrito'

#per runnare un file HTML dobbiamo creare una cartella dentro la cartella del server, in modo da scrivere ./file.html

#@app.route('/aboutme')  
#def hello_world2():
    #return render_template('./about.html')

#Static files: sono CSS and JS, creiamo una cartella static in cui metterli
#bisogna però aggiornare dove sono i file nel codice html

#adding a favicon: we must download an image a ICO file
#https://flask.palletsprojects.com/en/1.1.x/patterns/favicon/
#la favicon è un'immagine che sta affianco al nome del sito, in questo caso avremo:
# (fulmine) LUCA GIORGIO PAOLETTI

#flask has also variable rules: https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules

#when trhough the chrome we go to the file we find that its content type is text/html
#this is important cause it uses a MIME type: https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types
#browsers use the MIME type, NOT THE FILE EXTENSION, to determine how to process the URL

##################################################################################################
#FROM NOW ON IT STARTS THE CODING FOR OUR PORTFOLIO:
#useful links for templates:
#https://html5up.net/
#https://themewagon.com/author/mashuptemplate/
#https://www.creative-tim.com/bootstrap-themes/free


@app.route('/')
def my_home():
    return render_template('./index.html')

@app.route('/<string:page_name>') #to avoid copying and pasting the same line everytime
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database: #mode 'a' means that we append to a file that already exists
        email=data['email']
        subject=data['subject']
        message=data['message']
        file= database.write(f'\n{email},{subject},{message}')

#it is better to store the data on a CSV or an Excel, not in a txt
#Python has a CSV module which will help us
#https://docs.python.org/3/library/csv.html
import csv #Comma Separated Values

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2: #mode 'a' means that we append to a file that already exists
        email=data['email']
        subject=data['subject']
        message=data['message']
        csv_writer= csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #database2 is where we will save the data, delimiter is how we are going to delimit different columns
        csv_writer.writerow([email, subject, message]) 

#how to request data: https://flask.palletsprojects.com/en/1.1.x/quickstart/#accessing-request-data
#needed to contact

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
        try: 
            data=request.form.to_dict() #it turns the data to a dictionary
            write_to_csv(data)
            write_to_file(data)
            return redirect('/thankyou.html')
        except:
            return('ERROR: did not save to database.')
    else:
        return 'Something went wrong, try again!'

from PIL import Image, ImageFilter
img=Image.open(r"C:\Users\paole\Downloads\INFORMATICA\PYTHON\Teoria\Chap15_Utilities\project_files\static\assets\images\profil.jpg")
img2=img.convert('L') #this format is called grayscale->balck and white
file_name=r"C:\Users\paole\Downloads\INFORMATICA\PYTHON\Teoria\Chap15_Utilities\project_files\static\assets\images\profil.jpg"
img2.save(file_name, 'JPEG')

#the problem now is that the website is linked to the host, only we can access it
#https://help.pythonanywhere.com/pages/Flask/
#now, from GitHub we must do in the cmd:
# git clone git@github.com:lgpaoletti/portfolio.git




















