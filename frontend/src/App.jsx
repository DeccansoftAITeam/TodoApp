import { useState, useEffect } from 'react'
import TodoList from './components/TodoList'
import Login from './components/Login'
import './App.css'

function App() {
  const [token, setToken] = useState(null)

  useEffect(() => {
    const t = localStorage.getItem('token')
    setToken(t)
  }, [])

  const handleLogin = () => {
    const t = localStorage.getItem('token')
    setToken(t)
  }

  if (!token) {
    //Not Authorized
    return <Login onLogin={handleLogin} />
  }
  //Authorized
  return (<TodoList />)
}

export default App
