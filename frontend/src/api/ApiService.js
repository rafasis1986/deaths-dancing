import axios from 'axios'

const BASE_API_URL = 'http://localhost:8000/v1/'

export const API = axios.create({
  baseURL: BASE_API_URL,
  headers: {
    Authorization: localStorage.getItem('access_token')
  }
  resolve(true)
})
