import { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);

  // fetch users
  const fetchUsers = async () => {
    setLoading(true);
    try {
      const res = await axios.get("http://127.0.0.1:8000/users");
      setUsers(res.data);
    } catch (err) {
      console.error("Error fetching users:", err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  // delete user
  const handleDelete = async (id) => {
    try {
      await axios.delete(`http://127.0.0.1:8000/users/${id}`);
      setUsers(users.filter(u => u.id !== id)); // remove from state
    } catch (err) {
      console.error("Delete failed:", err);
    }
  };
  const deleteTable = async () => {
  try {
    await axios.delete("http://127.0.0.1:8000/users");
    setUsers([]); // clear UI instantly
  } catch (err) {
    console.error("Delete failed:", err);
  }
};

  if (loading) return <p>Loading users...</p>;

  return (
    <div style={{ padding: "20px" }}>
      <h2>Users</h2>
      <ul>
        {users.map(u => (
          <li key={u.id} style={{ marginBottom: "8px" }}>
            {u.email}{" "}
            <button 
              onClick={() => handleDelete(u.id)} 
              style={{ marginLeft: "10px" }}
            >
              Delete
            </button>
          </li>
        ))}
        <button 
              onClick={() => deleteTable()} 
              style={{ marginLeft: "10px" }}
            >
              Truncate table
            </button>
      </ul>
    </div>
  );
}

export default App;
