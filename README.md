# Flask Vue App

This project is a full-stack application built with Python Flask for the backend and Vue.js with Vuetify for the frontend as a Tech Challenge for the Deeper System role as Entry-Level Web Developer.

## Project Structure

```
deeper_systems/
├── docker-compose.yaml
├── README.md
├── server/
│   ├── __pycache__/
│   ├── .gitignore
│   ├── app.py
│   ├── clean_db.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── parser.py
│   ├── requirements.txt
│   ├── udata.json
│   └── views.py
└── web/
    ├── .editorconfig
    ├── .gitattributes
    ├── .gitignore
    ├── .prettierrc.json
    ├── .vscode/
    ├── env.d.ts
    ├── eslint.config.ts
    ├── index.html
    ├── package.json
    ├── public/
    ├── README.md
    ├── src/
    │   ├── api/
    │   │   └── UserService.ts
    │   ├── assets/
    │   │   ├── base.css
    │   │   └── main.css
    │   ├── components/
    │   │   ├── ConfirmDialog.vue
    │   │   ├── DeleteDialog.vue
    │   │   ├── UserDialog.vue
    │   │   └── UsersTable.vue
    │   ├── router/
    │   │   └── index.ts
    │   ├── views/
    │   │   ├── MainView.vue
    │   │   └── UserDetails.vue
    │   ├── App.vue
    │   ├── main.ts
    │   └── userDTO.ts
    ├── tsconfig.app.json
    ├── tsconfig.json
    ├── tsconfig.node.json
    └── vite.config.ts
```

## Database
1. Start the docker container with the MongoDB server
```
docker-compose up -d
```

## Backend Setup

1. Navigate to the `backend` directory:
   ```bash
   cd server
   ```

2. Create a Python virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
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
   python app.py
   ```

## Frontend Setup

1. Navigate to the `frontend` directory:
   ```bash
   cd web
   ```

2. Install the required dependencies:
   ```bash
   npm i
   ```

3. Run the Vue.js application:
   ```bash
   npm run dev
   ```


**Note:** The *gist* with the instructions specifies that the database shouldn't have an *updated_at* or *updated_ts* field, but later this info is requested, so I added this field in the User model.