from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure email settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'alexhenton@gmail.com'
app.config['MAIL_PASSWORD'] = 'jqre kyhy bwjt fvdh'

mail = Mail(app)

@app.route('/send-email', methods=['POST'])
def send_email():
    name = request.form.get('name')
    email = request.form.get('email')
    message_content = request.form.get('message')

    if not name or not email or not message_content:
        return jsonify({'error': 'Missing fields'}), 400

    msg = Message(
        subject=f"Message from {name}",
        sender=email,
        recipients=['alexhenton@gmail.com'],
        body=message_content
    )

    mail.send(msg)
    return jsonify({'success': 'Email sent successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
