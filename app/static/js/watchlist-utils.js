// Watchlist Utilities - Funciones compartidas
// Usado por watchlist.js, watchlist-modal.js, content.js

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function watchlistApiUrl(name, placeholderValue) {
    if (window.API_URLS && window.API_URLS[name]) {
        const url = window.API_URLS[name];
        return placeholderValue !== undefined ? url.replace('99999', placeholderValue) : url;
    }
    const prefix = window.LANG_PREFIX ? `/${window.LANG_PREFIX}` : '';
    const urls = {
        getLists: `${prefix}/api/watchlist/lists/`,
        createList: `${prefix}/api/watchlist/lists/create/`,
    };
    const url = urls[name];
    return placeholderValue !== undefined ? url.replace('99999', placeholderValue) : url;
}