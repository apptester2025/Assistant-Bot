from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

@app.route('/api/discord-invite', methods=['GET'])
def discord_invite():
    # Replace with your actual Discord invite link
    return jsonify({
        "invite_url": "https://discord.gg/your-invite-link"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)