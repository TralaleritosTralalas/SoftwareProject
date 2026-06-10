function openWatchlistModal() {
    const modal = document.getElementById('watchlist-modal');
    if (!modal) return;

    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
    loadWatchlistLists();
}

function closeWatchlistModal() {
    const modal = document.getElementById('watchlist-modal');
    if (!modal) return;

    modal.classList.add('hidden');
    document.body.style.overflow = '';
    hideCreateListInput();
}


function showCreateListInput() {
    const btn = document.getElementById('create-list-btn');
    const form = document.getElementById('create-list-form');
    const input = document.getElementById('new-list-name');

    if (!btn || !form || !input) return;

    btn.classList.add('hidden');
    form.classList.remove('hidden');
    input.focus();
}

function hideCreateListInput() {
    const btn = document.getElementById('create-list-btn');
    const form = document.getElementById('create-list-form');
    const input = document.getElementById('new-list-name');

    if (!btn || !form || !input) return;

    btn.classList.remove('hidden');
    form.classList.add('hidden');
    input.value = '';
}


function loadWatchlistLists() {
    const container = document.getElementById('watchlist-lists');
    if (!container) return;

    container.innerHTML = `
        <div class="text-center py-8 text-text-secondary">
            <span class="material-symbols-outlined text-4xl mb-2 animate-spin">progress_activity</span>
            <p>Loading...</p>
        </div>
    `;

    fetch('/api/watchlist/lists/')
        .then(r => r.json())
        .then(data => {
            if (data.success && data.lists.length > 0) {
                container.innerHTML = data.lists.map(list => `
                    <button onclick="toggleListContent(${list.id}, this)" 
                        class="w-full flex items-center gap-3 px-4 py-3 rounded-xl bg-surface-highlight hover:bg-white/5 border border-transparent hover:border-white/10 transition-all group ${isContentInList(list.id) ? 'border-blue-500/50' : ''}"
                        data-list-id="${list.id}">
                        <span class="material-symbols-outlined text-text-secondary group-hover:text-blue-400 transition-colors ${isContentInList(list.id) ? 'text-blue-400' : ''}">
                            ${isContentInList(list.id) ? 'check_box' : 'check_box_outline_blank'}
                        </span>
                        <div class="flex-1 text-left">
                            <p class="text-white font-semibold">${escapeHtml(list.name)}</p>
                            <p class="text-text-secondary text-sm">${list.item_count} items</p>
                        </div>
                    </button>
                `).join('');
            } else {
                container.innerHTML = `
                    <div class="text-center py-8 text-text-secondary">
                        <span class="material-symbols-outlined text-4xl mb-2">playlist_add</span>
                        <p class="mb-4">No lists yet</p>
                        <p class="text-sm">Create your first list above!</p>
                    </div>
                `;
            }
        })
        .catch(() => {
            container.innerHTML = `
                <div class="text-center py-8 text-text-secondary">
                    <span class="material-symbols-outlined text-4xl mb-2 text-red-400">error</span>
                    <p>Failed to load lists</p>
                </div>
            `;
        });
}


function isContentInList(listId) {
    return window.contentInLists && window.contentInLists.includes(listId);
}


function showToast(message, type = 'success') {
    const toast = document.getElementById('watchlist-toast');
    const msgEl = document.getElementById('toast-message');
    const iconEl = document.getElementById('toast-icon');
    if (!toast || !msgEl || !iconEl) return;

    msgEl.textContent = message;
    toast.classList.remove('hidden');

    if (type === 'remove') {
        toast.classList.remove('bg-emerald-500');
        toast.classList.add('bg-red-500');
        iconEl.textContent = 'remove_circle';
    } else {
        toast.classList.remove('bg-red-500');
        toast.classList.add('bg-emerald-500');
        iconEl.textContent = 'check_circle';
    }

    toast.style.animation = 'slideDown 0.3s ease';

    setTimeout(() => {
        toast.classList.add('hidden');
    }, 2500);
}


function toggleListContent(listId, btnElement) {
    const contentType = window.CONTENT_DATA ? window.CONTENT_DATA.type : null;
    const contentId = window.CONTENT_DATA ? window.CONTENT_DATA.id : null;
    const isInList = isContentInList(listId);
    const icon = btnElement.querySelector('.material-symbols-outlined');
    const nameEl = btnElement.querySelector('.text-white.font-semibold');
    const listName = nameEl ? nameEl.textContent : 'list';

    if (!contentType || !contentId) {
        showToast('Cannot add - no content selected');
        return;
    }

    const url = isInList
        ? `/content/${contentType}/${contentId}/remove-from-list/${listId}/`
        : `/content/${contentType}/${contentId}/add-to-list/${listId}/`;

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ ctype: contentType, cid: contentId })
    })
    .then(r => r.json())
    .then(data => {
        if (data.success) {
            if (isInList) {
                window.contentInLists = window.contentInLists.filter(id => id !== listId);
                icon.textContent = 'check_box_outline_blank';
                icon.classList.remove('text-blue-400');
                btnElement.classList.remove('border-blue-500/50');
                showToast(`Removed from "${listName}"`, 'remove');
            } else {
                window.contentInLists.push(listId);
                icon.textContent = 'check_box';
                icon.classList.add('text-blue-400');
                btnElement.classList.add('border-blue-500/50');
                showToast(`Added to "${listName}"`);
            }
        } else {
            showToast(data.error || 'Something went wrong');
        }
    })
    .catch(err => {
        console.error('Error:', err);
        showToast('Connection error');
    });
}


function createNewList() {
    const input = document.getElementById('new-list-name');
    if (!input) return;

    const name = input.value.trim();

    if (!name) {
        input.focus();
        return;
    }

    fetch('/api/watchlist/lists/create/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ name })
    })
    .then(r => r.json())
    .then(data => {
        if (data.success) {
            hideCreateListInput();
            showToast(`List "${name}" created!`);

            if (window.CONTENT_DATA && window.CONTENT_DATA.type && window.CONTENT_DATA.id) {
                const contentType = window.CONTENT_DATA.type;
                const contentId = window.CONTENT_DATA.id;

                fetch(`/content/${contentType}/${contentId}/add-to-list/${data.list.id}/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    body: JSON.stringify({ ctype: contentType, cid: contentId })
                })
                .then(r => r.json())
                .then(() => {
                    window.contentInLists.push(data.list.id);
                    loadWatchlistLists();
                });
            } else {
                loadWatchlistLists();
            }
        } else {
            showToast(data.error || 'Failed to create list');
        }
    })
    .catch(err => {
        console.error('Error:', err);
        showToast('Connection error');
    });
}