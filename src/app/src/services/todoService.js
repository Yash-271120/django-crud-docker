import API from "./api";

const TodoService = {
    async getAll() {
        const response = await API.get("todos/");
        return response.data.data;
    },
    async create(data) {
        const response = await API.post("todos/", data);
        return response.data.data;
    },

    async update(id, data) {
        const response = await API.put(`todos/${id}/`, data);
        return response.data.data;
    },
    async delete(id) {
        const response = await API.delete(`todos/${id}/`);
        return response.data.data;
    },
    async get(id) {
        const response = await API.get(`todos/${id}/`);
        return response.data.data;
    }
}

export {TodoService};