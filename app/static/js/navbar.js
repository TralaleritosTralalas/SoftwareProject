function getCookie(name) {
    let value = "; " + document.cookie;
    let parts = value.split("; " + name + "=");
    if (parts.length === 2) return parts.pop().split(";").shift();
}

function updateBadge(count) {
    const badge = document.getElementById('notif-badge');
    if (count > 0) {
        if (badge) {
            badge.textContent = count;
        }
    } else {
        if (badge) badge.remove();
    }
}

function markNotificationSeen(notificationId, itemEl) {
    fetch('/api/notifications/mark-seen/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({id: notificationId})
    })
    .then(r => r.json())
    .then(data => {
        itemEl.style.transition = 'all 0.25s ease-out';
        itemEl.style.opacity = '0';
        itemEl.style.transform = 'translateX(20px)';
        setTimeout(() => {
            itemEl.remove();
            const list = document.getElementById('notif-list');
            if (list && !list.querySelector('.notif-item')) {
                list.innerHTML = `
                    <div class="p-8 text-center flex flex-col items-center gap-2">
                        <span class="material-symbols-outlined text-3xl text-green-500">check_circle</span>
                        <p class="text-sm text-slate-400">There are no notifications</p>
                        <p class="text-xs text-slate-500">You'll be up to date when there are new updates.</p>
                    </div>
                `;
                const markBtn = document.getElementById('mark-all-seen');
                if (markBtn) markBtn.remove();
            }
            updateBadge(data.count);
        }, 250);
    });
}

function markAllNotificationsSeen() {
    fetch('/api/notifications/mark-seen/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({all: true})
    })
    .then(r => r.json())
    .then(data => {
        const list = document.getElementById('notif-list');
        if (list) {
            list.innerHTML = `
                <div class="p-8 text-center flex flex-col items-center gap-2">
                    <span class="material-symbols-outlined text-3xl text-green-500">check_circle</span>
                    <p class="text-sm text-slate-400">There are no notifications</p>
                    <p class="text-xs text-slate-500">You'll be up to date when there are new updates.</p>
                </div>
            `;
        }
        const markBtn = document.getElementById('mark-all-seen');
        if (markBtn) markBtn.remove();
        updateBadge(data.count);
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const mobileMenuBtn = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });
    }

    const userMenuBtn = document.getElementById('user-menu-button');
    const userDropdown = document.getElementById('user-dropdown');

    if (userMenuBtn && userDropdown) {
        userMenuBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            userDropdown.classList.toggle('hidden');
        });
    }

    // Notification dropdown toggle
    const notifBtn = document.getElementById('notif-button');
    const notifDropdown = document.getElementById('notif-dropdown');

    if (notifBtn && notifDropdown) {
        notifBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            notifDropdown.classList.toggle('hidden');
        });
    }

    // Notification individual click → mark as seen
    document.querySelectorAll('.notif-item').forEach(item => {
        item.addEventListener('click', function () {
            const id = this.dataset.id;
            if (id) markNotificationSeen(id, this);
        });
    });

    // Mark all as seen
    const markAllBtn = document.getElementById('mark-all-seen');
    if (markAllBtn) {
        markAllBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            markAllNotificationsSeen();
        });
    }

    // Cerrar al hacer click fuera del botón correspondiente
    document.addEventListener('click', (e) => {
        if (userDropdown && !userMenuBtn?.contains(e.target)) {
            userDropdown.classList.add('hidden');
        }
        if (notifDropdown && !notifBtn?.contains(e.target)) {
            notifDropdown.classList.add('hidden');
        }
    });
});