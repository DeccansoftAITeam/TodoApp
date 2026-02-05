import axios from 'axios';

//const remoteUrl = import.meta.env.VITE_API_URL || 'https://dsstodoapp.azurewebsites.net/api/todos/';

const API_URL = localStorage.getItem("URL")+ '/api/todos/';

function authHeaders() {
  const token = localStorage.getItem('token');
  return token ? { Authorization: `Bearer ${token}` } : {};
}

export const fetchTodos = async () => {
  const response = await axios.get(API_URL, { headers: authHeaders() });
  return response.data;
};

export const createTodo = async (todoData) => {
  const response = await axios.post(API_URL, todoData, { headers: authHeaders() });
  return response.data;
};

export const updateTodo = async (id, todoData) => {
  const response = await axios.put(`${API_URL}/${id}`, todoData, { headers: authHeaders() });
  return response.data;
};

export const deleteTodo = async (id) => {
  const response = await axios.delete(`${API_URL}/${id}`, { headers: authHeaders() });
  return response.data;
};
