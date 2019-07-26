import os, subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
	defaultText = "print('hello')"
	if request.method == "POST":
		if request.form.get('Run_button') == 'Run':
			textEnteredInEditor = request.form['editorText']
			textToDisplay = saveTextAndRun(textEnteredInEditor)
			return render_template('index.html', displayText = textEnteredInEditor, outputText = textToDisplay)
		elif request.form.get('Save_button') == 'Save':
			textEnteredInEditor = request.form['editorText']
			saveText(textEnteredInEditor)
			return render_template('index.html', displayText = textEnteredInEditor, outputText = "File saved")
		else:
			return render_template('index.html', displayText = defaultText, outputText = "")
	else:
		return render_template('index.html', displayText = defaultText, outputText = "")
	
def saveTextAndRun(textEnteredInEditor):
	with open('tortoiseCode/saveCode.py','w') as content_file:
		content_file.write(textEnteredInEditor)
	#exec(textEnteredInEditor)
	subprocess.call(["python tortoiseCode/saveCode.py 2>&1 | tee terminalOutput.txt"], shell=True)
	#subprocess.call(["python3", "saveCode.py", "2>&1|tee terminalOutput.txt"])
	with open('terminalOutput.txt', 'r') as content_file:
		content = content_file.read()
		return content

def saveText(textEnteredInEditor):
	with open('tortoiseCode/saveCode.py','w') as content_file:
		content_file.write(textEnteredInEditor)


if __name__ == '__main__':
	#app.run(host=os.getenv('IP','10.42.0.139'), port=int(os.getenv('PORT', 8080)), debug = True)
	app.run(host=os.getenv('IP','127.0.0.1'), port=int(os.getenv('PORT', 8080)), debug = True)
