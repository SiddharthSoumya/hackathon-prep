from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
from typing import Optional
import uuid
from datetime import datetime

app = FastAPI(title="Notes API", version="1.0")

# ── In-memory storage (Day 9 we replace with real DB) ──
notes_db = []

# ── Pydantic Models ─────────────────────────────────────

class NoteCreate(BaseModel):
    """What the USER sends when creating a note"""
    title: str
    content: str
    tag: Optional[str] = None  # optional field

    # Custom validator — title can't be empty or just spaces
    @field_validator("title")
    def title_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError("Title cannot be empty or whitespace")
        if len(v) > 100:
            raise ValueError("Title too long — max 100 characters")
        return v.strip()  # also strips whitespace automatically

class NoteResponse(BaseModel):
    """What WE send back — includes server-generated fields"""
    id: str
    title: str
    content: str
    tag: Optional[str]
    created_at: str

# ── Routes ──────────────────────────────────────────────

@app.get("/")
def root():
    return {"message": "Notes API is running", "total_notes": len(notes_db)}

@app.post("/notes", response_model=NoteResponse, status_code=201)
def create_note(note: NoteCreate):
    new_note = {
        "id": str(uuid.uuid4())[:8],   # short unique id e.g. "a3f9b2c1"
        "title": note.title,
        "content": note.content,
        "tag": note.tag,
        "created_at": datetime.now().isoformat()
    }
    notes_db.append(new_note)
    return new_note

@app.get("/notes", response_model=list[NoteResponse])
def get_all_notes():
    return notes_db

@app.get("/notes/{note_id}", response_model=NoteResponse)
def get_note(note_id: str):
    for note in notes_db:
        if note["id"] == note_id:
            return note
    # If we reach here, note wasn't found
    raise HTTPException(status_code=404, detail=f"Note '{note_id}' not found")

@app.delete("/notes/{note_id}")
def delete_note(note_id: str):
    for i, note in enumerate(notes_db):
        if note["id"] == note_id:
            deleted = notes_db.pop(i)
            return {"message": "Deleted successfully", "note": deleted}
    raise HTTPException(status_code=404, detail=f"Note '{note_id}' not found")

@app.put("/notes/{note_id}", response_model=NoteResponse)
def update_note(note_id: str, updated: NoteCreate):
    for note in notes_db:
        if note["id"] == note_id:
            note["title"] = updated.title
            note["content"] = updated.content
            note["tag"] = updated.tag
            return note
    raise HTTPException(status_code=404, detail=f"Note '{note_id}' not found")