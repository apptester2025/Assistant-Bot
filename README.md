# FEMA Compliance Bot

The FEMA Compliance Bot is a lightweight Discord bot designed to demonstrate how AI can streamline workflows by integrating Python-based tools. This bot is part of the TECH 1000 CHALLENGE at Tetra Tech, showcasing how quickly AI solutions can be implemented into tools we already use.

## Features
- GPT-powered responses for data validation and reasoning.
- Flask server integration to prevent timeout issues on Render.
- Hosted in the cloud for 24/7 availability.

---

## Local Setup

Follow these steps to set up and run the bot locally:

### Prerequisites
1. **Python 3.11.11**: Ensure Python is installed. You can download it from [python.org](https://www.python.org/).
2. **Dependencies**: Install the required Python packages.
3. **API Keys**: Obtain API keys for the services used by the bot (e.g., OpenAI, Discord).

### Installation on Mac Sequia 15.2 (24C101) (not tested anywhere else locally)
I vary between using pyenv & homebrew to manage python packages on my computer. For this exmaple I've used pyenv to set my local python to version @3.11.11 - this only impacted local development. Once the code was pushed to the cloud the version running on Render is @3.11.11 by default as of writing this. 

**THIS IS UNSTABLE AND WILL NEED TO BE UPDATED FOR PRODUCTION**

1. Clone the repository:

	```git clone https://github.com/ppdrmonitor/FEMA-Compliance-Bot.git```
	```cd FEMA-Compliance-Bot```
   

2. Install dependencies:
   
	```pip install -r requirements.txt```

3. Set up your .env file: Create a .env file in the project root and add your API keys:
	
	```DISCORD_TOKEN=your_discord_bot_token```
	```OPENAI_API_KEY=your_openai_api_key```

4. Run the bot:
	
	```python fema_discord_bot.py```

The bot should now be running locally. You can invite it to your server using the bot's invite link.

### Cloud Hosting with Render

To keep the bot active 24/7, host it on Render.

1. Create a new web service on Render.
2. Connect your GitHub repository to the service.
3. Set up the environment variables for API keys in Render's dashboard.
4. Deploy the service.

### Flask Integration
The bot uses Flask to handle the web server and prevent Render's timeout issues. The fema_discord_bot.py file includes the necessary configuration.

### Roadmap

Potential AI Implementations for TDR

1. GroupMe Bot: Extend the functionality of this bot to integrate with GroupMe, which is more widely used in TDR.

2. Field Data Automation: Automate workflows for field monitors:
	- Validate collection log images.
	- Extract data and check for backend matches.
	- Generate PDFs with consistent naming conventions and upload them to Box folders.

3. Advanced Data Tools:
	- Verify data context.
	- Generate custom responses for response teams.
	- Perform advanced data reasoning for field tasks.

These applications could significantly enhance productivity and reduce human error in TDR workflows.

### Contribution
Contributions are welcome! Fork the repository and submit a pull request with your enhancements.

### License
This project is open-source and available under the MIT License.

