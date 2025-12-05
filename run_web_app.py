"""
Simple script to run the Flask web application
"""
import subprocess
import sys

def install_flask():
    """Install Flask if not available"""
    try:
        import flask
        print("Flask is already installed")
    except ImportError:
        print("Installing Flask...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])

def run_app():
    """Run the Flask application"""
    install_flask()
    print("\nStarting Flight Delay Prediction Web App...")
    print("Open your browser and go to: http://127.0.0.1:5000")
    print("Press Ctrl+C to stop the server")
    
    from app import app
    app.run(debug=True, host='127.0.0.1', port=5000)

if __name__ == "__main__":
    run_app()