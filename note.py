from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI()

class NoteCreate(BaseModel):
    tittle: str
    content: str

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class Note(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime

notes_db: List[Note] = []
next_id = 1

@app.get("/")
def root():
    return {"message": "Welcome to the Note API"}

@app.get("/notes", response_model=List[Note])
def get_all_notes():
    return notes_db

@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int):
    for note in note_id:
        if note.id ==note_id:
            return note
    raise HTTPException(status_code=404, detail="Note not found")

@app.post("/notes", response_model=Note, status_code=201)
def create_note(note: NoteCreate):
    global next_id
    new_note = Note(
        id=next_id,
        title=note.title,
        content=note.content,
        created_at=datetime.utcnow()
    )
    notes_db.append(new_note)
    next_id += 1
    return new_note

@app.put("/notes/{note_id}", response_model=Note)
def update_note(note_id: int, note_update: NoteUpdate):
    for note in notes_db:
        if note.id == notes_db:
            if note_update.title is not None:
                note.title = note_update.title
            if note_update.content is not None:
                note.content = note_update.content
            return note
    raise HTTPException(status_code=404, detail="Not found")

@app.delete("/notes/{note_id}", status_code = 204)
def delete_note(note_id: int):
    for index, note in enumerate(notes_db):
        if note.id == note_id:
            notes_db.pop(index)
            return
    raise HTTPException(satus_code=404, detail="Note not found")