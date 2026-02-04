/**
 * @fileoverview Main App component that serves as the root of the React application.
 * @module App
 */

import TodoList from './components/TodoList'
import './App.css'

/**
 * App component - Root component of the Todo application.
 * Renders the TodoList component which contains all todo functionality.
 * 
 * @returns {JSX.Element} The main application component
 */
function App() {
  return <TodoList />
}

export default App
