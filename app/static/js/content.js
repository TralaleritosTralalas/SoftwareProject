
document.addEventListener('DOMContentLoaded', function() {
  const contentId = window.CONTENT_DATA.id;
  const contentType = window.CONTENT_DATA.type;
  const userStatus = window.CONTENT_DATA.userStatus;

  const statusLabels = {
    'not_seen': 'Not Seen',
    'watching': 'Watching',
    'completed': 'Completed'
  };
  const statusIcons = {
    'not_seen': 'visibility_off',
    'watching': 'play_circle',
    'completed': 'check_circle'
  };

  const statusText = document.getElementById('status-text');
  const statusIcon = document.getElementById('status-icon');
  if (statusText && userStatus) {
    statusText.textContent = statusLabels[userStatus] || 'Not Seen';
    statusIcon.textContent = statusIcons[userStatus] || 'visibility_off';
  }

  updateWatchlistButton();

  const statusBtn = document.getElementById('status-btn');
  const statusDropdown = document.getElementById('status-dropdown');

  if (statusBtn && statusDropdown) {
    statusBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      statusDropdown.classList.toggle('hidden');
    });

    document.addEventListener('click', function(e) {
      if (!statusBtn.contains(e.target) && !statusDropdown.contains(e.target)) {
        statusDropdown.classList.add('hidden');
      }
    });

    const statusOptions = statusDropdown.querySelectorAll('button[data-status]');
    statusOptions.forEach(btn => {
      btn.addEventListener('click', function(e) {
        const status = this.dataset.status;
        updateStatus(status);
        statusDropdown.classList.add('hidden');
      });
    });
  }

  const favoriteBtn = document.getElementById('favorite-btn');
  if (favoriteBtn) {
    favoriteBtn.addEventListener('click', function() {
      toggleFavorite();
    });
  }

  const watchlistBtn = document.getElementById('watchlist-btn');
  if (watchlistBtn) {
    watchlistBtn.addEventListener('click', function() {
      openWatchlistModal();
    });
  }

  function updateWatchlistButton() {
    const watchlistIcon = document.getElementById('watchlist-icon');
    const watchlistText = document.getElementById('watchlist-text');

    if (window.contentInLists && window.contentInLists.length > 0) {
      if (watchlistIcon) watchlistIcon.textContent = 'bookmark';
      if (watchlistText) watchlistText.textContent = 'In Watchlist';
    }
  }

  function updateStatus(status) {
    fetch(`/content/${contentType}/${contentId}/update-status/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')
      },
      body: JSON.stringify({ status: status })
    })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        const statusText = document.getElementById('status-text');
        const statusIcon = document.getElementById('status-icon');

        statusText.textContent = statusLabels[status] || 'Not Seen';
        statusIcon.textContent = statusIcons[status] || 'visibility_off';
      }
    })
    .catch(error => console.error('Error:', error));
  }

  function toggleFavorite() {
    fetch(`/content/${contentType}/${contentId}/toggle-favorite/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')
      }
    })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        const favoriteIcon = document.getElementById('favorite-icon');
        const favoriteText = document.getElementById('favorite-text');

        if (data.is_favorite) {
          favoriteIcon.textContent = 'favorite';
          favoriteText.textContent = 'Remove from Favorites';
        } else {
          favoriteIcon.textContent = 'favorite_border';
          favoriteText.textContent = 'Add to Favorites';
        }
      }
    })
.catch(error => console.error('Error:', error));
  }
});
