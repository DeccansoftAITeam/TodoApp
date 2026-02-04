/**
 * @fileoverview TodoItem component - Displays and manages individual todo items.
 * @module TodoItem
 */

import { useState } from 'react';

/**
 * TodoItem component - Renders a single todo item with edit, delete, and complete functionality.
 * Supports inline editing mode with save/cancel actions.
 * 
 * @param {Object} props - Component props
 * @param {Object} props.todo - The todo object to display
 * @param {number|string} props.todo.id - Unique identifier for the todo
 * @param {string} props.todo.title - Title of the todo
 * @param {string} [props.todo.description] - Optional description of the todo
 * @param {boolean} props.todo.is_completed - Completion status of the todo
 * @param {string} props.todo.created_at - ISO timestamp of when todo was created
 * @param {Function} props.onUpdate - Callback function to update the todo
 * @param {Function} props.onDelete - Callback function to delete the todo
 * @returns {JSX.Element} The todo item component
 */
function TodoItem({ todo, onUpdate, onDelete }) {
  const [isEditing, setIsEditing] = useState(false);
  const [title, setTitle] = useState(todo.title);
  const [description, setDescription] = useState(todo.description || '');

  /**
   * Toggles the completion status of the todo.
   * @returns {void}
   */
  const handleToggleComplete = () => {
    onUpdate(todo.id, { is_completed: !todo.is_completed });
  };

  /**
   * Enters edit mode for the todo item.
   * @returns {void}
   */
  const handleEdit = () => {
    setIsEditing(true);
  };

  /**
   * Saves the edited todo and exits edit mode.
   * @returns {void}
   */
  const handleSave = () => {
    onUpdate(todo.id, { title, description });
    setIsEditing(false);
  };

  /**
   * Cancels editing and reverts changes.
   * Resets local state to original todo values and exits edit mode.
   * @returns {void}
   */
  const handleCancel = () => {
    setTitle(todo.title);
    setDescription(todo.description || '');
    setIsEditing(false);
  };

  return (
    <div className="bg-white p-4 rounded-lg shadow-md mb-3">
      {isEditing ? (
        <div>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            className="w-full px-3 py-2 mb-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            className="w-full px-3 py-2 mb-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            rows="2"
          />
          <div className="flex gap-2">
            <button
              onClick={handleSave}
              className="px-4 py-1 bg-green-500 text-white rounded-md hover:bg-green-600"
            >
              Save
            </button>
            <button
              onClick={handleCancel}
              className="px-4 py-1 bg-gray-500 text-white rounded-md hover:bg-gray-600"
            >
              Cancel
            </button>
          </div>
        </div>
      ) : (
        <div>
          <div className="flex items-start gap-3">
            <input
              type="checkbox"
              checked={todo.is_completed}
              onChange={handleToggleComplete}
              className="mt-1 w-5 h-5 cursor-pointer"
            />
            <div className="flex-1">
              <h3 className={`text-lg font-semibold ${todo.is_completed ? 'line-through text-gray-500' : 'text-gray-800'}`}>
                {todo.title}
              </h3>
              {todo.description && (
                <p className={`text-sm mt-1 ${todo.is_completed ? 'line-through text-gray-400' : 'text-gray-600'}`}>
                  {todo.description}
                </p>
              )}
              <p className="text-xs text-gray-400 mt-2">
                {new Date(todo.created_at).toLocaleString()}
              </p>
            </div>
            <div className="flex gap-2">
              <button
                onClick={handleEdit}
                className="px-3 py-1 bg-blue-500 text-white text-sm rounded-md hover:bg-blue-600"
              >
                Edit
              </button>
              <button
                onClick={() => onDelete(todo.id)}
                className="px-3 py-1 bg-red-500 text-white text-sm rounded-md hover:bg-red-600"
              >
                Delete
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default TodoItem;
