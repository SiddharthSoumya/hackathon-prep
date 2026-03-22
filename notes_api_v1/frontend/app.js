const API = "http://127.0.0.1:8000"

// ── Load all notes when page opens ──────────────────────
async function loadNotes() {
    const response = await fetch(`${API}/notes`)
    const notes = await response.json()

    document.getElementById("noteCount").textContent = `(${notes.length})`
    renderNotes(notes)
}

// ── Render notes to page ────────────────────────────────
function renderNotes(notes) {
    const grid = document.getElementById("notesGrid")

    if (notes.length === 0) {
        grid.innerHTML = `<div class="empty-state">No notes yet. Create one above! ☝️</div>`
        return
    }

    grid.innerHTML = notes.map(note => `
        <div class="note-card">
            <div>
                <p class="note-title">${note.title}</p>
                <p class="note-content">${note.content}</p>
                ${note.tag ? `<span class="note-tag">${note.tag}</span>` : ""}
                <p class="note-meta">${note.created_at}</p>
            </div>
            <button class="btn btn-danger" onclick="deleteNote('${note.id}')">
                Delete
            </button>
        </div>
    `).join("")
}

// ── Create a note ───────────────────────────────────────
document.getElementById("noteForm").addEventListener("submit", async function(e) {
    e.preventDefault()   // stop page reload

    const title   = document.getElementById("title").value.trim()
    const content = document.getElementById("content").value.trim()
    const tag     = document.getElementById("tag").value.trim()

    // Frontend validation
    if (!title) {
        showError("Title cannot be empty!")
        return
    }

    const response = await fetch(`${API}/notes`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, content, tag: tag || null })
    })

    if (response.ok) {
        hideError()
        document.getElementById("noteForm").reset()  // clear form
        loadNotes()   // refresh the list
    } else {
        const err = await response.json()
        showError("Error: " + JSON.stringify(err.detail))
    }
})

// ── Delete a note ───────────────────────────────────────
async function deleteNote(id) {
    const response = await fetch(`${API}/notes/${id}`, {
        method: "DELETE"
    })
    if (response.ok) loadNotes()
}

// ── Error helpers ───────────────────────────────────────
function showError(msg) {
    const box = document.getElementById("errorBox")
    document.getElementById("errorText").textContent = msg
    box.style.display = "block"
}

function hideError() {
    document.getElementById("errorBox").style.display = "none"
}

// ── Run on page load ────────────────────────────────────
loadNotes()