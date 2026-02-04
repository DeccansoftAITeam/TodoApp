/**
 * @fileoverview TodoList component - Main container for managing and displaying todos.
 * @module TodoList
 */

import { useState, useEffect } from 'react';
import TodoForm from './TodoForm';
import TodoItem from './TodoItem';
import { fetchTodos, createTodo, updateTodo, deleteTodo } from '../services/api';

/**
 * TodoList component - Manages the list of todos and handles CRUD operations.
 * This component fetches todos from the API, manages local state, and coordinates
 * interactions between TodoForm and TodoItem components.
 * 
 * @returns {JSX.Element} The todo list container with form and items
 */
function TodoList() {
  const [todos, setTodos] = useState([]);

  /**
   * Loads todos from the API and updates state.
   * @async
   * @returns {Promise<void>}
   */
  const loadTodos = async () => {
    const data = await fetchTodos();
    setTodos(data);
  };

  // Load todos on component mount
  useEffect(() => {
    const initializeTodos = async () => {
      const data = await fetchTodos();
      setTodos(data);
    };
    initializeTodos();
  }, []);

  /**
   * Handles creation of a new todo.
   * @async
   * @param {Object} todoData - The todo data to create
   * @param {string} todoData.title - The title of the todo
   * @param {string} [todoData.description] - The description of the todo
   * @returns {Promise<void>}
   */
  const handleCreate = async (todoData) => {
    await createTodo(todoData);
    loadTodos();
  };

  /**
   * Handles updating an existing todo.
   * @async
   * @param {number|string} id - The ID of the todo to update
   * @param {Object} todoData - The updated todo data
   * @returns {Promise<void>}
   */
  const handleUpdate = async (id, todoData) => {
    await updateTodo(id, todoData);
    loadTodos();
  };

  /**
   * Handles deletion of a todo.
   * @async
   * @param {number|string} id - The ID of the todo to delete
   * @returns {Promise<void>}
   */
  const handleDelete = async (id) => {
    await deleteTodo(id);
    loadTodos();
  };

  return (
    <div className="min-h-screen bg-gray-100 py-8 px-4">
      <div className="max-w-2xl mx-auto">
        <h1 className="text-4xl font-bold text-gray-800 mb-8 text-center">Todo App</h1>
        <TodoForm onSubmit={handleCreate} />
        <div>
          {todos.map((todo) => (
            <TodoItem
              key={todo.id}
              todo={todo}
              onUpdate={handleUpdate}
              onDelete={handleDelete}
            />
          ))}
        </div>
      </div>
    </div>
  );
}

export default TodoList;
