import { useContext, useEffect } from "react";

import { TodoContext } from "../contexts/todoContext";
import { TodoService } from "../services/todoService";

const useTodo = () => {
  const {
    todos,
    setTodos,
    loading,
    setLoading,
    error,
    setError,
    inputState,
    setInputState,
  } = useContext(TodoContext);

  const getAllTodos = async () => {
    setLoading(true);
    try {
      const data = await TodoService.getAll();
      setTodos(data);
    } catch (error) {
      setError("Error fetching todos");
    } finally {
      setLoading(false);
    }
  };

  const createTodo = async (data) => {
    setLoading(true);
    try {
      const response = await TodoService.create(data);
      await getAllTodos();
    } catch (error) {
      setError("Error creating todo");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    getAllTodos();
  }, []);

  return {
    todos,
    loading,
    error,
    createTodo,
    inputState,
    setInputState,
    getAllTodos,
  };
};

export default useTodo;
