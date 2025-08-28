# 🔍 Advanced Bit Plane Slicing Analyzer

An **interactive web application** built with Streamlit that allows you to explore and analyze **bit plane slicing** of digital images. Extract individual bit planes, reconstruct images from selected planes, and gain insights into image structure at the bit level.

---

## ✨ Features

- 📸 **Image Upload**: Support for JPG, PNG, JPEG formats
- 🔬 **8-Bit Plane Extraction**: Visualize all 8 bit planes (LSB to MSB)
- 🔧 **Interactive Reconstruction**: Select and combine specific bit planes
- 📊 **Statistical Analysis**: Mean, standard deviation, and PSNR calculations
- 📈 **Histogram Visualization**: Grayscale intensity distribution
- ⚡ **Real-time Processing**: Instant results with interactive controls
- 💾 **Export Capability**: Download reconstructed images as PNG
- 🎨 **Contrast Enhancement**: Optional histogram equalization

---

## 🛠️ Tech Stack

- **Streamlit** - Interactive web application framework
- **OpenCV** - Image processing and computer vision
- **NumPy** - Numerical computations and array operations
- **Matplotlib** - Plotting and visualization
- **PIL (Pillow)** - Image handling and export functionality

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip package manager

### 1. Clone the repository
```bash
git clone <repository-url>
cd bit-plane-analyzer
```

### 2. Install dependencies
```bash
pip install streamlit opencv-python numpy matplotlib pillow
```

### 3. Run the application
```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

---

## 📖 How to Use

### Basic Workflow:
1. **Upload Image**: Click "Upload an Image" and select JPG/PNG/JPEG file
2. **View Original**: Original image displays in the left column
3. **Analyze Bit Planes**: All 8 bit planes are automatically extracted and displayed
4. **Select Planes**: Use sidebar to choose which bit planes to reconstruct
5. **View Results**: Reconstructed image appears in the right column
6. **Download**: Export reconstructed image as PNG

### Advanced Features:
- **Enhance Contrast**: Enable histogram equalization for better bit plane visibility
- **Show Histogram**: Display grayscale intensity distribution
- **Statistics**: View detailed image metrics including PSNR values
- **Interactive Selection**: Choose any combination of bit planes for reconstruction

---

## 🧮 Understanding Bit Plane Slicing

### What is Bit Plane Slicing?
Bit plane slicing decomposes an 8-bit grayscale image into 8 binary images, each representing one bit position:

- **Bit Plane 0 (LSB)**: Least significant bit - contains fine details and noise
- **Bit Plane 1-6**: Middle planes - contain varying levels of image information
- **Bit Plane 7 (MSB)**: Most significant bit - contains major image structure

### Mathematical Foundation:
For a pixel with intensity value `I`, bit plane `k` is extracted as:
```
Bit_Plane_k = (I >> k) & 1
```

Reconstruction combines selected planes:
```
Reconstructed = Σ(Bit_Plane_k × 2^k) for selected k
```

---

## 📊 Analysis Capabilities

### Image Statistics:
- **Dimensions**: Width × Height × Channels
- **Mean Intensity**: Average pixel value (0-255)
- **Standard Deviation**: Intensity variation measure
- **PSNR**: Peak Signal-to-Noise Ratio between original and reconstructed

### Visual Analysis:
- **Individual Bit Planes**: Binary representation of each bit level
- **Reconstructed Images**: Combination of selected bit planes
- **Histogram**: Pixel intensity distribution
- **Side-by-side Comparison**: Original vs. reconstructed images

---

## 📂 Project Structure

```
bit-plane-slicing/
│
├── app.py                   # Main Streamlit application
├── requirements.txt         # Python dependencies
├── package.txt
```

---

## 🎯 Use Cases

### Educational Applications:
- **Digital Image Processing Courses**: Demonstrate bit-level image representation
- **Computer Vision Learning**: Understand image data structure
- **Signal Processing**: Explore information content at different bit levels

### Research Applications:
- **Image Compression**: Analyze information distribution across bit planes
- **Steganography**: Study LSB manipulation for data hiding
- **Image Quality Assessment**: Compare reconstruction quality with different plane combinations

### Professional Applications:
- **Medical Imaging**: Analyze diagnostic image bit structure
- **Remote Sensing**: Process satellite/aerial imagery
- **Quality Control**: Industrial image analysis

---

## 📋 Requirements

```txt
streamlit==1.44.0
opencv-python==4.11.0.86
numpy==2.2.4
matplotlib==3.10.1
pillow==11.1.0
```

---

## 🔧 Configuration Options

### Sidebar Controls:
- **Enhance Contrast**: Applies histogram equalization to bit planes
- **Show Histogram**: Displays grayscale intensity distribution
- **Bit Plane Selection**: Multi-select for reconstruction (0-7)

### Display Settings:
- **Wide Layout**: Optimized for larger screens
- **Container Width**: Images scale to fit columns
- **Interactive Elements**: Real-time updates on selection changes

---

## 📈 Performance Notes

- **Memory Usage**: Proportional to image size × 8 bit planes
- **Processing Time**: Near-instantaneous for typical image sizes (<10MP)
- **Browser Compatibility**: Works with modern browsers supporting Streamlit
- **File Size Limits**: Default Streamlit limit (200MB), adjustable in config

---

## 🚀 Future Enhancements

### Planned Features:
- [ ] **Color Image Support**: RGB bit plane analysis
- [ ] **Multiple Image Comparison**: Side-by-side analysis
- [ ] **Advanced Metrics**: MSE, SSIM quality measures
- [ ] **Batch Processing**: Analyze multiple images simultaneously
- [ ] **Custom Bit Combinations**: Non-standard plane groupings

### Technical Improvements:
- [ ] **Performance Optimization**: Caching for large images
- [ ] **Mobile Responsiveness**: Better mobile interface
- [ ] **Export Options**: Multiple format support (TIFF, BMP)
- [ ] **Interactive Plots**: Plotly integration for better visualization

---

## 🐛 Known Limitations

- **Grayscale Only**: Currently processes images in grayscale
- **Memory Intensive**: Large images may consume significant RAM
- **Basic Export**: Only PNG format for downloads
- **No Undo/Redo**: Changes are immediate and irreversible

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/color-support`)
3. Make your changes and test thoroughly
4. Commit with clear messages (`git commit -m 'Add RGB bit plane support'`)
5. Push to your branch (`git push origin feature/color-support`)
6. Submit a Pull Request

---

## 📚 Educational Resources

### Bit Plane Slicing Theory:
- Digital Image Processing by Gonzalez & Woods
- Computer Vision: Algorithms and Applications by Szeliski

### Related Concepts:
- **Bit Manipulation**: Understanding binary operations
- **Image Compression**: JPEG, PNG compression techniques
- **Information Theory**: Data entropy and compression ratios

---

## 📜 License

MIT License © 2024

---

## 🙏 Acknowledgments

- **Streamlit Team** for the excellent web framework
- **OpenCV Community** for robust image processing tools
- **Digital Image Processing Community** for theoretical foundations

---

<div align="center">

**⭐ Star this repo if you find it useful for learning or research!**

*Perfect for students, researchers, and professionals in image processing*

[Report Bug](mailto:your-email@example.com) • [Request Feature](mailto:your-email@example.com) • [View Demo](#-how-to-use)

</div>
