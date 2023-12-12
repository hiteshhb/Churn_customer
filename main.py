from flask import Flask, jsonify, render_template, request

from project_app.utils import PredictionData

# Creating instance here
app = Flask(__name__)


@app.route("/") 
def hello_flask():
    print("Customer Churn Prediction")   
    return render_template("index.html")

# For testing on html
@app.route("/prediction", methods = ["POST", "GET"])
def get_prediction():
    if request.method == "GET":

        Age                         = float(request.args.get("Age"))
        Gender                      = (request.args.get("Gender"))
        Location                    = (request.args.get("Location"))
        Subscription_Length_Months  = float(request.args.get("Subscription_Length_Months"))
        Monthly_Bill                = float(request.args.get("Monthly_Bill"))
        Total_Usage_GB              = float(request.args.get("Total_Usage_GB"))

        predict = PredictionData(Age ,Gender,Location,Subscription_Length_Months,
                                Monthly_Bill,Total_Usage_GB )        
        result = predict.get_prediction()

        if result==1:
            result = "Customer would be Churn"
            return render_template("index.html", prediction = result)   #For html
        else:
            result = "Customer would not be Churn"
            return render_template("index.html", prediction = result)   #For html



# # For testing on Postman 
# @app.route("/prediction", methods = ["POST", "GET"])
# def get_prediction():
#     if request.method == "GET":

#         data = request.form

#         Age                         = eval(data["Age"])
#         Gender                      = data["Gender"]
#         Location                    = data["Location"]
#         Subscription_Length_Months  = eval(data["Subscription_Length_Months"])
#         Monthly_Bill                = eval(data["Monthly_Bill"])
#         Total_Usage_GB              = eval(data["Total_Usage_GB"])

  
#         predict = PredictionData(Age ,Gender,Location,Subscription_Length_Months,
#                                 Monthly_Bill,Total_Usage_GB )        
#         result = predict.get_prediction()

#         if result==1:
            # result = "Customer would be Churn"
#             return jsonify({"Result": result})    # For Postman testing
#         else:
#             result = "Customer would not be Churn"
#             return jsonify({"Result": result})    # For Postman testing
        


if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= 5005, debug = False)  # By default Prameters