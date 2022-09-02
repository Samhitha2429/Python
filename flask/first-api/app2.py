from flask import Flask, jsonify, request

app = Flask(__name__)
stores = [{"name": "t-Shirt", "qty": 56}, {"name": "pant", "qty": 36}]


@app.route("/store/<int:storeId>/item/<int:itemId>qty", methods=["POST"])
def changeStore(storeId, itemId):
    requestObj = request.get_json()
    for store in stores:
        if store["id"] == storeId:
            for item in store["items"]:
                if item["id"] == "itemId":
                    item["qty"] == requestObj['qty']
                    print(stores)
                else:
                    print("item not found")
        else:
            print("store not found")
    return


app.run(debug=True, port=5000)
