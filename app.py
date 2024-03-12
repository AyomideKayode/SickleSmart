#!/usr/bin/python3

"""
Entry point module for the SickleSmart website where the execution will take place.
"""

from sicklesmart_web import create_app

# Create the Flask application instance
app = create_app()

if __name__ == '__main__':
    # Run the Flask application in debug mode if this script is executed directly
    app.run(debug=True)
