from flask import Flask
from flask_cors import CORS

from config import Config
from routes.auth import auth_bp
from database.db import create_tables

app = Flask(__name__)

# Load configuration
app.config["SECRET_KEY"] = Config.SECRET_KEY

# Enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})

# Create database tables if they don't exist
create_tables()

# Register routes
app.register_blueprint(auth_bp)


@app.route("/")
def home():
    return {
        "status": "success",
        "message": "Placement Portal Backend Running"
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )