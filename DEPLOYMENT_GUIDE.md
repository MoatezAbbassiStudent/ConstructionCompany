## 🔑 GitHub Personal Access Token Setup

### Step 1: Create Token on GitHub
1. Go to: https://github.com/settings/tokens?type=beta
2. Click "Generate new token"
3. Select "Fine-grained personal access tokens"
4. Fill in:
   - **Token name:** GitHub Push Token
   - **Expiration:** 90 days
   - **Resource owner:** MoatezAbbassiStudent
   - **Repository access:** Select "Only select repositories" → Choose "ConstructionCompany"
   - **Permissions:** 
     - Contents: Read and write
     - Metadata: Read-only
5. Click "Generate token"
6. **COPY THE TOKEN** (you'll only see it once!)

### Step 2: Use Token for Git Push
In PowerShell, run:
```powershell
cd "C:\Users\Moetez\Desktop\Senior\Website with AI Assistant"
git config credential.https://github.com.username MoatezAbbassiStudent
git push -u origin main
```

When prompted for password, **paste your token** (not your GitHub password)

### Step 3: Verify Push
Go to https://github.com/MoatezAbbassiStudent/ConstructionCompany
You should see all files uploaded!

---

## 🚀 Deploy on Render After Push

Once GitHub has your code:
1. Go to https://render.com
2. Sign up with GitHub
3. Click **"New +"** → **"Web Service"**
4. Click **"Connect account"** (GitHub)
5. Authorize Render to access GitHub
6. Select **"ConstructionCompany"** repo
7. Fill settings:
   - **Name:** buildcraft-chatbot
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn -b 0.0.0.0:$PORT -w 2 -t 120 "app:create_app()"`
8. Click **"Create Web Service"**
9. Wait 2-3 minutes
10. Your live app: `https://buildcraft-chatbot.onrender.com`

---

**Once deployed, your chatbot will be live 24/7 on Render's free tier!** ✨
