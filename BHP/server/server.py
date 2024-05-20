from flask import Flask,request,jsonify
import util
app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello, world!'

@app.route('/get_location_names')    #http andpoint expose.
def get_location_names():
    locations = util.get_location_names()
    response = jsonify({'locations': locations})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
  


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    
        # Extract parameters from the request form data
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        # Call the util function to get the estimated price
        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

        # Create JSON response with the estimated price
        response = jsonify({'estimated_price': estimated_price})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
        
   
if __name__ == "__main__":
    print("Loading artifacts for home price prediction...")
    util.load_saved_artifacts()
    print("Starting python flask server for home price prediction...")
    app.run()