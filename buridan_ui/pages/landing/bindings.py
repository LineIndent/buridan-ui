from typing import Callable


key_bindings: Callable[[], str] = (
    lambda: """
document.addEventListener('keydown', function(event) {
  // Check for a specific key, e.g., 'G' key (case-insensitive)
  if (event.key === 'c' || event.key === 'C') {
    window.location.href = 'https://github.com/LineIndent/buridan-ui'; // Redirect to your desired URL
  }
  if (event.key === 'x' || event.key === 'X') {
    window.location.href = 'https://github.com/reflex-dev/reflex'; // Redirect to your desired URL
  }
});
"""
)
