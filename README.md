# GitHub Secrets Demo

A bare-minimum project to illustrate how to store, inject, and use sensitive credentials (secrets) securely in a GitHub repository using GitHub Actions.

---

## How It Works

1. **GitHub Secrets Storage**: Sensitive tokens (like API keys, passwords, database URLs) are stored securely in your GitHub repository settings. They are encrypted at rest.
2. **Workflow Mapping**: The GitHub Actions workflow (`.github/workflows/demo.yml`) retrieves the secret using the context syntax `${{ secrets.MY_SECRET_TOKEN }}` and maps it to an environment variable (`MY_SECRET_TOKEN`).
3. **Application Consumption**: The script (`main.py`) reads the secret from the environment variable (`os.environ.get("MY_SECRET_TOKEN")`).
4. **Log Masking**: If a secret is printed to standard output during the workflow run, GitHub Actions automatically detects it and masks it with `***` in the logs to prevent accidental exposure.

---

## Step-by-Step Setup Guide

Follow these steps to test this repository:

### Step 1: Create a GitHub Repository and Push this Code
1. Create a new repository on GitHub (e.g., named `github-secrets-demo`).
2. Initialize git, commit these files, and push them to your new GitHub repository:
   ```bash
   git init -b main
   git add .
   git commit -m "Initialize secrets demo project"
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

### Step 2: Add the Secret to GitHub
1. On GitHub, navigate to the main page of your repository.
2. Click on the **Settings** tab (the gear icon).
3. Under the **Security** section in the left sidebar, click on **Secrets and variables** -> **Actions**.
4. Click the green **New repository secret** button.
5. Fill in the fields:
   - **Name**: `MY_SECRET_TOKEN`
   - **Secret**: `SuperSecret12345!Key` *(or any test secret token you choose)*
6. Click **Add secret**.

### Step 3: Trigger the Workflow
You can trigger the workflow in two ways:
* **Trigger via manual run** (Recommended):
  1. Go to the **Actions** tab on your GitHub repository page.
  2. In the left sidebar, click on the **GitHub Secrets Demo** workflow.
  3. Click the **Run workflow** dropdown on the right side and click the green **Run workflow** button.
* **Trigger via push**: Make any commit (e.g., editing this README) and push it to `main`.

### Step 4: Verify the Results
1. In the **Actions** tab, select the run that was just triggered.
2. Click on the **run-demo** job.
3. Expand the **Run Demo Script** step in the logs.
4. You will see:
   - `[+] Successfully loaded MY_SECRET_TOKEN from environment.`
   - `[+] Secret token length: 20 characters`
   - `[i] Printing secret directly: ***` *(Notice how GitHub automatically masked the secret token!)*
