import React, { useState, useEffect } from 'react';  // Import useState and useEffect
import axios from 'axios';  // Import axios for making API calls
import { Header } from "./Header";
import { Navbar } from "./Navbar";
import { Main } from "./Main";

function App() {
  // Declare a state variable to store the message
  const [message, setMessage] = useState('');

  // Use the useEffect hook to make the API call when the component mounts
  useEffect(() => {
    axios.get('/api/').then((response) => {
      setMessage(response.data.Hello);
    });
  }, []);

  return (
    <div className="container-fluid">
      <Header title_text="My Title Text 1" />
      <div className="row mt-5">
        <div className="col-md-3">
          <Navbar />
        </div>
        <div className="col-md-9">
          <Main />
          {/* Display the message received from the API */}
          <p>Message from API: {message}</p>
        </div>
      </div>
    </div>
  );
}

export default App;
