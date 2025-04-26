import { fetchDistance } from '../utils/distanceAPI';
import React, { useState } from 'react';
import './distanceForm.css';

const CalcDistanceForm = () => {
    
    // set empty string of origin and destination
    const [origin, setOrigin] = useState('');
    const [destination, setDestination] = useState('');

    const [finalOrigin, setFinalOrigin] = useState('');
    const [finalDest, setFinalDest] = useState('');
    
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {

        // do not refresh page on form submission
        e.preventDefault();
        
        // clear existing error messages
        setError('');

        // set result to null
        setResult(null);

        const currOrigin = origin.trim();
        const currDest = destination.trim(); 

        if (currOrigin.toLowerCase() === currDest.toLowerCase()) {
            setError("Origin and Destination cannot be the same.");
            return;
        }
        
        // showing loader
        setLoading(true);

        try {

            // fetch data from backend
            const data = await fetchDistance(origin, destination);
            
            setFinalOrigin(currOrigin);
            setFinalDest(currDest);
            // set result value
            setResult(data);
        
        } catch (err) {
            // show the error
            setError(err.message);
        
        } finally {

            // stop screen loading
            setLoading(false);
        }
    };

    return (


        <div className="distance-form">
            
            <h1>Find Your Journey Distance</h1>

            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Enter origin"
                    value={origin}
                    onChange={(e) => setOrigin(e.target.value)}
                    required
                />
                <input
                    type="text"
                    placeholder="Enter destination"
                    value={destination}
                    onChange={(e) => setDestination(e.target.value)}
                    required
                />
                <button 
                    type="submit" 
                    disabled={loading}
                    style={{
                        backgroundColor: loading ? '#aaa' : '#007bff', // gray if loading, blue otherwise
                        color: 'white',
                        padding: '10px 20px',
                        border: 'none',
                        borderRadius: '5px',
                        cursor: loading ? 'not-allowed' : 'pointer'
                    }}>
                    {loading ? 'Loading...' : 'Calculate Distance'}
                </button>
            </form>

            {/* {loading && <p>Loading...</p>} */}
            {error && <p style={{ color: "red" }}>{error}</p>}

            {result && (
                <div className="result">
                    <h3>Journey details:</h3>
                
                    <p><strong>Original Origin:</strong> {finalOrigin}</p>
                    <p><strong title="More accurate and complete address">Complete Address:</strong> {result.origin}</p>
                
                    <p><strong>Original Destination:</strong> {finalDest}</p>
                    <p><strong title="More accurate and complete address">Complate Address:</strong> {result.destination}</p>
                
                    <p><strong>Distance:</strong> {result.distance_km} km</p>
                </div>
            )}
        </div>
    );
};

export default CalcDistanceForm;
