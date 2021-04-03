from woocommerce import API
import json

wcapi = API(
    url="http://pos.sharpwp.com/",
    consumer_key="ck_b1438481a2274b8cf70afaa3b1d74f11087fe3cd",
    consumer_secret="cs_ef6b3e25f5e31ed2279f927042726b5657de97e4",
    wp_api=True,
    version="wc/v3",
)

# print(wcapi.get("customers").text)
#
# print(type(wcapi.get("customers").json()))
#
# todos = wcapi.get("customers").json()
#
# print(todos[0]['id'])
# print(todos[0]['first_name'])
#
# for todo in todos:
#     print("ID's are: " + str(todo["id"]))
#     print(str(todo['first_name']))


# distros_dict = json.loads(wcapi.get("customers").json())

# print(distros_dict.type)


# print(wcapi.get("products").json())

class ApiProvider:
    @staticmethod
    def getCustomer():
        f = open("customers.txt", "w")
        f.write(str(wcapi.get("customers").json()))
        f.close()
        return wcapi.get("customers").json()

    @staticmethod
    def getProduct():
        f = open("products.txt", "w")
        f.write(str(wcapi.get("products").json()))
        f.close()
        return wcapi.get("products").json()

    @staticmethod
    def createUser(data):
        print(wcapi.post("customers", json.loads(data)).json())
