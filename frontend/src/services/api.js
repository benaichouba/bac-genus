const API_BASE = (import.meta.env.VITE_API_URL || 'http://localhost:8000/api').replace(/\/$/, '')

export async function fetchJson(path) {
  const res = await fetch(`${API_BASE}${path}`)
  if (!res.ok) throw new Error('Request failed')
  return res.json()
}

export async function uploadFile(file, title) {
  const formData = new FormData()
  formData.append('file', file)
  formData.append('title', title)

  const res = await fetch(`${API_BASE}/admin/upload`, {
    method: 'POST',
    body: formData,
  })

  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: 'Upload failed' }))
    throw new Error(err.detail || 'Upload failed')
  }

  return res.json()
}

export async function fetchLessons() {
  return fetchJson('/lessons')
}

export async function fetchLesson(id) {
  return fetchJson(`/lessons/${id}`)
}

export async function fetchExercises(lessonId, level = 'beginner') {
  return fetchJson(`/exercises?lesson_id=${lessonId}&level=${level}`)
}

export async function fetchAnalysis() {
  return fetchJson('/analysis')
}

export async function fetchPredictions() {
  return fetchJson('/predictions')
}
