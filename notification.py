from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/notifications', methods=['POST'])
def notifications():
    # Microsoft Graph sends a validation token on subscription creation to verify the endpoint
    if 'validationToken' in request.args:
        validation_token = request.args['validationToken']
        print(validation_token, 200, {'content-type': 'text/plain'})
        return {"body":validation_token+' 200'}
    
    # Handle notifications
    notifications = request.json
    print("Received notification:")
    print(notifications)
    
    # Respond with 202 Accepted
    return '', 202

if __name__ == '__main__':
    # Run on port 5000 accessible externally or use ngrok for tunneling
    app.run(host='0.0.0.0', port=5000)




