document.addEventListener('DOMContentLoaded', function() {
    loadUserLists();
    initRenameModal();
});

function loadUserLists() {
    fetch('/api/watchlist/lists/')
        .then(r => r.json())
        .then(data => {
            if (data.success) {
                window.userLists = data.lists;
                updateListsCount(data.lists.length);
            }
        })
        .catch(err => console.error('Error loading lists:', err));
}

function updateListsCount(count) {
    const statCards = document.querySelectorAll('.rounded-2xl.border.border-white\\/5.bg-surface-dark.p-5');
    statCards.forEach(card => {
        const title = card.querySelector('p.text-sm.text-text-secondary');
        if (title && title.textContent.includes('Lists')) {
            const valueEl = card.querySelector('h2.text-3xl');
            if (valueEl) {
                valueEl.textContent = count;
            }
        }
    });
}

function openCreateListModal() {
    openWatchlistModal();
}

function createList(name) {
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
            location.reload();
        } else {
            alert(data.error || 'Failed to create list');
        }
    })
    .catch(err => {
        console.error('Error:', err);
        alert('Failed to create list');
    });
}


function initRenameModal() {
    const modal = document.getElementById('rename-list-modal');
    if (!modal) return;

    const overlay = document.getElementById('rename-modal-overlay');
    const cancelBtn = document.getElementById('rename-cancel-btn');
    const form = document.getElementById('rename-list-form');

    overlay && overlay.addEventListener('click', closeRenameModal);
    cancelBtn && cancelBtn.addEventListener('click', closeRenameModal);

    form && form.addEventListener('submit', function(e) {
        e.preventDefault();
        const input = document.getElementById('rename-list-input');
        const listId = modal.dataset.listId;
        const newName = input.value.trim();
        if (newName && listId) {
            renameList(parseInt(listId), newName);
        }
    });
}

function openRenameListModal(listId, currentName) {
    const modal = document.getElementById('rename-list-modal');
    if (!modal) return;
    const input = document.getElementById('rename-list-input');
    const errorEl = document.getElementById('rename-list-error');

    modal.dataset.listId = listId;
    input.value = currentName;
    errorEl && (errorEl.textContent = '');
    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
    setTimeout(() => input.select(), 50);
}

function closeRenameModal() {
    const modal = document.getElementById('rename-list-modal');
    if (!modal) return;
    modal.classList.add('hidden');
    document.body.style.overflow = '';
}

document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closeRenameModal();
});

function renameList(listId, newName) {
    fetch(`/api/watchlist/lists/${listId}/rename/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ name: newName })
    })
    .then(r => r.json())
    .then(data => {
        if (data.success) {
            window.location.href = '/personal_library/';
        } else {
            const errorEl = document.getElementById('rename-list-error');
            if (errorEl) {
                errorEl.textContent = data.error || 'Failed to rename list';
            } else {
                alert(data.error || 'Failed to rename list');
            }
        }
    })
    .catch(err => {
        console.error('Error:', err);
        alert('Failed to rename list');
    });
}

function confirmDeleteList(listId) {
    if (confirm('Are you sure you want to delete this list?')) {
        deleteList(listId);
    }
}

function deleteList(listId) {
    fetch(`/api/watchlist/lists/${listId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
    .then(r => r.json())
    .then(data => {
        if (data.success) {
            window.location.href = '/personal_library/';
        } else {
            alert(data.error || 'Failed to delete list');
        }
    })
    .catch(err => {
        console.error('Error:', err);
        alert('Failed to delete list');
    });
}

function openListDetail(listId) {
    window.location.href = `/personal_library/list/${listId}/`;
}