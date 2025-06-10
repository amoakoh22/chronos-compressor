import streamlit as st
import os
import moviepy.editor as mp
import tempfile
import time # For simulating longer processes with st.spinner

# --- Configuration for a Futuristic Vibe ---
COMPRESSION_PRESETS = {
    "🚀 Quantum-Compressed (Smallest File)": "500k",
    "🌌 Nebula-Optimized (Balanced)": "1000k", # Default
    "🌟 Stellar-Quality (Larger File)": "2000k"
}

# --- Streamlit App Setup ---
st.set_page_config(
    page_title="Chronos-Compressor: Time-Bending Video Resizer",
    page_icon="🌌",
    layout="centered"
)

# --- Inject Custom CSS ---
# Load the custom CSS file and inject it into the Streamlit app
# This assumes style.css is in the same directory as app.py
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Header Section with Futuristic Flair ---
st.markdown(
    """
    <h1 class="futuristic-title">🌌 Chronos-Compressor 🚀</h1>
    <p class="futuristic-subtitle">Harnessing quantum algorithms to bend time and space for ultimate video optimization!</p>
    ---
    """,
    unsafe_allow_html=True
)

st.write("Initiate your video's temporal shift sequence:")

# --- File Uploader ---
uploaded_file = st.file_uploader(
    "Select a Temporal Data Stream (Video File)",
    type=["mp4", "mov", "avi", "mkv", "webm"],
    help="Supported formats: .mp4, .mov, .avi, .mkv, .webm. Maximum file size currently limited by universal bandwidth constraints."
)

if uploaded_file is not None:
    original_size_bytes = uploaded_file.size
    original_size_mb = original_size_bytes / (1024 * 1024)
    st.info(f"Detected inbound data stream: `{uploaded_file.name}` ({original_size_mb:.2f} MB)")

    # --- Engaging message during initial file upload/processing ---
    with st.spinner("🚀 Activating wormhole for data transfer..."):
        time.sleep(0.5) # Simulate slight network latency
        st.write("📡 Inbound data stream validation initiated...")
        time.sleep(0.5) # Simulate validation

    # Optional: show a preview of the uploaded video
    st.markdown("### Pre-Compression Aetherialization Preview:")
    st.video(uploaded_file)
    st.markdown("---")

    # --- User Options for Flexibility ---
    st.markdown("### Configure Temporal Compression Matrix:")
    selected_preset_label = st.selectbox(
        "Choose your compression intensity:",
        options=list(COMPRESSION_PRESETS.keys()),
        index=1, # Default to Balanced
        help="Quantum-Compressed for maximum space-saving, Stellar-Quality for minimal data loss."
    )
    compression_bitrate = COMPRESSION_PRESETS[selected_preset_label]

    st.warning("⚠️ Warning: Extreme compression may result in minor temporal distortions (quality loss).")

    # Create a temporary directory unique to this session
    with tempfile.TemporaryDirectory() as tmpdir:
        uploaded_file_path = os.path.join(tmpdir, uploaded_file.name)

        # Save the uploaded file to the temporary directory
        with open(uploaded_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(f"Data stream `{uploaded_file.name}` stabilized in temporary quantum buffer.")

        output_filename = f"chronos_optimized_{os.path.basename(uploaded_file.name)}"
        output_file_path = os.path.join(tmpdir, output_filename)

        st.markdown("### Initiating Compression Sequence...")
        
        # --- Dynamic Progress & Detailed Feedback during Compression ---
        status_message_container = st.empty() # Placeholder for changing status messages
        progress_bar_container = st.progress(0)

        try:
            current_progress = 0

            # Stage 1: Initializing Quantum Processors
            status_message_container.info("🌀 Engaging Chronos-Core processors... Standby for quantum computation.")
            current_progress += 10
            progress_bar_container.progress(current_progress)
            time.sleep(1) # Simulate complex initialization

            # Stage 2: Loading Data Stream
            status_message_container.info("🌌 Calibrating quantum video stream... Analyzing temporal data structure.")
            current_progress += 15
            progress_bar_container.progress(current_progress)
            time.sleep(1.5) # Simulate data stream analysis

            video_clip = mp.VideoFileClip(uploaded_file_path)
            
            # Stage 3: Applying Compression Algorithms
            status_message_container.info("🧬 Applying compression algorithms to data stream... Optimizing spacetime efficiency.")
            current_progress += 25
            progress_bar_container.progress(current_progress)
            # The actual write_videofile takes time, acting as the main "waiting" period
            video_clip.write_videofile(
                output_file_path,
                codec="libx264",
                bitrate=compression_bitrate,
                preset="medium",
                audio_codec="aac"
            )
            
            video_clip.close()

            # Stage 4: Finalizing & Verifying
            status_message_container.info("✔️ Verifying temporal integrity of optimized stream... Finalizing data packets.")
            current_progress = 90 # Jump close to end
            progress_bar_container.progress(current_progress)
            time.sleep(0.8) # Simulate finalization

            progress_bar_container.progress(100) # Complete progress
            status_message_container.success("✅ Compression sequence complete! Temporal data stream optimized.")
            
            # --- Calculate and Display Savings ---
            compressed_size_bytes = os.path.getsize(output_file_path)
            compressed_size_mb = compressed_size_bytes / (1024 * 1024)
            
            bytes_saved = original_size_bytes - compressed_size_bytes
            percentage_saved = (bytes_saved / original_size_bytes) * 100 if original_size_bytes > 0 else 0

            # Display notification using markdown for custom styling
            st.markdown(f"""
            <div class="save-notification">
                <h3>💾 Transmission Report: Compression Achieved!</h3>
                <p>Original Data Stream Size: <strong>{original_size_mb:.2f} MB</strong></p>
                <p>Optimized Data Stream Size: <strong>{compressed_size_mb:.2f} MB</strong></p>
                <p>Total Data Reduction: <strong>{bytes_saved / (1024 * 1024):.2f} MB</strong> (<strong>{percentage_saved:.1f}% saved!</strong>)</p>
                <p>Mission success! Your data is now ready for efficient interstellar travel.</p>
            </div>
            """, unsafe_allow_html=True)

            st.balloons() # Celebrate!

            # --- Download Button with Thematic Text ---
            st.markdown("### Download Your Optimized Temporal Data Stream:")
            with open(output_file_path, "rb") as f:
                st.download_button(
                    label="⬇️ Download Optimized Video File ⬇️",
                    data=f.read(),
                    file_name=output_filename,
                    mime="video/mp4" # Ensure correct MIME type
                )
            st.info("Your video is now ready for re-entry into the spacetime continuum.")

        except Exception as e:
            st.error(f"⚠️ Temporal anomaly detected: {e}")
            st.error("Protocol failure during compression. This could be due to corrupted data stream or an unforeseen spacetime distortion.")
            st.help("Ensure your original data stream is stable. If anomalies persist, contact Chronos-Compressor support.")
            st.stop() # Stop further execution if an error occurs

else:
    st.info("Awaiting inbound video data stream... Please upload a file to begin the compression sequence.")

# --- Footer with a Futuristic Touch ---
st.markdown("---")
st.markdown("🌐 Chronos-Compressor v1.0 | A product of StellarNet Dynamics Corporation | Ensuring efficient data transmission across all galaxies.")
st.markdown("<p style='font-size:0.8em; text-align:center;'>Powered by Streamlit and MoviePy's time-bending capabilities.</p>", unsafe_allow_html=True)