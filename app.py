from flask import Flask, render_template, request, flash, redirect, url_for
import yaml
from yaml.loader import UnsafeLoader
import subprocess

app = Flask(__name__)
app.secret_key = '12122323'

# Vulnerable deserialization function
def deserialize_yaml(yaml_data):
    try:
        # Unsafe loading
        data = yaml.load(yaml_data, Loader=UnsafeLoader)
        return data
    except yaml.YAMLError as e:
        return str(e)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        yaml_data = request.form['yaml_data']
        
        result = deserialize_yaml(yaml_data)
        
        flash(f"Deserialized Data: {result}", 'info')
        return redirect(url_for('index'))
    
    return render_template('index.html')

@app.route('/advanced', methods=['GET', 'POST'])
def advanced():
    if request.method == 'POST':
        yaml_data = request.form['yaml_data']
        
        result = deserialize_yaml(yaml_data)
        
        flash(f"Deserialized Data: {result}", 'info')
        return redirect(url_for('advanced'))
    
    return render_template('advanced.html')

if __name__ == '__main__':
    app.run(debug=True)
