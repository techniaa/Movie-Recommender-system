# 🎬 Movie Recommender System  

A personalized **Movie Recommendation Web App** built using **Python**, **Streamlit**, and **Machine Learning**.  
It recommends similar movies based on user selection, leveraging a precomputed **cosine similarity model** and fetching **movie posters dynamically** via the TMDb API.  

---

## 🚀 Live Demo  
🔗 **[Try the App on Streamlit Cloud](https://movie-recommender-system-xpfd3kpn9qtknwxoulrnc8.streamlit.app/)**  


---

## 🧠 Overview  

The app provides movie recommendations using a content-based filtering approach.  
When a user selects a movie, the system finds similar titles by comparing feature vectors generated from the TMDb dataset.  

Key features include:  
- Interactive movie selection  
- Dynamic poster fetching via TMDb API  
- Stylish dark-mode Gen-Z interface  
- Lightweight & cloud-deployable using Streamlit  

---

## 🧩 Tech Stack  

| Category | Technology |
|-----------|-------------|
| Framework | Streamlit |
| Language | Python |
| Libraries | pandas, requests, pickle, gdown |
| Model | Cosine Similarity (Content-Based Filtering) |
| API | TMDb (for movie posters) |
| Hosting | Streamlit Cloud |

---

## 📁 Project Structure  
```bash
movie-recommender-system/
│
├── app.py # Main Streamlit app
├── movie_dict.pkl # Movie data dictionary
├── similarity.pkl # Precomputed similarity matrix
├── requirements.txt # Project dependencies
├── README.md # Project documentation
└── images/ # (Optional) assets for README visuals
```
---


## 📦 Data Files

The following files are required to run the app:
- `movie_dict.pkl` – contains the preprocessed movie metadata
- `similarity.pkl` – contains the cosine similarity matrix

If not present, these files will be automatically downloaded from Google Drive using gdown.

---

## 💡 Features

- ✅ Gen-Z inspired dark theme
- ✅ Fast and interactive UI
- ✅ Top 20 similar movie recommendations
- ✅ Real-time poster fetching via TMDb
- ✅ Lightweight model, quick load time

---

## 🔮 Future Improvements

- 🚧 Add collaborative filtering model
- 🎭 Include genre and rating filters
- 🎞️ Improve poster fallback images
- 📱 Add responsive mobile layout
- 💬 Allow users to rate or save favorite movies

---

## 🧑‍💻 Author

**Neha**  
Blockchain & AI Developer | Fullstack Enthusiast  
📫 [LinkedIn](https://www.linkedin.com/in/neha-shah-056332247) • [GitHub](https://github.com/techniaa)

