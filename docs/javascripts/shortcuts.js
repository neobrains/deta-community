keyboard$.subscribe(function(key) {
  if (key.mode === "global" && key.type === "S") {
    if (key.key === "S") {
        // Open search
        document.getElementById("search-input").focus();
    }
    key.claim()
  }
})