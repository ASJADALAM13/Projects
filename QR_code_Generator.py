from flask import Flask, render_template, request, jsonify
import qrcode as qr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    url = request.form['link']
    
    # QR code generation code
    myqr = qr.QRCode(
        version=1,
        error_correction=qr.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4
    )
    myqr.add_data(url)
    myqr.make(fit=True)
    img = myqr.make_image(fill_color="red", back_color="white")

    # Save the image
    img_path = f"static/qrcodes/{url.replace('/', '_')}.png"
    img.save(img_path)

    # Provide the image path to the frontend
    return jsonify({'qrCode': img_path})

if __name__ == '__main__':
    app.run(debug=True)
