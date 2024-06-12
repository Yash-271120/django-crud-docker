import { createContext, useState } from "react";

const defaultValues = {
  todos: [],
  setTodos: () => {},
  inputState: "",
  setInputState: () => {},
  loading: false,
  setLoading: () => {},
  error: null,
  setError: () => {},
};

export const TodoContext = createContext(defaultValues);

export const TodoProvider = ({ children }) => {
  const [todos, setTodos] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [inputState, setInputState] = useState("");

  return (
    <TodoContext.Provider
      value={{
        todos,
        setTodos,
        loading,
        setLoading,
        error,
        setError,
        inputState,
        setInputState,
      }}
    >
      {children}
    </TodoContext.Provider>
  );
};
