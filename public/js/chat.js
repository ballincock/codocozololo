async function send(e) {
    e.preventDefault();
    const val = document.getElementById('mText').value;
    await fetch('/api/send', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            receiver: "{{ receiver }}",
            content: val
        })
    });
    location.reload();
}
async function deleteMsg(id) {
    if (!confirm("Delete?")) return;
    await fetch('/api/delete', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            id: id
        })
    });
    location.reload();
}
async function doSearch() {
    const q = document.getElementById('sInput').value.trim();
    const iv = document.getElementById('inboxView');
    const sv = document.getElementById('searchView');

    if (q.length < 1) {
        iv.style.display = 'block';
        sv.style.display = 'none';
        return;
    }

    try {
        const res = await fetch(`/api/search_users?q=${encodeURIComponent(q)}`);
        const users = await res.json();

        iv.style.display = 'none';
        sv.style.display = 'block';

        if (users.length === 0) {
            sv.innerHTML = '<p style="padding: 20px; color: #555; font-size: 0.9rem;">No users found.</p>';
        } else {
            sv.innerHTML = users.map(u => `
                <a href="/chat/${u}" class="contact">
                    <span>🔍 ${u}</span>
                </a>
            `).join('');
        }
    } catch (err) {
        console.error("Search failed:", err);
    }
}

const b = document.getElementById('chatBox');
b.scrollTop = b.scrollHeight;
