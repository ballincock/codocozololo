            let actP = null,
                actParent = null;

            function move(dir) {
                const v = document.getElementById('viewport');
                v.scrollBy({
                    left: v.clientWidth * dir,
                    behavior: 'smooth'
                });
            }
            async function vote(id, type, val) {
                await fetch('/api/vote', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        id,
                        type,
                        vote: val
                    })
                });
                location.reload();
            }
            async function openComments(pid) {
                actP = pid;
                document.getElementById('c-drawer').style.display = 'flex';
                const res = await fetch(`/api/comments/${pid}`);
                const data = await res.json();
                const build = (l) => l.map(c => `<div style="border-left:2px solid #ddd; padding-left:10px; margin-top:8px; font-size:13px;">
                <strong>@${c.username}</strong>: ${c.content} <span style="color:green; cursor:pointer;" onclick="actParent=${c.id}">Reply</span>
                ${c.replies.length ? build(c.replies) : ''}</div>`).join('');
                document.getElementById('c-list').innerHTML = data.length ? build(data) : 'No comments.';
            }
            async function sendComment() {
                await fetch('/api/post_comment', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        post_id: actP,
                        parent_id: actParent,
                        content: document.getElementById('c-input').value
                    })
                });
                document.getElementById('c-input').value = '';
                actParent = null;
                openComments(actP);
            }
