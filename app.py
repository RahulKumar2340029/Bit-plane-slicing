import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Function to perform Bit Plane Slicing
def bit_plane_slicing(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    bit_planes = []
    for i in range(8):
        bit_plane = (gray >> i) & 1
        bit_planes.append(bit_plane * 255)
    return gray, bit_planes

# Function to reconstruct image from selected bit planes
def reconstruct_image(bit_planes, selected_planes):
    reconstructed = np.zeros_like(bit_planes[0], dtype=np.uint8)
    for i in selected_planes:
        reconstructed += bit_planes[i] * (2 ** i)
    return reconstructed

# Main Streamlit app
def main():
    st.set_page_config(page_title="Advanced Bit Plane Analyzer", layout="wide")
    
    st.title("Advanced Bit Plane Slicing Analyzer")
    st.markdown("""
    Explore image bit planes with interactive controls and reconstruction capabilities.
    Upload an image to begin analysis.
    """)

    # Sidebar controls
    st.sidebar.header("Settings")
    enhance_contrast = st.sidebar.checkbox("Enhance Contrast", value=False)
    show_histogram = st.sidebar.checkbox("Show Histogram", value=False)
    
    # File uploader
    uploaded_file = st.file_uploader(
        "Upload an Image", 
        type=["jpg", "png", "jpeg"],
        help="Supported formats: JPG, PNG, JPEG"
    )

    if uploaded_file is not None:
        # Read and process image
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        
        # Convert for display
        display_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Columns for layout
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.image(display_image, caption="Original Image", use_container_width=True)
        
        # Get bit planes
        gray, bit_planes = bit_plane_slicing(image)
        
        # Bit plane selection for reconstruction
        st.sidebar.subheader("Image Reconstruction")
        selected_planes = st.sidebar.multiselect(
            "Select Bit Planes to Reconstruct",
            options=list(range(8)),
            default=[7]  # Default to MSB
        )
        
        # Process and display
        with st.container():
            st.subheader("Analysis Results")
            
            # Bit Planes Display
            st.write("### Bit Planes Visualization")
            cols = st.columns(4)
            for i in range(8):
                with cols[i % 4]:
                    plane = bit_planes[i]
                    if enhance_contrast:
                        plane = cv2.equalizeHist(plane)
                    st.image(
                        plane,
                        caption=f"Bit Plane {i}",
                        use_container_width=True,
                        clamp=True
                    )
            
            # Reconstructed Image
            if selected_planes:
                reconstructed = reconstruct_image(bit_planes, selected_planes)
                with col2:
                    st.image(
                        reconstructed,
                        caption=f"Reconstructed Image (Planes: {selected_planes})",
                        use_container_width=True
                    )
            
            # Histogram
            if show_histogram:
                st.write("### Histogram Analysis")
                fig, ax = plt.subplots(figsize=(8, 4))
                ax.hist(gray.ravel(), bins=256, range=(0, 255))
                ax.set_title("Grayscale Histogram")
                ax.set_xlabel("Pixel Value")
                ax.set_ylabel("Frequency")
                st.pyplot(fig)
        
        # Additional Analysis
        with st.expander("Detailed Statistics"):
            st.write("Image Statistics:")
            st.write(f"- Dimensions: {image.shape}")
            st.write(f"- Mean Intensity: {np.mean(gray):.2f}")
            st.write(f"- Standard Deviation: {np.std(gray):.2f}")
            
            if selected_planes:
                recon_mean = np.mean(reconstructed)
                st.write(f"- Reconstructed Mean: {recon_mean:.2f}")
                st.write(f"- PSNR (vs Original): {cv2.PSNR(gray, reconstructed):.2f} dB")

        # Download option
        st.sidebar.subheader("Export")
        if st.sidebar.button("Download Reconstructed Image"):
            pil_img = Image.fromarray(reconstructed)
            buf = BytesIO()
            pil_img.save(buf, format="PNG")
            byte_im = buf.getvalue()
            st.sidebar.download_button(
                label="Download",
                data=byte_im,
                file_name="reconstructed_image.png",
                mime="image/png"
            )

if __name__ == "__main__":
    main()