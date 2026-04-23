# climate-challenge-week0
python3 -m venv venv//venv install
sourse "venv/bin/activate"//activate the venv
# TASK 1 (git and github setape)
# 1. Create the branch
git checkout -b setup-task
# 2. Create .github/workflows/ci.yml
mkdir -p .github/workflows
# 3. Add your files, commit, push
git add .
git commit -m "init: setup venv and requirements"
git push origin task-1