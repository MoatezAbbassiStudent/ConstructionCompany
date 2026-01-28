# BuildCraft - AI Assistant Website

A modern, responsive website for a tile and concrete construction company with an integrated AI chatbot assistant.

## Features

✨ **Professional Website Design**
- Modern, responsive layout that works on all devices
- Beautiful gradient color scheme with smooth animations
- Navigation menu with smooth scrolling
- Hero section with call-to-action

📋 **Service Showcase**
- Services grid displaying 4 main services
- Professional service cards with hover effects

🎨 **Project Gallery**
- Showcase 6 featured projects with gradient backgrounds
- Project card hover animations and transitions
- Ready to add real project images

ℹ️ **Company Information**
- About section with company stats
- Contact information with location, phone, and email
- Footer with copyright information

🤖 **AI Chat Assistant**
- Floating chat widget in the corner
- Intelligent responses to customer inquiries
- Knowledge base covering services, contact info, and FAQs
- Smooth animations and professional styling
- Toggle between open/closed states

## Project Structure

```
Website with AI Assistant/
├── app/
│   ├── __init__.py       # Flask app factory
│   └── routes.py         # Chatbot logic & Flask routes
├── static/
│   ├── css/style.css     # Frontend styling
│   └── js/script.js      # Frontend chat logic
├── templates/
│   └── index.html        # Main HTML page
├── Procfile              # Render deployment config
├── requirements.txt      # Python dependencies
├── run.py               # Entry point
└── README.md            # This file
```

## Deployment to Render (FREE)

### Step 1: Push to GitHub
The code is already initialized with git. To push to your GitHub repo:

```bash
cd "C:\Users\Moetez\Desktop\Senior\Website with AI Assistant"
git remote add origin https://github.com/MoatezAbbassiStudent/ConstructionCompany.git
git branch -M main
git push -u origin main
```

**If you get authentication errors:**
1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token"
3. Select `repo` scope
4. Copy the token and use it as password when `git push` prompts

### Step 2: Deploy on Render
1. Go to https://render.com and sign up (free tier available)
2. Click **"New +"** → **"Web Service"**
3. Select **"Connect your GitHub repository"**
4. Find and select `MoatezAbbassiStudent/ConstructionCompany`
5. Fill in these settings:
   - **Name:** `buildcraft-chatbot`
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn -b 0.0.0.0:$PORT -w 2 -t 120 "app:create_app()"`
6. Click **"Create Web Service"**
7. Wait 2-3 minutes for deployment
8. Your live app URL will appear (e.g., `https://buildcraft-chatbot.onrender.com`)

### Alternative: Deploy on Railway
1. Go to https://railway.app and sign up
2. Create new project → Deploy from GitHub
3. Select your repo
4. Railway auto-detects Flask and deploys automatically

## Local Development

### Setup
```bash
# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### Run Locally
```bash
python run.py
```

Visit `http://127.0.0.1:5000` in your browser.

## Installation & Setup

### 1. Navigate to the project directory
```bash
cd "C:\Users\Moetez\Desktop\Senior\Website with AI Assistant"
```

### 2. Activate virtual environment
```bash
venv\Scripts\Activate.ps1
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask application
```bash
python app.py
```

### 5. Open in browser
Navigate to `http://localhost:5000` in your web browser.

## Customization Guide

### Change Company Information
Edit `templates/index.html`:
- Replace "BuildCraft" with your company name
- Update phone number: `+1 (555) 123-4567`
- Update email: `info@buildcraft.com`
- Update address: `123 Construction Ave, City, State 12345`

### Add Project Images
1. Save your project images in `static/images/` folder
2. Edit the project cards in `templates/index.html`:
```html
<div class="project-image" style="background-image: url('{{ url_for('static', filename='images/your-image.jpg') }}');">
```

### Customize Colors
Edit `:root` variables in `static/css/style.css`:
```css
:root {
    --primary-color: #FF6B35;      /* Main orange color */
    --secondary-color: #004E89;    /* Dark blue color */
    --accent-color: #F7931E;       /* Light orange accent */
}
```

### Expand AI Knowledge Base
Edit the `knowledge_base` dictionary in `app.py` to add more Q&A pairs:
```python
knowledge_base = {
    "services": {
        "your service": "Description of your service",
    },
    "general": {
        "your question": "Your answer",
    }
}
```

## Features Explained

### Navigation
- Sticky navigation bar with smooth scrolling to sections
- Hover effects on navigation links
- Professional branding

### Hero Section
- Eye-catching gradient background
- Large headline and subheading
- Call-to-action button that scrolls to contact section

### Services Section
- 4 service cards with icons
- Hover animations for better interactivity
- Easy to add more services

### Projects Gallery
- 6 featured project cards
- Each project shows gradient background (ready for real images)
- Smooth hover effects

### About Section
- Company information and history
- List of key features and benefits
- Statistics cards showing experience metrics

### Contact Section
- Complete contact information
- Easy-to-scan contact details with icons
- Ready to integrate with contact forms

### AI Chat Widget
- Floating chat button in bottom-right corner
- Modern chat interface with message history
- Responsive on mobile devices
- Ready to add more advanced NLP or API integration

## Next Steps & Enhancements

1. **Add Real Images**
   - Replace placeholder gradients with actual project photos
   - Add company logo and team photos

2. **Upgrade AI Assistant**
   - Integrate with OpenAI API for advanced natural language processing
   - Add sentiment analysis
   - Implement conversation memory

3. **Database Integration**
   - Store chat history
   - Track customer inquiries
   - Manage projects and testimonials

4. **Additional Features**
   - Contact form with email integration
   - Customer testimonials/reviews section
   - Blog or news section
   - Before/after project comparisons
   - Video gallery
   - Appointment booking system

5. **SEO Optimization**
   - Add meta tags
   - Optimize for search engines
   - Create sitemap

6. **Deployment**
   - Deploy to Heroku, PythonAnywhere, or similar platform
   - Set up SSL certificate for HTTPS
   - Configure custom domain

## Support

For questions or issues, check the code comments or review the configuration options in each file.

---

Made with ❤️ for BuildCraft Construction Company
