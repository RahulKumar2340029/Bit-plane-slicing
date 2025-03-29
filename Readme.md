# Bit-Plane Slicing App 🎭 | Image Processing with OpenCV

🚀 **A web-based application that performs Bit-Plane Slicing on uploaded images using OpenCV and Streamlit.**

<!-- Add a GIF or Screenshot -->

## 📌 Features
- ✅ Upload any image (JPG, PNG, etc.)
- ✅ Process the image and extract **8 different bit planes**
- ✅ View the **original vs. processed images** side by side
- ✅ Download the processed bit-plane images

## 🖼️ What is Bit-Plane Slicing?
Bit-plane slicing is a technique in **image processing** where we extract specific bits from each pixel's intensity value to highlight fine details or noise.

**Example of Bit-Planes in an Image:**

| **Bit Plane** | **Effect** |
|---------------|------------|
| Plane 7 (MSB) | High contrast & major image structure |
| Plane 4       | Mid-level detail |
| Plane 0 (LSB) | Noise & fine textures |

## ⚡ Tech Stack
* **Frontend:** Streamlit
* **Backend:** OpenCV, NumPy, PIL
* **Deployment:** Streamlit Cloud

## 📥 Installation & Setup

**1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/bit-plane-slicing.git
cd bit-plane-slicing
## Bit-Plane Slicing App

### 🚀 Features
- Upload an image and extract bit-plane slices.
- View different levels of bit-plane representation.
- Download processed images for further analysis.

---

## 📥 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/RahulKumar2340029/Bit-plane-slicing.git
cd Bit-plane-slicing
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App
```bash
streamlit run app.py
```

---

## 📸 Usage
1. Open the app in your browser.
2. Click **Upload Image** and select a file.
3. The app will process the image and display **bit-plane slices**.
4. Download the processed images if needed.

---

## 🛠️ Deployment

### 🚀 Deploy on Streamlit Cloud
1. Push your code to **GitHub**.
2. Go to **Streamlit Cloud → New App**.
3. Select your **GitHub repo & branch**.
4. Set the main script as **app.py**.
5. Click **Deploy!** 🎉

---

## 🐛 Troubleshooting

If you get **ImportError: libGL.so.1 not found**, run:
```bash
sudo apt-get update && sudo apt-get install -y libgl1-mesa-glx
```

---

## 📌 Future Enhancements

- 🔹 Add **edge detection & segmentation** features.
- 🔹 Allow users to **adjust bit-plane levels dynamically**.
- 🔹 Deploy on **Hugging Face Spaces or AWS Lambda**.

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 🙌 Contributing
Pull requests are welcome! If you find a bug or want a new feature, feel free to **open an issue**.

---

## 📞 Contact

- 📧 **Email:** karnrahul786@gmail.com
- 🐙 **GitHub:** [RahulKumar2340029](https://github.com/RahulKumar2340029/)
- 🌐 **Live App:** [Streamlit App](https://bit-plane-slicing-rkrsuj.streamlit.app/)

