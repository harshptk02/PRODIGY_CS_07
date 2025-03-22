from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_cipher(text, shift, mode):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        text = request.form['text']
        shift = int(request.form['shift'])
        mode = request.form['mode']
        result = caesar_cipher(text, shift, mode)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)