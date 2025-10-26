# Arthvidya Monopoly - Multiplayer Version

A multiplayer Streamlit-based Monopoly game where participants join via shared links.

## 🎮 How It Works

1. **Share the Link**: All participants (teams + admin) use the same Streamlit app URL
2. **Login**: Each person logs in with their role (Admin, Team 1-5) and password
3. **Team Actions**: Teams request actions (roll dice, buy property, etc.)
4. **Admin Approval**: Admin approves/rejects actions and sees all game state
5. **Screen Share**: Admin screen-shares the game display with participants

## 🚀 Quick Start

### Installation

```bash
pip install streamlit
```

### Run the App

```bash
cd streamlit_multiplayer
streamlit run streamlit_app.py
```

### Default Passwords

| Role | Password |
|------|----------|
| Admin | `admin123` |
| Team 1 | `team1` |
| Team 2 | `team2` |
| Team 3 | `team3` |
| Team 4 | `team4` |
| Team 5 | `team5` |

## 🎯 Game Flow

### For Teams:
1. Login with your team password
2. See your balance and position
3. Click "Roll Dice" - request sent to admin
4. Admin approves - you move automatically
5. Land on a property - click "Buy Property" if desired
6. End your turn when done

### For Admin:
1. Login with admin password
2. See all pending action requests
3. Approve/reject each action
4. Monitor all teams' balances and positions
5. Use manual controls if needed
6. Share screen to show game to participants

## 📋 Features

✅ **Team Interface**: Action buttons, property management
✅ **Admin Panel**: Approve/reject actions, monitor game state
✅ **Action Queue**: All team actions require admin approval
✅ **Chance Cards**: Interactive questions with admin approval
✅ **Mystery Wheel**: Random effects with admin control
✅ **Persistent State**: Game state saved to file
✅ **Manual Controls**: Admin can manually adjust positions/balances

## 🌐 Deploy to Streamlit Cloud

1. **Create GitHub repository**
2. **Push files**:
   ```bash
   git init
   git add .
   git commit -m "Streamlit multiplayer monopoly"
   git push origin main
   ```

3. **Deploy to Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - New app → Select repo
   - Main file: `streamlit_app.py`
   - Deploy!

4. **Share the URL** with all participants

## 🔧 Customization

### Change Passwords
Edit `config.py`:
```python
PASSWORDS = {
    "ADMIN": "your_admin_password",
    "T1": "team1_password",
    # ...
}
```

### Adjust Starting Balance
Edit `game_state.py`:
```python
Team("T1", "Team 1", "#D32F2F", 20_000_000, 0)
```

### Add More Chance Questions
Edit `config.py` - add to `CHANCE_QUESTIONS` list

## 📁 Project Structure

```
streamlit_multiplayer/
├── streamlit_app.py    # Main entry point
├── game_state.py       # Shared game state manager
├── team_view.py        # Team interface
├── admin_view.py       # Admin interface
├── config.py          # Configuration and passwords
├── requirements.txt    # Dependencies
├── README.md          # This file
└── data/              # Game state storage
    ├── game_state.json
    └── actions_queue.json
```

## 🎲 Game Mechanics

- **5 Teams**: Each starts with ₹10 million
- **24 Properties**: Marketing-themed locations
- **Chance Cards**: Knowledge questions (positions 4, 8, 16, 20)
- **Mystery Wheel**: Random effects (positions 2, 10, 14, 22)
- **Penalties**: Society (₹1M) and Event (₹1.5M)
- **GO Bonus**: ₹2M when passing/landing on GO

## 💡 Tips

- **Admin**: Keep the window open and screen-share
- **Teams**: Refresh periodically to see updates
- **Save Often**: Admin can manually save game state
- **Backup**: The `data/` folder contains saved game state

## 🐛 Troubleshooting

**Issue**: Actions not showing
- Solution: Refresh the browser

**Issue**: Game state not updating
- Solution: Click "Save Game State" button as admin

**Issue**: Can't see pending actions
- Solution: Check that admin refreshed after team sent request

---

Made for Arthvidya Marketing Event 🎯

