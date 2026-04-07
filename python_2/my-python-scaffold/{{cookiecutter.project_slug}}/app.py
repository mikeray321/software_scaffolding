from flask import Flask
import os

app = Flask(__name__)

# Injection via Cookiecutter (Static)
PROJECT_NAME = "{{ cookiecutter.project_name }}"

@app.route("/")
def hello():
    return {
        "message": f"Hello from {PROJECT_NAME}!",
        "status": "up"
    }

if __name__ == "__main__":
    # Injection via Environment Variable (Dynamic/Runtime)
    # This allows the Platform to override the port later if needed
    port = int(os.getenv("PORT", {{ cookiecutter.app_port }}))
    app.run(host="0.0.0.0", port=port)
