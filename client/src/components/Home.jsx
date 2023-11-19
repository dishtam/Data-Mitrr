import React, { useState } from 'react';
import '../style/home.css';
import axios from 'axios';

const BACKEND_URL = ''; // Add your backend URL here

const Home = () => {
  const [url, setUrl] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const info = { url: url };

    try {
      const response = await axios.post(BACKEND_URL, info);

      if (response.data.success) {
        console.log('URL Sent Successfully');
      } else {
        console.log('Error');
      }
    } catch (error) {
      console.log('Error:', error);
    }
  };

  return (
    <div>
      <div className="container">
        <div className="child">
          <form onSubmit={handleSubmit}>
            <input
              type="text"
              name="url"
              id="url"
              value={url}
              placeholder="Enter the URL here"
              onChange={(e) => setUrl(e.target.value)}
            />
            <button type="submit">Click to Proceed</button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Home;
