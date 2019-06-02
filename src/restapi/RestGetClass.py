import requests
import json

class SimpleGetClass():

    BASE_URL = "https://reqres.in"
    def getClass(self):
        print(self.BASE_URL)
        response = requests.get(self.BASE_URL+"/api/users?page=2")
        print(response)
        print(response.json())

def main():
    api = SimpleGetClass()
    api.getClass()

if __name__ == '__main__':
    main()