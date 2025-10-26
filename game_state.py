"""
Shared Game State Manager
All teams and admin interact through this shared state
"""
import json
import os
from dataclasses import dataclass, asdict
from typing import Optional, List
from datetime import datetime

# Shared state file path
STATE_FILE = "data/game_state.json"
ACTIONS_FILE = "data/actions_queue.json"

@dataclass
class Team:
    team_id: str
    name: str
    color: str
    balance: int
    position: int
    active: bool = True

@dataclass
class Property:
    index: int
    name: str
    price: int
    rent: int
    owner: Optional[str] = None

@dataclass
class ActionRequest:
    action_id: str
    team_id: str
    action_type: str  # 'roll_dice', 'buy_property', 'chance_answer', 'sell_property'
    params: dict
    timestamp: str
    status: str = 'pending'  # 'pending', 'approved', 'rejected'

class GameState:
    def __init__(self):
        self._ensure_data_dir()
        self.teams = [
            Team("T1", "Team 1", "#D32F2F", 10_000_000, 0),
            Team("T2", "Team 2", "#1976D2", 10_000_000, 0),
            Team("T3", "Team 3", "#388E3C", 10_000_000, 0),
            Team("T4", "Team 4", "#F57C00", 10_000_000, 0),
            Team("T5", "Team 5", "#7B1FA2", 10_000_000, 0),
        ]
        self.current_team_idx = 0
        self.properties = self._create_properties()
        self.actions_queue: List[ActionRequest] = []
        self.game_started = False
        self.current_dice_roll = 0
        
    def _ensure_data_dir(self):
        """Ensure data directory exists"""
        os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    
    def _create_properties(self):
        """Create initial property list"""
        return [
            Property(0, "START/GO", 0, 0),
            Property(1, "Digital Marketing", 2_000_000, 500_000),
            Property(2, "MYSTERY WHEEL", 0, 0),
            Property(3, "Social Media", 2_500_000, 600_000),
            Property(4, "CHANCE", 0, 0),
            Property(5, "Content Marketing", 2_000_000, 500_000),
            Property(6, "Society Penalty", 0, 0),
            Property(7, "Email Marketing", 2_500_000, 600_000),
            Property(8, "CHANCE", 0, 0),
            Property(9, "SEO", 3_000_000, 800_000),
            Property(10, "MYSTERY WHEEL", 0, 0),
            Property(11, "PPC Advertising", 3_500_000, 1_000_000),
            Property(12, "Free Parking", 0, 0),
            Property(13, "Influencer Marketing", 3_000_000, 800_000),
            Property(14, "MYSTERY WHEEL", 0, 0),
            Property(15, "Brand Management", 3_500_000, 1_000_000),
            Property(16, "CHANCE", 0, 0),
            Property(17, "Event Management", 2_500_000, 600_000),
            Property(18, "Event Penalty", 0, 0),
            Property(19, "Market Research", 3_000_000, 800_000),
            Property(20, "CHANCE", 0, 0),
            Property(21, "PR & Communications", 3_500_000, 1_000_000),
            Property(22, "MYSTERY WHEEL", 0, 0),
            Property(23, "Analytics", 2_000_000, 500_000),
        ]
    
    def save(self):
        """Save game state to file"""
        data = {
            'current_team_idx': self.current_team_idx,
            'teams': [asdict(t) for t in self.teams],
            'properties': [asdict(p) for p in self.properties],
            'game_started': self.game_started,
            'current_dice_roll': self.current_dice_roll,
        }
        with open(STATE_FILE, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load(self):
        """Load game state from file"""
        if not os.path.exists(STATE_FILE):
            return
        
        with open(STATE_FILE, 'r') as f:
            data = json.load(f)
        
        self.current_team_idx = data.get('current_team_idx', 0)
        self.game_started = data.get('game_started', False)
        self.current_dice_roll = data.get('current_dice_roll', 0)
        
        # Load teams
        teams_data = data.get('teams', [])
        self.teams = [Team(**t) for t in teams_data]
        
        # Load properties
        props_data = data.get('properties', [])
        self.properties = [Property(**p) for p in props_data]
    
    def add_action(self, action_type: str, team_id: str, params: dict = None):
        """Add an action to the queue"""
        action_id = f"{team_id}_{datetime.now().timestamp()}"
        action = ActionRequest(
            action_id=action_id,
            team_id=team_id,
            action_type=action_type,
            params=params or {},
            timestamp=datetime.now().isoformat(),
            status='pending'
        )
        self.actions_queue.append(action)
        self.save_actions_queue()
        return action_id
    
    def get_pending_actions(self):
        """Get all pending actions"""
        return [a for a in self.actions_queue if a.status == 'pending']
    
    def approve_action(self, action_id: str):
        """Approve an action and remove it from queue"""
        for action in self.actions_queue:
            if action.action_id == action_id:
                action.status = 'approved'
                self.save_actions_queue()
                return action
        return None
    
    def reject_action(self, action_id: str):
        """Reject an action"""
        for action in self.actions_queue:
            if action.action_id == action_id:
                action.status = 'rejected'
                self.save_actions_queue()
                return action
        return None
    
    def save_actions_queue(self):
        """Save actions queue to file"""
        data = [asdict(a) for a in self.actions_queue]
        with open(ACTIONS_FILE, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_actions_queue(self):
        """Load actions queue from file"""
        if not os.path.exists(ACTIONS_FILE):
            return
        
        with open(ACTIONS_FILE, 'r') as f:
            data = json.load(f)
        
        self.actions_queue = [ActionRequest(**a) for a in data]
    
    def get_team_by_id(self, team_id: str):
        """Get team by ID"""
        for team in self.teams:
            if team.team_id == team_id:
                return team
        return None
    
    def get_current_team(self):
        """Get current team"""
        return self.teams[self.current_team_idx]
    
    def format_money(self, amount: int) -> str:
        """Format money amount"""
        return f"₹{amount:,}"

