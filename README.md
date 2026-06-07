# 🚀 GemSphere AI

> **A Multi-Agent AI Assistant powered by Google Gemini 2.5 Flash**  
> Built with Streamlit · Supports 5 specialized agents · Multi-language responses · Export & TTS
 The application provides a ChatGPT-like experience while introducing specialized AI agents for different domains such as education, programming, business consulting, and research.

The platform combines an elegant dark-themed user interface with advanced AI capabilities, allowing users to interact naturally with intelligent agents, export conversations, generate reports, and listen to AI responses through integrated text-to-speech technology.

🎯 Project Objective

The goal of GemSphere AI is to create a single intelligent platform capable of handling multiple user needs through specialized AI agents. Instead of using one generic chatbot, users can switch between domain-specific agents optimized for different tasks.

The system improves productivity, learning, research, and problem-solving by providing tailored responses according to the selected agent.
---

## 📸 Preview

```
🚀 GemSphere AI
Powered by Gemini 2.5 Flash • Multi-Agent AI Assistant
```

---

## ✨ Features

- 🤖 **5 Specialized AI Agents** — General, Study, Coding, Business, Research
- 🌐 **Multi-language Support** — English, Hindi, Kannada, Tamil, Telugu (+ Auto Detect)
- 🔊 **Text-to-Speech** — Responses are read aloud using Google TTS
- 💬 **Typing Animation** — Smooth word-by-word response rendering
- 🧠 **Conversation Memory** — Retains the last 10 messages as context
- 📄 **Export to PDF** — Download the full chat as a formatted PDF
- 📥 **Download Report** — Export the chat as a plain `.txt` file
- 🗑 **Clear Chat** — Reset the conversation at any time

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| UI Framework | [Streamlit](https://streamlit.io/) |
| AI Model | [Google Gemini 2.5 Flash](https://deepmind.google/technologies/gemini/) |
| Google AI SDK | `google-genai` |
| PDF Export | `ReportLab` |
| Text-to-Speech | `gTTS` (Google Text-to-Speech) |
| Config | `python-dotenv` |

---

## 📁 Project Structure

```
gemsphere-ai/
├── app.py              # Main Streamlit application
├── .env                # API key (not committed)
├── .env.example        # Template for environment variables
├── requirements.txt    # Python dependencies
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/gemsphere-ai.git
cd gemsphere-ai
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_google_gemini_api_key_here
```

> 🔑 Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

### 5. Run the app

```bash
 https://gemsphere-ai-app.streamlit.app/
```

Open your browser at `http://localhost:8501`

---
video link:https://drive.google.com/file/d/1LNAiJA_o3dKT5Q5cOHe7Y_eCKb8NsRfh/view?usp=sharing
## 📦 Requirements

Create a `requirements.txt` with the following:

streamlit
google-genai
python-dotenv
pillow
pypdf
streamlit-mic-recorder
gtts

```

---

## 🤖 Agent Descriptions

| Agent | Role |
|---|---|
| **General AI** | All-purpose helpful assistant |
| **Study Agent** | Expert teacher — explains concepts with examples |
| **Coding Agent** | Senior software engineer — writes clean, explained code |
| **Business Agent** | Startup consultant — business plans and practical advice |
| **Research Agent** | Research specialist — detailed reports and analysis |

---

## 📤 Export Options

| Format | Description |
|---|---|
| 📄 PDF | Formatted chat export using ReportLab |
| 📥 TXT Report | Plain text version of the full conversation |

---

## 🌍 Supported Languages

- Auto Detect
- English
- Hindi
- Kannada
- Tamil
- Telugu

---

## 📌 Environment Variables

| Variable | Description | Required |
|---|---|---|
| `GEMINI_API_KEY` | Your Google Gemini API key | ✅ Yes |

---

## 🚧 Known Limitations

- TTS may silently fail on long responses or network issues (handled gracefully)
- Conversation context is limited to the last 10 messages
- PDF export does not support markdown formatting in message content

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

1. Fork the project
2. Create your feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a pull request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author
 
 chinmayi.P
Built with ❤️ using Streamlit and Google Gemini.

| | |
|---|---|
| **Name** | Chinmayi.P |
| **Email** | lakshmijyothi663@gmail.com|
| **GitHub** | [@chinmayi1012](https://github.com/chinmayi1012) |
| **Deployment link**|https://gemsphere-ai-app.streamlit.app/  |
|**video link** | https://drive.google.com/file/d/1LNAiJA_o3dKT5Q5cOHe7Y_eCKb8NsRfh/view?usp=sharing |

---
Your code is a **Multi-Agent AI Assistant built with Streamlit and Google Gemini 2.5 Flash**. Here's a detailed project description you can use for GitHub, competitions, hackathons, or resumes.

# 🚀 GemSphere AI – Multi-Agent Intelligent Assistant

GemSphere AI is a modern AI-powered conversational platform developed using Python, Streamlit, and Google Gemini 2.5 Flash. The application provides a ChatGPT-like experience while introducing specialized AI agents for different domains such as education, programming, business consulting, and research.

The platform combines an elegant dark-themed user interface with advanced AI capabilities, allowing users to interact naturally with intelligent agents, export conversations, generate reports, and listen to AI responses through integrated text-to-speech technology.

---

## 🎯 Project Objective

The goal of GemSphere AI is to create a single intelligent platform capable of handling multiple user needs through specialized AI agents. Instead of using one generic chatbot, users can switch between domain-specific agents optimized for different tasks.

The system improves productivity, learning, research, and problem-solving by providing tailored responses according to the selected agent.

---

## ✨ Core Features

### 🤖 Multi-Agent Architecture

GemSphere AI includes five intelligent agents:

#### General AI Agent

* Handles everyday conversations
* Answers general knowledge questions
* Assists with productivity and information retrieval

#### Study Agent

* Acts as a virtual teacher
* Explains concepts clearly
* Provides examples and educational guidance
* Supports academic learning

#### Coding Agent

* Functions as a software engineering assistant
* Generates code snippets
* Explains programming concepts
* Helps debug applications
* Supports multiple programming languages

#### Business Agent

* Provides startup and entrepreneurship guidance
* Creates business plans
* Suggests growth strategies
* Helps with business decision-making

#### Research Agent

* Generates detailed reports
* Assists in information gathering
* Conducts topic exploration
* Supports academic and professional research

---

## 🌍 Multilingual AI Support

Users can receive responses in multiple languages:

* English
* Hindi
* Kannada
* Tamil
* Telugu
* Auto Detection Mode

The selected language is dynamically injected into the AI system prompt, ensuring language-specific responses.

---

## 💬 Conversational Interface

The application provides a modern chat-based interface featuring:

* Real-time messaging
* ChatGPT-style conversation layout
* Session-based memory
* Smooth user experience
* Professional UI design
* Dark mode interface

---

## ⚡ Typing Animation

To create a more natural conversational experience, AI responses are displayed using a typing animation effect.

Benefits:

* Simulates human-like interaction
* Improves engagement
* Creates a premium chatbot experience

---

## 🔊 Text-to-Speech Integration

GemSphere AI automatically converts AI-generated responses into audio using Google Text-to-Speech (gTTS).

Features:

* Audio playback of responses
* Accessibility enhancement
* Hands-free learning experience
* Better user engagement

---

## 📄 PDF Export Functionality

Users can export complete chat conversations as PDF documents.

The PDF export includes:

* User messages
* AI responses
* Structured formatting
* Shareable conversation history

This feature is implemented using ReportLab.

---

## 📥 Report Generation

The application can generate downloadable text reports containing:

* Complete conversation logs
* User inputs
* AI outputs
* Session records

Useful for:

* Research documentation
* Meeting notes
* Academic references
* Knowledge management

---

## 📊 Sidebar Control Center

The sidebar acts as a central dashboard where users can:

* Select AI agents
* Choose response language
* View message count
* Export conversations
* Download reports
* Clear chat history

This improves usability and provides quick access to key application features.

---

## 🎨 User Interface Design

The application uses custom CSS styling to create a modern appearance.

### Design Highlights

* Dark Theme (#0e1117)
* Rounded chat containers
* Professional typography
* Responsive layout
* Streamlined user experience

The interface is optimized for:

* Students
* Developers
* Researchers
* Entrepreneurs
* Professionals

---

## 🏗️ System Architecture

### Frontend

* Streamlit

### AI Model

* Google Gemini 2.5 Flash

### Backend

* Python

### Supporting Libraries

#### google-genai

Provides access to Gemini AI models.

#### python-dotenv

Loads environment variables securely.

#### ReportLab

Generates PDF exports.

#### gTTS

Converts text into speech.

#### tempfile

Creates temporary audio files.

#### io.BytesIO

Handles in-memory file generation.

---

## 🔐 Security Implementation

API keys are securely managed through environment variables.

Benefits:

* Prevents hardcoding credentials
* Improves application security
* Simplifies deployment

Example:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## 📂 Project Workflow

### Step 1

User enters a prompt.

### Step 2

Selected AI Agent determines behavior.

### Step 3

Language preference is applied.

### Step 4

Recent conversation history is collected.

### Step 5

Prompt is sent to Gemini 2.5 Flash.

### Step 6

Response is generated.

### Step 7

Typing animation displays response.

### Step 8

Audio version is generated.

### Step 9

Conversation is stored in session memory.

### Step 10

User can export PDF or reports.

---

## 🎓 Educational Value

GemSphere AI demonstrates:

* Prompt Engineering
* Large Language Model Integration
* Streamlit Development
* AI Product Design
* Session Management
* PDF Generation
* Text-to-Speech Systems
* Multi-Agent AI Architecture
* UI/UX Design

---

## 🚀 Future Enhancements

Potential upgrades include:

* Long-term memory system
* Voice input support
* Image understanding
* Document analysis
* Database integration
* User authentication
* Team collaboration features
* Cloud deployment
* AI workflow automation
* Mobile application version

---
video link: https://drive.google.com/file/d/1LNAiJA_o3dKT5Q5cOHe7Y_eCKb8NsRfh/view?usp=sharing
## 🌟 Conclusion

GemSphere AI is a comprehensive multi-agent AI platform that combines intelligent conversation, multilingual support, speech synthesis, PDF reporting, and domain-specific expertise into a single application. It demonstrates how modern AI technologies can be integrated into a user-friendly platform to assist students, developers, researchers, entrepreneurs, and professionals in their daily tasks.

**Tagline:**
*"One Platform. Multiple AI Experts. Unlimited Possibilities."* 🚀🤖

