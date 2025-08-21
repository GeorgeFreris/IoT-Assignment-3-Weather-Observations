# app.py
 
# Import Flask and your BOM stats function
from flask import Flask, render_template
from BOM_observations import get_bom_stats
import os
 
# Initialize Flask app
app = Flask(__name__)
 
# Define route to display weather stats
@app.route('/weather')
def weather():
    # Get stats from bom_stats.py
    stats = get_bom_stats()
 
    # Show error if data couldn't be fetched
    if not stats:
        return "<h1>Error fetching BOM data</h1>"
 
    # Render HTML template with stats
    return render_template("web_temp.html", stats=stats)
 
# Run the app using the port provided by Render or default to 5000
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
