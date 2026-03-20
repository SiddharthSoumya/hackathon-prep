import requests
import json

def show(label,response):
    print(f"\n{'='*40}")
    print(f" {label}")
    print(f"Status code: {response.status_code}")
    print(f"Response : {json.dumps(response.json(),indent=2)}")

response = requests.get("https://api.agify.io/?name=ravi")
show("Agify - guess age from name", response)

response=requests.get("https://jsonplaceholder.typicode.com/todos")
todos=response.json()

print(f"\n{'='*40}")
print(f"First 5 todos from JSONPlaceholder")
for todo in todos[:5]:
    status="✅ " if todo["completed"] else "o"
    print(f" [{status}] {todo['id']}. {todo['title']} ")


new_note={
    "title":"My first POST request",
    "body":"FastAPI is going to be fun",
    "userId":1
}

response=requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_note
)
show("POST - create a fake post",response)



response=requests.get("https://jsonplaceholder.typicode.com/posts/1")
show("GET single post by ID",response)



response=requests.get("https://jsonplaceholder.typicode.com/posts/999999")
print(f"\n{'='*40}")
print(f"Intentional 404")
print(f"Status code: {response.status_code}")
if response.status_code ==404:
    print("Item not found - handle this gracefully!")




def fetch_and_save_remote_todos():
    response=requests.get("https://jsonplaceholder.typicode.com/todos")
    remote_todos=response.json()[:5]

    my_todos=[
        {
            "id":t["id"],
            "title":t["title"],
            "done":t["completed"]
        }
        for t in remote_todos
    ]

    with open("todos.json","w") as f:
        json.dump(my_todos,f,indent=2)

    print(f"saved {len(my_todos)} todos from the internet!")

fetch_and_save_remote_todos()