from flask import Flask, jsonify
import os
import sys

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'CI/CD Pipeline Demo',
        'version': '1.0.0',
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'status': 'running'
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'checks': {
            'application': 'pass',
            'database': 'pass'
        }
    }), 200

@app.route('/ready')
def ready():
    return jsonify({'status': 'ready'}), 200

@app.route('/api/version')
def version():
    return jsonify({
        'version': '1.0.0',
        'python': sys.version,
        'commit': os.getenv('GIT_COMMIT', 'unknown')
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
