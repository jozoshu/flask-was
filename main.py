"""
Web Application Server with Flask
"""

if __name__ == '__main__':
    try:
        from core.app import run_flask_app
    except Exception as e:
        raise ImportError('Could not execute Flask server!')
    run_flask_app(__name__)
