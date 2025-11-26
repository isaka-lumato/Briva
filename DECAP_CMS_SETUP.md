# Decap CMS Setup Guide for Briva Website

## 🎯 What is Decap CMS?

Decap CMS is a git-based content management system that allows you to edit your website content through a user-friendly admin interface. All changes are saved directly to your GitHub repository and automatically deployed by Netlify.

---

## 📋 Prerequisites

Before proceeding, you need:
- ✅ Your website hosted on **Netlify**
- ✅ Your code in a **GitHub** or **GitLab** repository
- ✅ **Admin access** to both Netlify and GitHub

---

## 🚀 Step-by-Step Setup

### Step 1: Convert Projects Data Format

Your current `projects.json` uses an object format. Decap CMS works better with arrays. Run this command to convert:

```bash
node admin/convert-projects.js
```

This will:
- Create a backup (`projects-backup.json`)
- Convert your projects to the new format
- Your website will still work with both formats!

### Step 2: Enable Netlify Identity

1. Go to your **Netlify Dashboard**
2. Select your **Briva** site
3. Click **"Identity"** in the top menu
4. Click **"Enable Identity"**
5. Under **Registration**, select **"Invite only"** (recommended)
6. Under **Services** → **Git Gateway**, click **"Enable Git Gateway"**

### Step 3: Add Yourself as an Admin User

1. In Netlify Identity settings, click **"Invite users"**
2. Enter your email address
3. Check your email and click the invite link
4. Set your admin password

### Step 4: Update Admin Files

Rename the Decap admin file:
```bash
# In the /admin folder
mv decap-index.html index.html
```

Or manually rename `admin/decap-index.html` to `admin/index.html`

### Step 5: Deploy to Netlify

Push your changes to GitHub:

```bash
git add .
git commit -m "Add Decap CMS admin panel"
git push origin main
```

Netlify will automatically rebuild your site.

### Step 6: Access the Admin Panel

Once deployed, visit:
```
https://your-site.netlify.app/admin/
```

Login with the email and password you set up in Step 3.

---

## 🎨 Using the Admin Panel

### Managing Projects

1. **Login** to `https://your-site.netlify.app/admin/`
2. Click **"Projects"** → **"All Projects"**
3. Click **"Edit"**
4. You'll see a list of all projects
5. **Add a new project:**
   - Click **"Add projects"** at the bottom
   - Fill in all fields (Project ID, Title, Location, etc.)
   - Upload images or paste image paths
   - Click **"Save"**
6. **Edit existing project:**
   - Click on any project in the list
   - Modify the fields
   - Click **"Save"**
7. **Delete a project:**
   - Expand the project
   - Click the **trash icon**
8. Click **"Publish"** (top right) to save all changes

### Managing Site Settings

1. Click **"Site Settings"** → **"General Settings"**
2. Edit contact information, social media URLs
3. Click **"Publish"** to save

---

## 🔐 Security Notes

- **Invite only:** Keep registration set to "Invite only" in Netlify Identity
- **Password:** Use a strong password for your admin account
- **2FA:** Enable two-factor authentication in Netlify if possible
- **Git Gateway:** Only authorized users can commit changes

---

## 🧪 Testing Locally (Optional)

To test the CMS before deploying:

1. Install Decap CMS Proxy:
   ```bash
   npx decap-server
   ```

2. In `admin/config.yml`, uncomment:
   ```yaml
   local_backend: true
   ```

3. Open `http://localhost:8080/admin/`

---

## 📂 File Structure

```
admin/
├── index.html          # Decap CMS interface (renamed from decap-index.html)
├── config.yml          # CMS configuration
└── convert-projects.js # Data conversion script

data/
├── projects.json       # Your projects (new array format)
├── projects-backup.json # Backup of old format
└── site-settings.json  # Site-wide settings

js/
└── project-details.js  # Updated to support both formats
```

---

## 🔄 Workflow

```
1. Edit content in admin panel
       ↓
2. Click "Publish"
       ↓
3. Decap creates Git commit
       ↓
4. Netlify detects change
       ↓
5. Site rebuilds automatically
       ↓
6. Changes are live! ✅
```

---

## ❓ Troubleshooting

**Can't access /admin:**
- Ensure `admin/index.html` exists (renamed from `decap-index.html`)
- Clear browser cache
- Check Netlify deployment logs

**"Git Gateway Not Enabled" error:**
- Go to Netlify → Identity → Services → Enable Git Gateway

**Changes not appearing:**
- Check Netlify deploy status
- Projects might still be cached - hard refresh (Ctrl+Shift+R)

**Image uploads not working:**
- Ensure `images/projects` folder exists
- Check Netlify build settings include image folder

---

## 🆘 Need Help?

- Decap CMS Docs: https://decapcms.org/docs/
- Netlify Identity: https://docs.netlify.com/visitor-access/identity/
- Contact your developer

---

## ✅ Checklist

- [ ] Converted projects.json format
- [ ] Enabled Netlify Identity
- [ ] Enabled Git Gateway
- [ ] Invited yourself as admin
- [ ] Renamed `decap-index.html` to `index.html`
- [ ] Deployed to Netlify
- [ ] Tested logging in to /admin
- [ ] Successfully added/edited a test project

---

**Ready to go live? Follow the steps above and you'll be editing content in minutes!** 🚀
