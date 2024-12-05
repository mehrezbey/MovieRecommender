# MovieRecommender

MovieRecommender is an app that recommends a movie after you answer 7 questions.

## Setup Instructions

1. **Create an API Key**  
   Sign up at [TheMovieDB](https://www.themoviedb.org/) and generate an API key. Then, create a `.env` file in the root directory and add your API key as `SECRET_KEY` (refer to the `.env.example` file for the format).

2. **Create a Virtual Environment**  
   ```
   python -m venv .venv
   ```

3. **Activate the Virtual Environment**
    - On Windows:
    ```
    .\.venv\Scripts\activate
    ```
    - On macOS/Linux:
    ```
    source .venv/bin/activate
    ```

4- **Install Dependencies**

    
    pip install -r requirements.txt
    

5- **Run**

    ```
    streamlit run movie_recommender.py
    ```



6- **Deactivate venv**
    ```
    deactivate
    ```
