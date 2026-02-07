# Using Ollama with LangChain Academy

This branch has been modified to use **Ollama** instead of OpenAI, allowing you to run all the LangChain Academy notebooks with local LLMs.

## Benefits

- ✅ **No API costs** - Run models completely free
- ✅ **Complete privacy** - Your data never leaves your machine
- ✅ **No API keys required** - No signup or authentication needed (except TAVILY for web search)
- ✅ **Works offline** - No internet connection required once models are downloaded

## Prerequisites

1. **Install Ollama**: Download from [https://ollama.ai](https://ollama.ai)
2. **Pull the correct model**: 
   ```bash
   ollama pull llama3.1
   ```

## ⚠️ IMPORTANT: Tool Calling Support

**Most notebooks in this course use tool calling (function calling), which requires specific models.**

### Models that Support Tool Calling:
- ✅ **llama3.1** (8B, 70B, or 405B) - **RECOMMENDED**
- ✅ **llama3.2** (1B or 3B)
- ✅ **mistral**
- ✅ **mixtral**
- ✅ **qwen2.5**

### Models that DO NOT Support Tool Calling:
- ❌ **llama3** - This will cause errors!

### Common Error

If you see this error:
```
ResponseError: registry.ollama.ai/library/llama3:latest does not support tools (status code: 400)
```

**Solution:** You need to use `llama3.1` instead:
```bash
ollama pull llama3.1
```

Then restart your notebook kernel.

## Available Models on Your System

You currently have these models installed:
- `llama3:latest` (4.7 GB) - **Recommended for this course**
- `gemma3:latest` (3.3 GB)
- `devstral:latest` (14 GB)
- `deepseek-r1:latest` (5.2 GB)

## Quick Start

1. **Verify Ollama is running**:
   ```bash
   ollama list
   ```

2. **Activate your environment**:
   ```bash
   source lc-academy-env/bin/activate
   ```

3. **Install additional dependencies**:
   ```bash
   pip install langchain-ollama
   ```

4. **Run the notebooks**: The notebooks have been modified to use `ChatOllama` instead of `ChatOpenAI`

## What Changed

### In `module-0/basics.ipynb`:
- Replaced `langchain-openai` with `langchain-ollama`
- Updated model initialization to use `ChatOllama`
- Removed OpenAI API key requirements
- Added Ollama availability checks
- Set default model to `llama3:latest`

### In `requirements.txt`:
- Added `langchain-ollama` package

## Switching Models

To use a different model in any notebook, simply change the model parameter:

```python
from langchain_ollama import ChatOllama

# Use any model you have installed
chat_model = ChatOllama(model="gemma3:latest", temperature=0)
# or
chat_model = ChatOllama(model="deepseek-r1:latest", temperature=0)
```

## Pulling Additional Models

```bash
# Popular models for this course
ollama pull llama3.2        # Latest Llama (smaller, faster)
ollama pull mistral         # Fast and efficient
ollama pull codellama       # Optimized for coding
ollama pull llama3.1:70b    # More capable (requires more RAM)
```

## Performance Tips

- **RAM**: Larger models require more RAM (8GB+ recommended)
- **Speed**: Smaller models (3B-8B parameters) are faster
- **Quality**: Larger models (70B+) give better results but are slower
- **Temperature**: Use 0 for consistent outputs, higher values for creativity

## Troubleshooting

### "Ollama not found"
- Make sure Ollama is installed and in your PATH
- Restart your terminal after installation

### "Model not found"
- Pull the model: `ollama pull llama3`
- Check available models: `ollama list`

### Slow performance
- Try a smaller model like `llama3.2` or `mistral`
- Close other applications to free up RAM

### Connection errors
- Ensure Ollama service is running
- Check `http://localhost:11434` in your browser

## Additional Resources

- [Ollama Documentation](https://github.com/ollama/ollama)
- [Ollama Model Library](https://ollama.ai/library)
- [LangChain Ollama Integration](https://python.langchain.com/docs/integrations/chat/ollama)

## Notes for Other Modules

The same pattern can be applied to other modules:
1. Replace `ChatOpenAI` imports with `ChatOllama`
2. Update model initialization
3. Remove API key requirements

For studio deployments in each module, you'll need to update the respective files in the `studio/` folders following the same pattern.
