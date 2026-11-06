import { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("Loading...");

  useEffect(() => {
    fetch("http://localhost:8000/api/hello")
      .then((response) => response.json())
      .then((data) => setMessage(data.message))
      .catch(() => setMessage("Failed to connect to backend"));
  }, []);

  return (
    <div>
      <h1>TherapistFlow</h1>
      <p>{message}</p>
    </div>
  );
}

export default App;