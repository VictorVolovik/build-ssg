clear
echo "Runnning static site generator..."
python3 src/main.py
echo "Access site at http://localhost:8888"
cd public && python3 -m http.server 8888
