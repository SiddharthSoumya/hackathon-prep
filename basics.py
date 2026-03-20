def greet(name):
    return f"Hello, {name}!"
print(greet("Priya"))

notes=["Buy milk","Exercise","Study FastAPI"]
notes.append("")
notes.remove("Buy milk")
print(notes)

user={"name":"Ravi","age":18,"skills":["Python","FastAPI"]}
print(user["name"])
print(user.get("email","Not found"))

for skill in user["skills"]:
    print(f"I know {skill}")

squares=[x**2 for x in range(1,6)]
print(squares)

name="Ravi"
score=95.678
print(f"Name: {name}, Score: {score:.2f}")