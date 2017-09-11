export const UPDATE_USER = (state, user) => {
  state.user = user
}

export const UPDATE_AUTH_HEADER = (state, authHeader) => {
  state.auth_header = authHeader
}

/**
 * Clear each property, one by one, so reactivity still works.
 */
export const CLEAR_ALL_DATA = (state) => {
  // User
  state.user.name = null
  state.user.id = null
  state.user.picture = null
  state.user.email = null

  // AUTH_HEADER
  state.auth_header = {
    token: null,
    expires_at: null
  }
}
