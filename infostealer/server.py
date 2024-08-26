from flask import Flask, request

app = Flask(__name__)

@app.post("/")
def root():
    data = request.json['info']
    
    with open("target_information.txt", "w") as file:
         file.write(data)
         
    return "OK"

if __name__ == "__main__":
     app.run(port=3000)
    
