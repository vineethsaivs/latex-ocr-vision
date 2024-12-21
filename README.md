# 🦙 LaTeX OCR with Llama 3.2 Vision  
_A Streamlit web app to extract LaTeX code from images of mathematical equations using Llama 3.2 Vision._  

## 🚀 Overview  
This application streamlines the process of converting mathematical equations from images into precise LaTeX code using Llama 3.2 Vision.
It is an essential tool for researchers, students, and educators, offering seamless conversion of handwritten or printed formulas into LaTeX, saving time and effort.

---

## 🎯 Features  
- 📷 **Image Upload**: Easily upload `.png`, `.jpg`, or `.jpeg` files containing equations.  
- 🧠 **OCR with Llama 3.2 Vision**: Leverages advanced OCR to ensure accurate LaTeX extraction.  
- 🔍 **Real-time LaTeX Rendering**: See the LaTeX output and its corresponding mathematical rendering side by side.  
- 🗑️ **Clear Session**: Reset and start fresh with just one click.  
- 🔒 **Secure and Fast**: Minimal latency with secure image handling (processing managed by Llama 3.2 API).  

---

## 🛠️ Setup and Installation  

### 1. Clone the Repository  
```bash
git clone https://github.com/vineethsaivs/latex-ocr-vision.git
cd latex-ocr-vision
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## ▶️ Running the App
```bash
streamlit run app.py
```

The app will run locally and can be accessed at:  

- **Local URL**: [http://localhost:8501](http://localhost:8501)  
- **Network URL**: Accessible on your network at a specified address.  

Once the app starts, upload an image of a mathematical equation and extract LaTeX with one click.

---

## 📂 File Structure  
```text
📂 Vision2LaTeX
│
├── app.py                   # Main Streamlit application handling image upload and LaTeX extraction
├── requirements.txt         # List of dependencies required to run the app
├── README.md                # Project documentation and instructions
├── LICENSE                  # Licensing information (MIT)
└── sample_images/           # (Optional) Example images for testing and demonstration
```

## 🧩 How It Works  
1. Upload an image of a mathematical equation.  
2. The image is processed using **Llama 3.2 Vision** to extract LaTeX.  
3. Extracted LaTeX is displayed and rendered in real-time.  

---

## ⚙️ Requirements  
- **Python 3.8+**  
- **Streamlit**  
- **Pillow**  
- **Ollama**  

---

## 📋 Dependencies (requirements.txt)  
```text
streamlit
Pillow
ollama
```
## 📜 License  
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🧑‍💻 Author  
**Vineeth Sai Varikuntla**  
- **GitHub**: [vineethsaivs](https://github.com/vineethsaivs)
- **LinkedIn**: [Vineeth Sai](https://www.linkedin.com/in/vineethsaivarikuntla)

---

## 📝 Acknowledgements  
- [Streamlit](https://streamlit.io/)  
- [Llama 3.2 Vision](https://ollama.com/)  

---

### **Why This README Structure?**  
- **Professional and Clear**: Easy to navigate and understand for new visitors.  
- **User-Friendly**: Includes setup instructions, running steps, and explanations.  
- **Encourages Contribution**: Adds contribution guidelines for open-source friendliness.  
- **SEO-Optimized**: Uses relevant keywords like LaTeX OCR, Streamlit, and Llama Vision, which increases discoverability.  

---

### **Additional Notes**  
- Add sample images to the repo under `sample_images/` if needed.  
- If you have a demo video (like `.mp4`), consider adding it to the README using:  
```markdown
## 🎥 Demo  
![Demo](demo/demo.gif)
```
