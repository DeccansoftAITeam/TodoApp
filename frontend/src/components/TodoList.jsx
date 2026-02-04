import { useState, useEffect } from 'react';
import TodoForm from './TodoForm';
import TodoItem from './TodoItem';
import { fetchTodos, createTodo, updateTodo, deleteTodo } from '../services/api';

function TodoList() {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    loadTodos();
  }, []);

  const loadTodos = async () => {
    const data = await fetchTodos();
    setTodos(data);
  };

  const handleCreate = async (todoData) => {
    await createTodo(todoData);
    loadTodos();
  };

  const handleUpdate = async (id, todoData) => {
    await updateTodo(id, todoData);
    loadTodos();
  };

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
