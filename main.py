from fastapi import FastAPI
import json
import os
from datetime import datetime

app = FastAPI()

File_name = "student.json"

def read_data():
    if os.path.exists(File_name):
        return()
    with open(File_name , "r") as file:
        json.load(file)

def write_data(data):
    with open(File_name , "w") as file:
        json.dump(data,file,indent=4)

@app.get("/")
def home():
    return{"message":"Welcome to Student API"}

@app.get("/students")
def get_students():
    return{read_data}

@app.post("/student")
def add_student(student:dict):
    students = read_data()

    for s in students:
        if s["id"] == student["id"]:
            return{"error":"student with this ID is already exists"}
        
    student["added_on"] = datetime.now().strftime("")

    students.append(student)
    write_data(students)

    return {"message": "student added successfully", "student": student}

@app.get("/students/{id}")
def get_student(id : int):
    students = read_data()

    for student in students:
        if student["id"] == id:
            return student

    return {"error": "student not found"}

@app.delete("Delete/students/{id}")
def delete_student(id : int):
    students = read_data()

    new_student=[]
    found = False

    if 