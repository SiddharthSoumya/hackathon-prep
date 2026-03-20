import json
import os

FILE ="todos.json"

def load_todos():
    if not os.path.exists(FILE):
        return []
    with open(FILE,"r") as f:
        return json.load(f)

def save_todos(todos):
    with open(FILE,"w") as f:
        json.dump(todos,f,indent=2)


def add_todos(title):
    todos=load_todos()
    new_id=(max(t["id"] for t in todos) + 1) if todos else 1
    todos.append({"id":new_id,"title":title,"done":False})
    save_todos(todos)
    print(f" Added: '{title}' (id={new_id})")

def list_todos():
    todos=load_todos()
    if not todos:
        print("No todos yet!")
        return
    for t in todos:
        status="✅" if t["done"] else "o"
        print(f" [{status}] {t['id']}. {t['title']}")


def delete_todo(todo_id):
    todos=load_todos()
    todos =[t for t in todos if t["id"] !=todo_id]
    save_todos(todos)
    print(f" Deleted todo {todo_id}")
def mark_done(todo_id):
    todos=load_todos()
    found=False
    for t in todos:
        if t["id"]==todo_id:
            t["done"]=True
            found=True
            break
    if found:
        save_todos(todos)
        print(f"Marked {todo_id} as done!")
    else:
        print(f"❌ ID {todo_id} not found.")

while True:
    print("\n--- TO-DO APP ---")
    print("1.ADD 2.LIST 3.DELETE 4.DONE 5.QUIT")
    choice = int(input("Choose: ").strip())

    match choice:
        case 1:
            title=input("Title: ")
            add_todos(title)

        case 2:
            list_todos()

        case 3:
            todo_id=int(input("ID to delete: "))
            delete_todo(todo_id)

        case 4:
            todo_id=int(input("ID to mark done: "))
            mark_done(todo_id)
        case 5:
            print("Bye!!!")
            break

