# 🤖 Local LLM Setup Guide

## Quick Setup (5 minutes)

### Step 1: Install Ollama

**Windows:**
1. Download from: https://ollama.ai/download/windows
2. Run the installer
3. Ollama will start automatically

**Mac:**
```bash
brew install ollama
```

**Linux:**
```bash
curl https://ollama.ai/install.sh | sh
```

---

### Step 2: Pull the Phi-3 Mini Model

Open a terminal and run:

```bash
ollama pull phi3
```

**Model Details:**
- **Size**: ~2.3GB
- **Parameters**: 3.8B
- **Speed**: Very fast (even on CPU)
- **Quality**: Excellent for this use case

**Alternative Models** (if you want to try others):
```bash
# Smaller, faster (2B params, ~1.4GB)
ollama pull gemma2:2b

# Slightly larger (3B params, ~1.9GB)  
ollama pull llama3.2

# Larger, more capable (7B params, ~4.7GB)
ollama pull llama3.2:7b
```

---

### Step 3: Verify Installation

Test that Ollama is working:

```bash
ollama list
```

You should see `phi3` in the list.

Test the model:

```bash
ollama run phi3 "Hello, how are you?"
```

---

### Step 4: Install Python Package

```bash
cd backend
pip install ollama
```

---

### Step 5: Restart the Backend

```bash
python main.py
```

You should see:
```
✅ Local LLM 'phi3' is ready!
```

---

## 🎯 How It Works

### Before (Rule-Based):
```python
if "attendance" in query:
    return f"Your attendance is {attendance}%"
```

### After (LLM-Based):
```python
llm.generate_response(
    user_query="What's my attendance?",
    user_data={"attendance": 85.5, "name": "Alice"},
    context_docs=["Attendance policy..."],
    role="student"
)
```

**LLM Response:**
> "Hi Alice! Your current attendance is 85.5%, which is great! You're well above the minimum 75% requirement. Keep up the good work! 📚"

---

## 🚀 Benefits

### ✅ Natural Conversations
- More human-like responses
- Better context understanding
- Handles complex queries

### ✅ Still Local & Private
- No API calls
- No internet required (after download)
- All data stays on your server

### ✅ Lightweight & Fast
- Phi-3 Mini: 3.8B parameters
- Runs on CPU (no GPU needed)
- ~200-500ms response time

### ✅ Smart Fallback
- If Ollama isn't installed, uses rule-based responses
- Graceful degradation
- No errors

---

## 📊 Model Comparison

| Model | Size | Params | Speed | Quality | Recommended |
|-------|------|--------|-------|---------|-------------|
| **phi3** | 2.3GB | 3.8B | ⚡⚡⚡ | ⭐⭐⭐⭐ | ✅ **Best** |
| gemma2:2b | 1.4GB | 2B | ⚡⚡⚡⚡ | ⭐⭐⭐ | For slower PCs |
| llama3.2 | 1.9GB | 3B | ⚡⚡⚡ | ⭐⭐⭐⭐ | Alternative |
| llama3.2:7b | 4.7GB | 7B | ⚡⚡ | ⭐⭐⭐⭐⭐ | If you have RAM |

---

## 🔧 Configuration

### Change Model

Edit `backend/llm_integration.py`:

```python
# Line 11
def __init__(self, model_name: str = "phi3"):  # Change to "gemma2:2b" or "llama3.2"
```

### Adjust Response Length

Edit `backend/llm_integration.py`:

```python
# Line 54
options={
    "temperature": 0.7,  # 0.0 = deterministic, 1.0 = creative
    "num_predict": 256,  # Max tokens (increase for longer responses)
}
```

---

## 🐛 Troubleshooting

### "Ollama not available"
- Install Ollama from https://ollama.ai
- Make sure it's running: `ollama list`

### "Model not found"
- Pull the model: `ollama pull phi3`
- Check available models: `ollama list`

### Slow responses
- Use a smaller model: `ollama pull gemma2:2b`
- Reduce `num_predict` in config
- Close other applications

### Out of memory
- Use gemma2:2b (smaller model)
- Close other applications
- Increase system swap space

---

## 📈 Performance Tips

### 1. **Keep Ollama Running**
Ollama runs as a background service. Don't close it.

### 2. **First Response is Slower**
The first query loads the model into memory (~5 seconds).
Subsequent queries are fast (~200-500ms).

### 3. **Concurrent Users**
Phi-3 can handle multiple users simultaneously on a decent CPU.

### 4. **GPU Acceleration** (Optional)
If you have an NVIDIA GPU:
- Ollama automatically uses it
- 10x faster responses
- Can use larger models

---

## 🎓 Example Queries

### Student Queries:
**Q:** "What's my attendance and how am I doing?"

**LLM Response:**
> "Your current attendance is 76.58%, which is good! You're just above the minimum 75% requirement. Try to maintain or improve this to stay eligible for final exams. Keep it up! 📚"

**Q:** "I'm worried about my CGPA"

**LLM Response:**
> "I can see your CGPA is 7.85, which is a solid B+ grade! That's actually quite good. If you're aiming higher, I'd recommend focusing on your weaker subjects and utilizing the free tutoring services at the Learning Center. Would you like some study tips?"

### Faculty Queries:
**Q:** "How many leave days can I take this month?"

**LLM Response:**
> "You currently have 15 days of paid leave remaining. According to the leave policy, you can take up to 10 consecutive days with one week's advance notice. Would you like me to explain the leave request process?"

---

## 🔄 Switching Back to Rule-Based

If you want to use the old system, edit `backend/main.py` line 669:

```python
# Comment out LLM
# llm = get_llm()
# response = llm.generate_response(...)

# Uncomment rule-based
response = generate_rule_based_response(
    request.message,
    personal_data,
    relevant_docs,
    user_data['role'],
    context
)
```

---

## 📚 Resources

- **Ollama**: https://ollama.ai
- **Phi-3**: https://ollama.ai/library/phi3
- **Model Library**: https://ollama.ai/library
- **Documentation**: https://github.com/ollama/ollama

---

**Ready to use! The system will automatically detect if Ollama is available and use it, otherwise it falls back to rule-based responses.** 🚀
