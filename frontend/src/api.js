const API_BASE = (typeof import.meta !== 'undefined' && import.meta.env && import.meta.env.VITE_API_BASE) || 'http://localhost:8000'

async function request(path, options = {}) {
	const res = await fetch(`${API_BASE}${path}`, {
		headers: { 'Content-Type': 'application/json' },
		...options,
	})

	const text = await res.text()
	let data = null
	try {
		data = text ? JSON.parse(text) : null
	} catch (err) {
		throw new Error('Invalid JSON response from API')
	}

	if (!res.ok) {
		const errMsg = (data && (data.detail || data.error)) || res.statusText || 'API error'
		throw new Error(errMsg)
	}

	return data
}

export async function startGame() {
	return request('/start', { method: 'POST' })
}

export async function sendAction(session_id, action) {
	return request('/action', {
		method: 'POST',
		body: JSON.stringify({ session_id, action }),
	})
}

export async function health() {
	return request('/')
}

export default { startGame, sendAction, health }

