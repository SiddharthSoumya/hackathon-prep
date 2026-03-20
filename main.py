from fastapi import FastAPI

# Create the app instance — this is your entire API
app=FastAPI()

@app.get("/")
def root():
    return {"message":"I am alive","status":"running"}

# path parameter {}
@app.get("/greet/{name}")
def greet(name:str):
    return{
        "greeting":f"Hello,{name}!",
        "length":len(name)
    }

# query parameter
@app.get("/add")
def add(a:int,b:int):
    return{
        "a":a,
        "b":b,
        "result":a+b
    }


# Optional query parameter

@app.get("/temperature/{value}")
def temperature(value:float,unit:str="celsius"):
    if unit =="celsius":
        converted = (value * 9/5) + 32
        return {"input":value,"unit":"celsius","converted_to":"fahrenheit","result":round(converted,2)}
    else:
        converted=(value-32)*5/9
        return {"input":value,"unit":"fahrenheit","converted_to":"celsius","result":round(converted,2)}
    

 