export const UPDATE_USER = (state, user) => {
  state.user = user
}

/**
 * Clear each property, one by one, so reactivity still works.
 */
export const CLEAR_ALL_DATA = (state) => {
  // User
  state.user.name = ''
  state.user.id = null
  state.user.picture = null
  state.user.email = ''
}
