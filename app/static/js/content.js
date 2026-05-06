
document.addEventListener('DOMContentLoaded', function() {
  const contentId = '{{ content.unique_id|default:content.id }}';
  const contentType = '{{ content.content_type|default:"movie" }}';
  const userStatus = '{{ user_status|default:"not_seen" }}';
  
  // Inicializar estado del dropdown
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
  
  // Actualizar texto del status según el estado del usuario
  const statusText = document.getElementById('status-text');
  const statusIcon = document.getElementById('status-icon');
  if (statusText && userStatus) {
    statusText.textContent = statusLabels[userStatus] || 'Not Seen';
    statusIcon.textContent = statusIcons[userStatus] || 'visibility_off';
  }
  
  // Toggle dropdown de Status
  const statusBtn = document.getElementById('status-btn');
  const statusDropdown = document.getElementById('status-dropdown');
  
  if (statusBtn && statusDropdown) {
    statusBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      statusDropdown.classList.toggle('hidden');
    });
    
    // Cerrar dropdown al hacer click fuera
    document.addEventListener('click', function(e) {
      if (!statusBtn.contains(e.target) && !statusDropdown.contains(e.target)) {
        statusDropdown.classList.add('hidden');
      }
    });
    
    // Manejar cambio de estado
    const statusOptions = statusDropdown.querySelectorAll('button[data-status]');
    statusOptions.forEach(btn => {
      btn.addEventListener('click', function(e) {
        const status = this.dataset.status;
        updateStatus(status);
        statusDropdown.classList.add('hidden');
      });
    });
  }
  
  // Toggle Favorites
  const favoriteBtn = document.getElementById('favorite-btn');
  if (favoriteBtn) {
    favoriteBtn.addEventListener('click', function() {
      toggleFavorite();
    });
  }
  
  // Función para actualizar estado
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
  
  // Función para toggle favorite
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
  
  // Función para obtener CSRF token
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
});
