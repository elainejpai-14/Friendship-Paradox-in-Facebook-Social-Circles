# Friendship Paradox in Social Circles

A visual analytics dashboard built with Plotly Dash to explore the **Friendship Paradox** — the idea that *on average, your friends have more friends than you do* — using Facebook ego-network data. This paradox highlights how your friends are likely to have more friends than you.

We investigate how this paradox appears in different ego networks, visualize key metrics, and build an interactive dashboard with Plotly Dash to analyze network properties such as degree distribution, paradox strength, and centrality.

---

## About the Project

The **Friendship Paradox** is a well-known phenomenon in social networks. It emerges from the fact that high-degree nodes (very social users) are overrepresented in the neighbor lists of others, skewing the average.

In this project, we:
- Load and analyze ego networks from Facebook.
- Measure paradox presence and strength across users.
- Identify top paradoxical nodes.
- Compare results with random networks.
- Build an interactive **Dash dashboard** for real-time filtering and visualizations.

---

## Dataset Used

We use the **Facebook Social Circles** dataset provided by the Stanford Network Analysis Project (SNAP).

- Dataset: [`facebook.tar.gz`](https://snap.stanford.edu/data/ego-Facebook.html)
- Each `.edges` file represents an ego network (i.e., a user and their friends).
- Attributes analyzed: degree, average friend degree, paradox strength, centrality metrics, communities.

**Citation (if used in research):**
If you use this dataset, please cite the following paper:

> J. McAuley and J. Leskovec. *Learning to Discover Social Circles in Ego Networks*. In NIPS, 2012.  
> [https://snap.stanford.edu/data/egonets-Facebook.html](https://snap.stanford.edu/data/egonets-Facebook.html)

---

## Live Public Dashboard

Explore the Live interactive Render dashboard here: [https://friendship-paradox-in-facebook-social.onrender.com/](https://friendship-paradox-in-facebook-social.onrender.com/)

---

## Features of the Dashboard

- Dropdown filter to toggle between:
  - All users
  - Only users for whom the paradox holds
  - Only users for whom it does not
- Histogram of user degree distribution
- Histogram of paradox strength
- Scatter plot of degree vs paradox strength
- Color-coded node classification (paradox vs non-paradox)

---

## Technologies Used

- `Python`
- `NetworkX`, `NumPy`, `Matplotlib`, `PyVis`, `Plotly`
- `Dash`, `Dash Bootstrap Components`
- `Google Colab` for data processing
- `Render` for public deployment

---

## How to Run

### Locally:
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/friendship-paradox-dashboard.git
   cd friendship-paradox-dashboard
   ```
2. Install Dependencies
   (Make sure Python 3.7+ is installed)
    ```bash
    pip install -r requirements.txt
    ```
3. Run the App
   ```bash
   python app.py
   ```
   
### On Render:
1. Create a Free Account
Go to [Render.com](https://render.com/) and sign up.

2. Create a New Web Service
- Click "New + → Web Service"
- Connect your GitHub repo
- Fill in:
  - Environment: Python 3
  - Build Command: pip install -r requirements.txt
  - Start Command: python app.py
  - Port: 8050

3. Add the Required Files to Your Repo
  - `app.py` – Your Dash app
  - `requirements.txt` – All Python packages needed
  - `paradox_analysis.csv` – Data file (ensure it's committed in the repo)
  - `render.yaml` – Optional but recommended
4. Wait for Build & Access Your Public Link <br>
Once deployed, Render will give you a public URL

---

## Screenshots / GIF

An Interactive vizualization of the loaded friendship network, where node size and color encode paradox strength and degree respectively. This helps explore node-level characteristics visually.<br>
![Vizualize the network](Vizualize%20Network.gif)<br><br>
A snip from the dashboard showing a plot of Paradox Strength vs the Degree for both paradox and non-paradox nodes.<br>
<img width="1679" height="481" alt="image" src="https://github.com/user-attachments/assets/a785fd03-c77d-4395-9ecb-01699a23bdd3" /><br><br>

The Green dots:
true → Nodes where the Friendship Paradox holds: their friends, on average, have more friends than they do.

Most of these users have low degrees (between 1 and 20), but very high paradox strength values, sometimes over 50×.

The Purple dots:
false → Nodes where the Friendship Paradox does not hold.

These users tend to have higher degrees (more friends), meaning their own degree is close to or exceeds that of their friends.


