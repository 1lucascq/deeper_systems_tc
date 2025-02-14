# FILE: /flask-vue-app/flask-vue-app/README.md

# Flask Vue App

This project is a full-stack application built with Python Flask for the backend and Vue.js with Vuetify for the frontend, following the MVC architecture.

## Project Structure

```
flask-vue-app
├── backend
│   ├── app
│   ├── tests
│   ├── requirements.txt
│   └── run.py
├── frontend
│   ├── src
│   ├── package.json
│   └── vue.config.js
└── .gitignore
```

## Backend Setup

1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```

2. Create a Python virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the Flask application:
   ```bash
   python run.py
   ```

## Frontend Setup

1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```

2. Install the required dependencies:
   ```bash
   npm install
   ```

3. Run the Vue.js application:
   ```bash
   npm run serve
   ```

## Testing

To run tests for the backend, ensure you have the necessary dependencies installed and run:
```bash
pytest
```

## GitHub Repository

This project is versioned in a GitHub repository. Make sure to commit your changes and push them to the remote repository regularly.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.