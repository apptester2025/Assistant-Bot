# Simple Assistant Bot (Alpha)

A lightweight, multi-platform AI assistant demonstrating natural language queries and contextual AI insights being integrated into Discord and GroupMe using opensource tools.

## Features

- ** Parsing & Insights**:  
  Utilizes GPT-based AI to analyze documents and provide actionable interpretations.  

- **Multi-Platform Integration**:  
  Accessible via Discord and GroupMe for real-time collaboration and support.

- **Ease of Use**:  
  Lightweight design with a conversational interface tailored to specific needs.

## Future Roadmap

- **Advanced Analysis**:  
  Automated document updates and contextual guidance for complex scenarios.

- **Workflow Automation**:  
  Streamlined processes, logging, and workflows.

- **Dynamic Training Modules**:  
  AI-powered, adaptive data aligned with evolving situations.

- **Multi-Project Management**:  
  Tools for tracking across multiple operations.

- **Platform Expansion**:  
  Web, desktop, and mobile application integrations to enhance accessibility.


## Dev Highlights

- Discord & GroupMe integration
- OpenAI GPT model integration
- Landing page built with TypeScript and Tailwind CSS
- Cross-platform compatibility (Windows, Linux, macOS)

## Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.x ([Download](https://python.org))
- Node.js and npm ([Download](https://nodejs.org))
- Git ([Download](https://git-scm.com))

## Local Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/apptester2025/Assistant-Bot.git
   cd Assitant-Bot
   ```

2. **Set Up Python Environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   
   pip install -r requirements.txt
   ```

3. **Install Node.js Dependencies**
   ```bash
   npm install
   ```

4. **Configure Environment Variables**
   Create a `.env` file in the project root and add necessary variables:
   ```
   OPENAI_API_KEY=your_openai_api_key
   DISCORD_TOKEN=your_discord_bot_token
   GROUPME_BOT_ID=your_groupme_bot_id
   # Add other required environment variables
   ```

5. **Build Frontend Assets**
   ```bash
   npm run build
   ```

6. **Run the Application**
   ```bash
   python run.py
   ```

## Key Dependencies

### Python Packages
- discord.py - Discord API integration
- openai - GPT model integration
- flask - Web server functionality

### Node.js Packages
- vite - Frontend build tool
- tailwindcss - UI styling
- typescript - Type-safe JavaScript

## Cloud Deployment Options

### Render (Recommended for Testing)
1. Create an account at [render.com](https://render.com)
2. Create a new Web Service
3. Connect your GitHub repository
4. Configure build command:
   ```bash
   npm install && npm run build && pip install -r requirements.txt
   ```
5. Set start command:
   ```bash
   python run.py
   ```
6. Add environment variables in the Render dashboard

### AWS (Free Tier)
1. Sign up at [aws.amazon.com](https://aws.amazon.com)
2. Install AWS CLI and Elastic Beanstalk CLI
3. Initialize and deploy:
   ```bash
   eb init -p python-3.x assistant-bot
   eb create assistant-bot-env
   eb deploy
   ```

### Heroku
1. Create account at [heroku.com](https://heroku.com)
2. Install Heroku CLI
3. Deploy:
   ```bash
   heroku login
   heroku create assistant-bot
   git push heroku main
   heroku config:set DISCORD_TOKEN=your_discord_token
   ```

### Azure
1. Sign up at [azure.microsoft.com](https://azure.microsoft.com)
2. Install Azure CLI
3. Deploy:
   ```bash
   az webapp up --name assistant-bot --resource-group MyResourceGroup --runtime "PYTHON|3.9"
   ```

## Development

To run the frontend development server:
```bash
npm run dev
```

This will start a local server at `http://localhost:3000`.

## Command Reference

| Command | Description |
|---------|-------------|
| `npm run build` | Build frontend assets |
| `npm run dev` | Start development server |
| `python run.py` | Run backend server |

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is open-source and available under the MIT License.
