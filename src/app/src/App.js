import "./App.css";
import logo from "./logo.svg";
import { useEffect } from "react";

import useTodo from "./hooks/useTodo";

export function App() {
  const { createTodo, error, loading, todos, inputState, setInputState } =
    useTodo();

  const submitTodo = async (e) => {
    e.preventDefault();
    if (inputState === "") return;
    const data = {
      content: inputState,
    };
    await createTodo(data);
    setInputState("");
  };
  return (
    <div className="App">
      {loading ? (
        <p>Loading....</p>
      ) : (
        <div>
          <h1>List of TODOs</h1>
          <li>Learn Docker</li>
          <li>Learn React</li>
          {todos.map((todo) => {
            return <li key={todo._id.$oid}>{todo.content}</li>;
          })}
        </div>
      )}
      <div>
        <h1>Create a ToDo</h1>
        <form onSubmit={submitTodo}>
          <div>
            <label for="todo">ToDo: </label>
            <input
              type="text"
              value={inputState}
              onChange={(e) => setInputState(e.target.value)}
            />
          </div>
          <div style={{ marginTop: "5px" }}>
            <button type="submit">Add ToDos!</button>
          </div>
        </form>
      </div>
      <p style={{ color: "red" }}>{error}</p>
    </div>
  );
}

export default App;
