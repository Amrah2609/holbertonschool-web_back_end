#!/usr/bin/env python3
"""
Flask i18n app
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    """
    Main page of the app
    """
    return render_template('0-index.html')
