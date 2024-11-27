from flask import Flask,render_template
from flask import request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/palindrome',methods=["POST"])
def palindrome():
    myString=request.form['palin']
    lowerString=myString.lower()
    revString=lowerString
    print(lowerString)
    
    revObj=reversed(revString)
    print(revObj)
    revList=list(revObj)
    print(revList)
    lowerStringList=list(lowerString)
    print(lowerStringList)

    
    message=f'<h1>Original string={myString}<br>'
    message+=f'lower case={lowerString}<br>'
    
    message+=f'revList={revList}<br>'
    message+=f'OriginalList={lowerStringList}</h1><br>'

    if lowerStringList==revList:
        message+=f'<h1>{myString} is Palindrome</h1>'
    else:
        message+=f'<h1>{myString} is NOT Palindrome</h1>'


    return message

if __name__=='__main__':
    app.run(debug=True)