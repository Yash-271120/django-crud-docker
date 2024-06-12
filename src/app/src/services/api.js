import axios from "axios";

export const BASE_URL = "http://localhost:8000/api/";

const API = axios.create({
  baseURL: BASE_URL,
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
});

export default API;
