from fastapi import FastAPI, HTTPException
from models import DatabaseManager
from urllib.parse import quote
from messages import set_message

app = FastAPI(title="TasksApi",
    description="Welcome to the TasksApi",
    version="1.0.0")
db_manager = DatabaseManager("tasks.db")  # Nome do arquivo do banco de dados

MESSAGES = ['replacement', 'tutoring', 'introduction', 'undeclared']

get_message = lambda name, selected_time, message_type:  set_message(name, selected_time, message_type)

@app.post("/tasks/", tags=["Tasks Operations"])
async def create_task(student_name: str, phone: str, message_type: str, selected_time):
    """
    Creates a task to send a message via WhatsApp.

    Receives the student's name, phone number, message type, and a selected time.
    Checks if the message type is valid according to pre-defined options.
    Formats the message based on the selected type and time.
    Constructs the final link for sending the message via WhatsApp.
    Adds the task to the database and returns the task ID and the generated link.

    Args:
        student_name (str): Name of the student who is the recipient of the message.
        phone (str): Student's phone number in string format.
        message_type (str): Type of message to be sent. Must be among pre-defined options.
        selected_time: The selected time for message formatting.

    Returns:
        dict: A dictionary containing the task ID and the generated WhatsApp link.
    """
    if message_type not in MESSAGES:
        raise HTTPException(status_code=400, detail="Tipo de mensagem inválido")
    
    message = get_message(student_name, selected_time, message_type)
    
    message = quote(message)

    link = f"https://web.whatsapp.com/send?phone=+55{phone}&text={message}"

    task_id = db_manager.add_task(link)

    return {"id": task_id, "link": link}

@app.delete("/remove-task/{task_id}", tags=["Tasks Operations"])
async def remove_task(task_id: int):
    db_manager.remove_task(task_id)
    return {"message": "Task removed successfully"}

@app.get("/tasks/", tags=["Tasks Operations"])
async def get_tasks():
    tasks = db_manager.get_pending_tasks()
    return tasks