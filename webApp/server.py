import os, subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
	defaultText = "print('hello')"
	if request.method == "POST":
		receivedText = request.form['editorText']
		outputText = saveTextAndRun(receivedText)
		return render_template('index.html', displayText = receivedText, outputText = outputText)
	else:
		return render_template('index.html', displayText = defaultText, outputText = "")
	
def saveTextAndRun(receivedText):
	with open('tortoiseCode/saveCode.py','w') as content_file:
		content_file.write(receivedText)
	#exec(receivedText)
	subprocess.call(["python tortoiseCode/saveCode.py 2>&1 | tee terminalOutput.txt"], shell=True)
	#subprocess.call(["python3", "saveCode.py", "2>&1|tee terminalOutput.txt"])
	with open('terminalOutput.txt', 'r') as content_file:
		content = content_file.read()
		return content



if __name__ == '__main__':
	app.run(host=os.getenv('IP','10.42.0.139'), port=int(os.getenv('PORT', 8080)), debug = True)
