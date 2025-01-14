from flask import Blueprint, jsonify

# Define a new Blueprint instance
api = Blueprint('api', __name__)

@api.route('/discord-invite', methods=['GET'])
def discord_invite():
    return jsonify({
        "invite_url": "https://discord.gg/svVAnQ8z"
    })