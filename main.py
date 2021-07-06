# pip install -r requirements.txt
from flask import Flask, request, render_template
from cryptography.fernet import Fernet

app = Flask(__name__)

# key is generated
key = Fernet.generate_key()
# value of key is assigned to a variable
f = Fernet(key)

@app.route('/encrypt')
def encrypt():
	"""Returns entered text converted from the plaintext to the ciphertext"""
	text = request.args.get('string', "Please enter text for encrypting by format /encrypt?string=<string_to_encrypt>")
	text_in_bytes = bytes(text, 'utf-8')
	encrypted_code = f.encrypt(text_in_bytes)
	return render_template("index.html", text="Encrypted result: ", value=encrypted_code)


@app.route('/decrypt')
def decrypt():
	"""Returns entered text decrypted from the ciphertext"""
	text = request.args.get('string', "Please enter text for decrypting by format /decrypt?string=<string_to_decrypt>")
	text_in_bytes = bytes(text, 'utf-8')
	decrypted_code = f.decrypt(text_in_bytes)
	return render_template("index.html", text="Decrypted result: ", value=decrypted_code.decode())

if __name__ == '__main__':
	app.run(debug=True)
