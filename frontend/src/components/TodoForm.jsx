/**
 * @fileoverview TodoForm component - Form for creating new todos.
 * @module TodoForm
 */

import { useState } from 'react';

/**
 * TodoForm component - Provides a form interface for creating new todos.
 * Manages form state and validation before submitting to parent component.
 * 
 * @param {Object} props - Component props
 * @param {Function} props.onSubmit - Callback function called when form is submitted
 * @returns {JSX.Element} The todo creation form
 */
function TodoForm({ onSubmit }) {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');

  /**
   * Handles form submission.
   * Validates that title is not empty before calling onSubmit callback.
   * Clears form fields after successful submission.
   * 
   * @param {React.FormEvent<HTMLFormElement>} e - The form event
   * @returns {void}
   */
  const handleSubmit = (e) => {
    e.preventDefault();
    if (title.trim()) {
      onSubmit({ title, description });
      setTitle('');
      setDescription('');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="mb-6 bg-white p-6 rounded-lg shadow-md">
      <div className="mb-4">
        <input
          type="text"
          placeholder="Todo title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
      </div>
      <div className="mb-4">
        <textarea
          placeholder="Description (optional)"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          rows="3"
        />
      </div>
      <button
        type="submit"
        className="w-full bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600 transition-colors"
      >
        Add Todo
      </button>
    </form>
  );
}

export default TodoForm;
