from flask import Blueprint, request, jsonify


# Define the Blueprint
api = Blueprint('api', __name__)

@api.route('/discord-invite', methods=['GET'])
def discord_invite():
    """
    Returns the Discord invite link as a JSON response.
    """
    return jsonify({
        "invite_url": "https://discord.gg/svVAnQ8z"
    })
