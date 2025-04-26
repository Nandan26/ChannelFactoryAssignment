## A web application built with Django (backend) and React (frontend).

### Prerequisites

Make sure the following are installed on your machine:

- **Python** (latest stable version)
- **pip** (Python package manager)
- **Node.js** (latest stable version)
- **npm** (Node package manager)


### Installation

To set up the project on your local machine, follow these steps:

1. Clone the repository:  
   `git clone https://github.com/Nandan26/ChannelFactoryAssignment.git`
2. Navigate to the project directory
3. Navigate to the backend directory
4. Create a virtual environment and activate it:  
   `python -m venv myenv`
5. Install the python dependencies for backend:  
   `pip install -r requirements.txt`
6. Create the .env file to store google maps API key
   `GOOGLE_MAPS_API_KEY = YOUR_API_KEY`
7. Apply the database migrations:  
   `python manage.py migrate`
8. Run the development server:  
   `python manage.py runserver`
9. Access the backend in your web browser at `http://localhost:8000`.


10. Now navigate to the frontend directory
11. Install all the dependancy from package.json 
    `npm i`
12. Run the development server:
    `npm start`
13. Access the frontend in your web browser at `http://localhost:3000`. 

You can refer to below video for setup and demo

### Demo Video

<a href="https://youtu.be/i3J4A40Ap44">Watch Setup and Working Demo</a>
   
### Future Enhancements

- **Convert Django REST endpoints to asynchronous views** for improved performance and scalability.
- **Implement caching** (e.g., using Redis) to optimize repeated API requests.
