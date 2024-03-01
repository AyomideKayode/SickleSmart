#!/usr/bin/python3

"""Entry point module for the website where the execution will take place.
"""

from sicklesmart_web import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
