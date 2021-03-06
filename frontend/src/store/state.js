// Set the key we'll use in local storage.
// Go to Chrome dev tools, application tab, click "Local Storage" and "http://localhost:8080"
// and you'll see this key set below (if logged in):
export const STORAGE_KEY = 'death-client'

let syncedData = {
  user: {
    name: null,
    email: null,
    picture: null,
    id: null
  },
  auth_header: {
    token: null,
    expires_at: null
  }
}

// Sync with local storage.
if (localStorage.getItem(STORAGE_KEY)) {
  syncedData = JSON.parse(localStorage.getItem(STORAGE_KEY))
}

// Merge data and export it.
export const state = Object.assign(syncedData)
