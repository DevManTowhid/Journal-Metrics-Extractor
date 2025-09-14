from flask import Flask, request, render_template

import utils

app = Flask(__name__)

@app.route('/')




@app.route('/extract', methods=['POST'])

def extract_metrics():
    url = request.form['url'] # Required URL input
    pdf_path = request.files.get('pdf') # Optional PDF upload
    if url:
        metrics = utils.extract_data_from_url(url)
    elif pdf_path:
        metrics = utils.extract_data_from_pdf(pdf_path)
    return render_template('results.html', metrics=metrics)

