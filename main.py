import streamlit as st
import os
import json
import base64
import io

# ----------- FUNCTIONS ------------

def display_notebook(notebook_path):
    """Read and display a Jupyter notebook file"""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook_content = json.load(f)
        
        st.markdown("## 📓 Notebook Contents")

        for i, cell in enumerate(notebook_content.get('cells', [])):
            cell_type = cell.get('cell_type', '')
            source = ''.join(cell.get('source', ''))

            if cell_type == 'markdown':
                st.markdown(f"### 📝 Markdown Cell {i+1}")
                st.markdown(source, unsafe_allow_html=True)
                st.markdown("---")

            elif cell_type == 'code':
                st.markdown(f"### 💻 Code Cell {i+1}")
                st.code(source, language='python')

                outputs = cell.get('outputs', [])
                if outputs:
                    st.markdown("**🔽 Output:**")
                    for output in outputs:
                        if output.get('output_type') == 'error':
                            st.error("⚠️ Error in Code Execution:")
                            st.text('\n'.join(output.get('traceback', [])))
                        elif 'text' in output:
                            st.text(''.join(output['text']))
                        elif 'data' in output:
                            data = output['data']
                            if 'text/plain' in data:
                                st.code(''.join(data['text/plain']), language='python')
                            if 'image/png' in data:
                                image_data = base64.b64decode(data['image/png'])
                                st.image(io.BytesIO(image_data))

                st.markdown("---")

    except Exception as e:
        st.error(f"Error loading notebook: {str(e)}")

def show_gradio_image(image_path):
    if os.path.exists(image_path):
        st.image(image_path, caption="Gradio UI Snapshot", use_column_width=True)
    else:
        st.warning("Gradio image not found!")

# ----------- UI STARTS HERE ------------

def main():
    st.set_page_config(
        page_title="Gemma Model Project",
        page_icon="🤖",
        layout="wide"
    )

    # Custom Styling
    st.markdown("""
    <style>
    .main-header {
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .sub-header {
        font-size: 28px;
        font-weight: bold;
        margin-top: 30px;
        margin-bottom: 15px;
    }
    .highlight {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title
    st.markdown('<div class="main-header">Gemma Language Model Project 🚀</div>', unsafe_allow_html=True)

    # Intro
    st.markdown("""
    Welcome to my implementation of **Google's Gemma language model**!  
    This app demonstrates how I fine-tuned the model, created a user interface with Gradio,  
    and deployed it on **Hugging Face Spaces** for the world to try!
    """)

    # Project Overview
    st.markdown('<div class="sub-header">📌 Project Overview</div>', unsafe_allow_html=True)
    st.markdown("""
    - ✅ Fine-tuned Gemma on custom dataset  
    - 🧠 Built an interactive UI using Gradio  
    - 🚀 Deployed on Hugging Face Spaces  
    - 💡 Optimized model performance and inference  
    """)

    # Notebook Display
    st.markdown('<div class="sub-header">📘 Gemma Notebook (Jupyter)</div>', unsafe_allow_html=True)
    notebook_path = "Gemma3_Hugging_Face.ipynb"
    if os.path.exists(notebook_path):
        display_notebook(notebook_path)
    else:
        st.error("Notebook file not found.")

    # Gradio UI Image
    st.markdown('<div class="sub-header">🎨 Gradio UI Snapshot</div>', unsafe_allow_html=True)
    show_gradio_image("Gradio.png")

    # Deployment Guide
    st.markdown('<div class="sub-header">🚀 How to Deploy on Hugging Face Spaces</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="highlight">
        <ol>
            <li><strong>Login to Hugging Face:</strong> Create an account at <a href='https://huggingface.co'>huggingface.co</a></li>
            <li><strong>Create a New Space:</strong> Choose <code>Gradio</code> as the SDK</li>
            <li><strong>Upload Files:</strong> Upload these:
                <ul>
                    <li><code>main.py</code> (this file)</li>
                    <li><code>requirements.txt</code></li>
                    <li><code>Gemma3_Hugging_Face.ipynb</code></li>
                    <li><code>Gradio.png</code> (optional, for UI demo)</li>
                </ul>
            </li>
            <li><strong>Set Python Environment:</strong> Hugging Face will auto-install from <code>requirements.txt</code></li>
            <li><strong>Deploy:</strong> Click on "Commit changes" and wait 1–2 mins for the space to go live!</li>
        </ol>
        <p>That's it! Your NLP app is now LIVE for the world 🌍</p>
    </div>
    """, unsafe_allow_html=True)

    # Outro
    st.markdown('<div class="sub-header">📫 Connect With Me</div>', unsafe_allow_html=True)
    st.markdown("""
    - 🧑‍💻 Made with ❤️ by a passionate ML engineer  
    - 💬 Always open to feedback, collabs, or mentorship  
    - 📧 Reach out on [LinkedIn](https://www.linkedin.com) or [GitHub](https://github.com)
    """)

if __name__ == "__main__":
    main()
