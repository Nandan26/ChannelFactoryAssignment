import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/api'; // for backend running locally

export const fetchDistance = async (origin, destination) => {
    try {

        const response = await axios.post(`${API_BASE_URL}/calc/distance/`, {
            origin,
            destination
        });

        return response.data;
    
    } catch (error) {

        if (error.response) {
            // Server responds with error
            const status = error.response.status;

            // in case of bad request
            if (status === 400) {
                throw new Error(error.response.data?.error || "There was an issue while fetching data , please try again")
            } 
            else {
                throw new Error("There was an issue while fetching data , please try again");
            }
        } else if (error.request) {
            // Request made but no response received
            throw new Error("Taking time to get response, Please check your network.");
        } else {
            // Something else happened
            throw new Error("There was an issue while fetching data , please try again");
        }
    }
};