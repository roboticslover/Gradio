# main.py
import streamlit as st
import os
import json
import base64
from pathlib import Path

def display_notebook(notebook_path):
    """Read and display a Jupyter notebook file"""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook_content = json.load(f)
        
        st.markdown("## Notebook Contents")
        
        # Display each cell
        for i, cell in enumerate(notebook_content.get('cells', [])):
            # Get cell type and source
            cell_type = cell.get('cell_type', '')
            source = ''.join(cell.get('source', ''))
            
            # Display markdown cells directly
            if cell_type == 'markdown':
                st.markdown(f"### Markdown Cell {i+1}")
                st.markdown(source)
                st.markdown("---")
            
            # Display code cells with syntax highlighting
            elif cell_type == 'code':
                st.markdown(f"### Code Cell {i+1}")
                st.code(source, language='python')
                
                # Display outputs if they exist
                outputs = cell.get('outputs', [])
                if outputs:
                    st.markdown("**Output:**")
                    for output in outputs:
                        if 'text' in output:
                            st.text(''.join(output['text']))
                        elif 'data' in output:
                            data = output['data']
                            if 'text/plain' in data:
                                st.code(''.join(data['text/plain']), language='python')
                            if 'image/png' in data:
                                image_data = data['image/png']
                                st.image(f"data:image/png;base64,{image_data}")
                
                st.markdown("---")
            
    except Exception as e:
        st.error(f"Error loading notebook: {str(e)}")
        st.info("Please make sure the notebook file is in the same directory as this app.")

def get_download_link(file_path):
    """Generate a download link for a file"""
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        filename = os.path.basename(file_path)
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="{filename}">Download {filename}</a>'
        return href
    except Exception as e:
        return f"Error generating download link: {str(e)}"

def main():
    st.set_page_config(
        page_title="Gemma Model Project",
        page_icon="🤖",
        layout="wide"
    )

    # Custom CSS for better styling
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
    .section {
        padding: 20px 0;
    }
    .highlight {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header Section
    st.markdown('<div class="main-header">Gemma Language Model Implementation</div>', unsafe_allow_html=True)
    
    st.markdown("""
    This project demonstrates my implementation of Google's Gemma language model for 
    natural language processing tasks. While the full model can't be deployed permanently due to resource constraints,
    this portfolio showcases the development process, implementation details, and results.
    """)

    # Project Overview
    st.markdown('<div class="sub-header">Project Overview</div>', unsafe_allow_html=True)
    st.markdown("""
    The Gemma model is a state-of-the-art language model developed by Google that excels at various NLP tasks.
    This project demonstrates how I:
    
    - Fine-tuned the model for specific use cases
    - Built a user-friendly interface using Gradio
    - Evaluated performance and optimized for better results
    - Addressed deployment challenges with resource-intensive models
    """)

    # Implementation Details
    st.markdown('<div class="sub-header">Implementation Details</div>', unsafe_allow_html=True)
    
    st.markdown("""
    The implementation uses Google's Gemma model, which requires significant computational resources.
    The model was set up in Google Colab with GPU acceleration to handle the resource requirements.
    
    Key components:
    - Model initialization and configuration
    - Custom preprocessing pipeline
    - Integration with Gradio for the user interface
    - Optimization techniques for improved performance
    """)

    # Demonstration Section
    st.markdown('<div class="sub-header">Model Demonstration</div>', unsafe_allow_html=True)
    st.markdown("""
    Below is a screenshot of the working application deployed on Gradio. 
    The temporary Gradio deployment was active for 72 hours for testing and demonstration purposes.
    """)

    # Display model interface screenshot
    if os.path.exists("Gradio.png"):
        st.image("Gradio.png", caption="Gemma Model Gradio Interface", use_container_width=True)
    else:
        st.error("Gradio.png file not found. Please make sure it's in the same directory as main.py")

    # Notebook Section
    st.markdown('<div class="sub-header">Project Notebook</div>', unsafe_allow_html=True)
    st.markdown("""
    The complete implementation details are available in my Jupyter notebook.
    You can explore the notebook content below and download it for further reference.
    """)

    # Display notebook content
    notebook_path = "Gemma3_Hugging_Face.ipynb"
    if os.path.exists(notebook_path):
        # Provide download button
        st.markdown(get_download_link(notebook_path), unsafe_allow_html=True)
        
        # Use tabs instead of nested expanders
        tab1, tab2 = st.tabs(["Notebook Overview", "Full Notebook Content"])
        
        with tab1:
            st.markdown("""
            This notebook contains a complete implementation of the Google Gemma model using Hugging Face's transformers library.
            It includes:
            
            - Model setup and initialization
            - Tokenizer configuration
            - Inference pipeline
            - Gradio interface implementation
            - Performance evaluation
            
            Switch to the "Full Notebook Content" tab to explore the complete code and implementation details.
            """)
        
        with tab2:
            display_notebook(notebook_path)
    else:
        st.error(f"{notebook_path} not found. Please make sure it's in the same directory as main.py")

    # Deployment Challenges
    st.markdown('<div class="sub-header">Deployment Challenges</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="highlight">', unsafe_allow_html=True)
    st.markdown("""
    ### Why Full Deployment Wasn't Possible
    
    The Gemma model faces several deployment challenges that are common in large language model projects:
    
    1. **Resource Requirements**: The model requires significant GPU memory and computational power, making it expensive to host continuously.
    
    2. **Gradio's 72-Hour Limit**: Free Gradio deployments are limited to 72 hours, which doesn't allow for permanent hosting.
    
    3. **Cost Constraints**: Maintaining a dedicated GPU instance for continuous deployment would incur substantial monthly costs.
    
    4. **Alternative Solutions**: This portfolio approach allows me to showcase the project's capabilities while acknowledging practical constraints.
    
    These challenges represent real-world considerations in ML engineering that professionals regularly navigate.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Future Improvements
    st.markdown('<div class="sub-header">Future Improvements & Full Deployment Plan</div>', unsafe_allow_html=True)
    st.markdown("""
    With additional resources, I would implement the following improvements:
    
    - Optimize the model for reduced memory footprint using quantization techniques
    - Deploy on a dedicated cloud instance with GPU support
    - Implement caching and batching for more efficient inference
    - Create a more robust API with authentication and usage tracking
    
    The ideal deployment would use a service like AWS SageMaker, Google Cloud AI Platform, or a dedicated 
    virtual machine with sufficient GPU capabilities.
    """)

    # Contact Information
    st.markdown('<div class="sub-header">Contact & Additional Information</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        For more information about this project or to discuss how I approach machine learning challenges:
        
        - GitHub: [P-256](https://github.com/roboticslover)
        - LinkedIn: [Sachin Rathore](https://www.linkedin.com/in/sachin-rathore-97776a283/)
        """)
    
    with col2:
        st.markdown("""
        **Technologies Used:**
        - Python
        - PyTorch
        - Hugging Face Transformers
        - Google Colab
        - Gemma Model
        - Gradio
        - Streamlit
        """)

if __name__ == "__main__":
    main()