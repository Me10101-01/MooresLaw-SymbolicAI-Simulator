#!/bin/bash

# Step 1: Set your authtoken
echo "🔐 Adding ngrok authtoken..."
ngrok config add-authtoken 2xfPuAVygE5Dyz6YLUF5gRKQmGj_4QXzXSgs5fr3AvbW91hec

# Step 2: Start ngrok tunnel in background
echo "🌐 Launching ngrok on port 8501..."
(ngrok http 8501 > ngrok_output.log &)  # Run in background

# Step 3: Wait a moment for tunnel to establish
sleep 3

# Step 4: Grab the public HTTPS link from API (works in ngrok v3+)
PUBLIC_URL=$(curl -s http://127.0.0.1:4040/api/tunnels | grep -o 'https://[a-zA-Z0-9.-]*\.ngrok\.io' | head -n 1)

if [[ -z "$PUBLIC_URL" ]]; then
  echo "❌ Unable to fetch ngrok URL. Is ngrok running?"
  exit 1
fi

echo "✅ ngrok is running at: $PUBLIC_URL"

# Step 5: Append to README if not already there
if ! grep -q "$PUBLIC_URL" README.md; then
  echo -e "\n## 🌍 Public App Link\n\n🔗 [Launch Moore’s Law AI Visualizer]($PUBLIC_URL)\n" >> README.md
  echo "📄 Public link added to README.md"
else
  echo "ℹ️ Link already exists in README.md"
fi

# Step 6: Show final summary
echo -e "\n🧠 Ready! Your AI visualizer is live at:\n$PUBLIC_URL\n"
