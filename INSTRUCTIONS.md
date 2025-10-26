# Setup and Usage Instructions

## 🎯 How to Use This System

### Step 1: Install and Run

```bash
cd streamlit_multiplayer
pip install streamlit
streamlit run streamlit_app.py
```

The app will open at `http://localhost:8501`

### Step 2: Deploy to Streamlit Cloud (Recommended)

1. **Create GitHub Repository**
2. **Upload all files** from `streamlit_multiplayer/` folder
3. **Go to** [share.streamlit.io](https://share.streamlit.io)
4. **Sign in** with GitHub
5. **Click** "New app"
6. **Fill in**:
   - Repository: Your GitHub repo
   - Branch: main/master
   - Main file: `streamlit_app.py`
7. **Click** "Deploy"
8. **Share the URL** with all participants

### Step 3: Login Credentials

**Admin Panel:**
- Role: `ADMIN`
- Password: `admin123`

**Team Panels:**
- Team 1: Password: `team1`
- Team 2: Password: `team2`
- Team 3: Password: `team3`
- Team 4: Password: `team4`
- Team 5: Password: `team5`

## 🎮 Game Flow Example

### Scenario: Team 1's Turn

1. **Admin opens** the app and logs in as `ADMIN` with password `admin123`
2. **Admin starts the game** by clicking "▶️ Start Game"
3. **Team 1 opens** the same URL and logs in as `T1` with password `team1`
4. **Team 1 clicks** "🎲 Roll Dice" button
5. **Back on admin screen**: A pending action appears "Roll Dice request from Team 1"
6. **Admin clicks** "✅ Approve" button
7. **Dice is rolled** automatically and Team 1 moves
8. **Team 1 can now** buy property, end turn, etc.

## 📊 Admin Responsibilities

✅ Monitor all pending actions
✅ Approve/reject team actions
✅ See all teams' balances and positions
✅ Manually adjust positions/balances if needed
✅ Screen-share the admin panel to show game to participants
✅ Save game state regularly

## 👥 Team Responsibilities

✅ Log in with team password
✅ Request actions (roll dice, buy property, etc.)
✅ Wait for admin approval
✅ Make decisions when landing on properties
✅ End turn when finished

## 🎯 Chance Cards Flow

1. Team lands on CHANCE position (4, 8, 16, 20)
2. Team sees "🎯 Chance Card" button and clicks it
3. A question appears with A/B/C/D options
4. Team clicks an answer
5. **Admin sees**: "chance_answer request from Team X"
6. Admin can see if answer is correct
7. Admin clicks "✅ Approve"
8. If correct: Team gets bonus money (₹500K - ₹2M)

## 🎡 Mystery Wheel Flow

1. Team lands on MYSTERY position (2, 10, 14, 22)
2. Team sees "🎡 Spin Mystery Wheel" button and clicks it
3. Random result appears immediately (no approval needed)
4. Admin sees the result in action queue
5. Effect is applied automatically

## 💰 Buying Properties

1. Team lands on a property
2. Team clicks "💰 Buy Property"
3. Request sent to admin
4. Admin sees: "buy_property request from Team X"
5. Admin clicks "✅ Approve"
6. Property is purchased and team balance deducted

## 🏠 Selling Properties

1. Team goes to "My Properties" section
2. Team clicks "Sell" button next to owned property
3. Request sent to admin
4. Admin approves
5. Team gets refund (half of purchase price)

## 🔄 Screen-Sharing Setup

**Admin should:**
1. Have admin panel open on your computer
2. Start screen sharing (Zoom, Meet, Teams, etc.)
3. Share the screen showing the admin panel
4. All participants can see game state in real-time

**Teams should:**
1. Each open their own team panel on their device
2. Make their own decisions privately
3. Send requests to admin
4. Watch screen-share to see admin approve and execute

## 📝 Tips for Smooth Gameplay

1. **Admin**: Keep refreshing to see new requests
2. **Teams**: Don't spam requests, wait for approval
3. **Admin**: Approve requests quickly to keep game moving
4. **Both**: Save game state regularly as admin
5. **Admin**: Use manual controls for corrections
6. **Teams**: Check balance before buying properties

## 🐛 Common Issues

### Issue: Actions not showing
- **Solution**: Click refresh in browser
- **Cause**: Streamlit auto-refresh might be delayed

### Issue: Can't login
- **Solution**: Check password is correct (case-sensitive)
- **Solution**: Try logging out and in again

### Issue: Game state not saving
- **Solution**: Click "💾 Save Game State" button
- **Solution**: Check `data/` folder exists

### Issue: Multiple admins
- **Warning**: Only one admin should be active
- **Solution**: Have only one person log in as admin

## 🎓 Training the Admin

Before the event, practice:
1. Logging in as admin
2. Approving dice rolls
3. Approving property purchases
4. Using manual controls
5. Saving game state
6. Screen sharing the admin panel

## 🌐 Production Deployment Checklist

Before the event:
- [ ] Deploy to Streamlit Cloud
- [ ] Test all passwords
- [ ] Have admin practice with system
- [ ] Test screen sharing setup
- [ ] Backup game state data folder
- [ ] Prepare list of passwords for participants
- [ ] Have technical support on standby

## 📞 Support

If issues occur during the event:
1. **Admin** should use manual controls
2. **Save game state** regularly
3. **Reset game** if completely stuck
4. **Keep participants informed** about delays

---

**Made with ❤️ for Arthvidya Marketing Event**

