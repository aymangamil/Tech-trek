import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from streamlit_option_menu import option_menu
import base64
from datetime import datetime

st.set_page_config(
    page_title="Tech Trek AI Academy",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_local_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

try:
    logo_image = load_local_image("Screenshot 2025-06-16 042217.png")
    data_science_image = load_local_image("Screenshot 2025-06-16 041008.png")
except:
    logo_image = ""
    data_science_image = ""

def local_css():
    st.markdown(f"""
    <style>
    /* Tech Trek Theme */
    :root {{
        --primary: #FF2E2E;       /* Vibrant red */
        --primary-dark: #CC0000;
        --primary-light: #FF9999;
        --secondary: #000000;     /* Black */
        --secondary-light: #333333;
        --dark: black;            /* Dark background */
        --light: #F0F0F0;        /* Light text */
        --text: #FFFFFF;         /* Main text */
        --text-light: #CCCCCC;   /* Secondary text */
        --accent: #FF2E2E;       /* Highlight color */
        --menu-bg: #1a1a1a;      /* New menu background color */
        --menu-text: #e6e6e6;    /* New menu text color */
        --menu-hover: #333333;   /* New menu hover color */
    }}

    /* Logo Animation */
    .logo-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        animation: fadeLogo 6s infinite ease-in-out;
        padding: 20px;
        border-radius: 20px;
        background: black;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        margin-top: 30px;
    }}

    .logo-container img {{
        height: 120px;
        filter: drop-shadow(0px 0px 8px rgba(0, 0, 0, 0.3));
        transition: transform 0.5s ease;
    }}

    .logo-container:hover img {{
        transform: scale(1.05);
    }}

    @keyframes fadeLogo {{
        0%, 100% {{
            opacity: 0;
            transform: translateY(-20px);
        }}
        50% {{
            opacity: 1;
            transform: translateY(0px);
        }}
    }}

    /* Certificate Styles */
    .certificate-container {{
        background: linear-gradient(135deg, #000000 0%, #1a1a1a 100%);
        border: 3px solid var(--primary);
        border-radius: 15px;
        padding: 3rem;
        text-align: center;
        margin: 2rem auto;
        max-width: 900px;
        position: relative;
        overflow: hidden;
        box-shadow: 0 0 30px rgba(255, 46, 46, 0.5);
    }}

    .certificate-container::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url("data:image/svg+xml,%3Csvg width='100' height='100' viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M11 18c3.866 0 7-3.134 7-7s-3.134-7-7-7-7 3.134-7 7 3.134 7 7 7zm48 25c3.866 0 7-3.134 7-7s-3.134-7-7-7-7 3.134-7 7 3.134 7 7 7zm-43-7c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zm63 31c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zM34 90c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zm56-76c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zM12 60c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2z' fill='%23ff2e2e' fill-opacity='0.05' fill-rule='evenodd'/%3E%3C/svg%3E");
        opacity: 0.3;
    }}

    /* باقي أنماط CSS */
    .stApp {{
        background-color: black;
        color: var(--text);
        font-family: 'Orbitron', 'Roboto', sans-serif;
        background: linear-gradient(rgba(10, 10, 10, 0.95), rgba(10, 10, 10, 0.95));
    }}

    .main-container {{
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
    }}

    .header-tech {{
        color: var(--primary);
        text-shadow: 0 0 10px rgba(255, 46, 46, 0.7);
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 2px;
        position: relative;
        padding-bottom: 1rem;
        margin-bottom: 2rem;
        border-bottom: 2px solid var(--primary);
    }}

    .tech-card {{
        background: rgba(20, 20, 20, 0.8);
        border-radius: 12px;
        border: 1px solid var(--primary);
        padding: 2rem;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        margin-bottom: 2rem;
        box-shadow: 0 10px 20px rgba(255, 46, 46, 0.1);
    }}

    .tech-card:hover {{
        transform: translateY(-10px);
        box-shadow: 0 15px 30px rgba(255, 46, 46, 0.3);
    }}

    /* New Menu Styles */
    .st-emotion-cache-1avcm0n {{
        background-color: var(--menu-bg) !important;
        border-bottom: 1px solid var(--primary) !important;
    }}
    
    .st-emotion-cache-1avcm0n .st-emotion-cache-1avcm0n {{
        border-bottom: none !important;
    }}
    
    /* باقي أنماط CSS... */
    </style>
    """, unsafe_allow_html=True)

# صور التطبيق
tech_images = {
    "ai_dashboard": 'https://png.pngtree.com/thumb_back/fw800/background/20230525/pngtree-futuristic-robot-is-standing-near-a-red-background-image_2630357.jpg',
    "machine_learning": 'https://i.pinimg.com/736x/5e/4f/a6/5e4fa683fa82a799f56708ea94cb9c7e.jpg',
    "deep_learning": "https://i.pinimg.com/736x/7e/99/7d/7e997d9128386adc614922ce4db5f04a.jpg",
    "neural_network": 'https://i.pinimg.com/736x/89/0a/66/890a66f5910d8554f309a8fbeed5c6fc.jpg',
    "big_data": 'https://i.pinimg.com/736x/19/6f/74/196f747810acb88bb8db73df2d704d26.jpg',
    "instructor1": "https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e",
    "instructor2": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d",
    "instructor3": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2"
}

local_css()

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Roboto:wght@300;400;500&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

st.markdown(f"""
    <div class="logo-container">
        <img src="data:image/png;base64,{logo_image}" alt="Tech Trek Logo">
    </div>
""", unsafe_allow_html=True)

selected = option_menu(
    menu_title=None,
    options=["🏠 Home", "📊 Data Analysis", "🧠 ML", "🕸️ Deep Learning"],
    icons=["house", "bar-chart", "cpu", "diagram-3"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {
            "padding": "0!important",
            "background-color": "var(--menu-bg)",
            "border-bottom": "1px solid var(--primary)"
        },
        "icon": {"color": "var(--primary)", "font-size": "18px"},
        "nav-link": {
            "font-family": "'Orbitron', sans-serif",
            "font-size": "16px",
            "text-align": "center",
            "margin": "0 auto",
            "padding": "12px 20px",
            "color": "var(--menu-text)",
            "border-radius": "0px",
            "transition": "all 0.3s ease",
            "border-bottom": "2px solid transparent"
        },
        "nav-link-selected": {
            "background-color": "transparent",
            "color": "var(--primary)",
            "font-weight": "bold",
            "border-bottom": "2px solid var(--primary)"
        },
        "nav-link:hover": {
            "background-color": "var(--menu-hover)",
            "color": "var(--primary-light)",
            "border-bottom": "2px solid var(--primary-light)"
        }
    }
)

# المحتوى الرئيسي
with st.container():
    if selected == "🏠 Home":
        st.markdown("""
        <div style="margin-top: -1rem; text-align: center;">
            <h1 class="header-tech">TECH TREK AI ACADEMY</h1>
            <h2 style="color: var(--primary-light); font-size: 1.8rem; font-family: 'Orbitron', sans-serif;">Master Cutting-Edge AI Technologies</h2>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([3, 2])
        with col1:
            st.markdown("""
            <div class="tech-card">
                <h3 style="color: var(--primary);">🚀 Intensive AI Training Programs</h3>
                <p style="font-size: 1.1rem; line-height: 1.6;">From fundamentals to deploying AI models in production. Gain cutting-edge skills with our project-based curriculum.</p>
                <div class="laser-beam" style="width: 100%; left: 0; bottom: 10px;"></div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin: 2rem 0;">
                <div class="tech-card">
                    <h4>📊 Data Analysis</h4>
                    <p>Master data analysis and visualization</p>
                </div>
                <div class="tech-card">
                    <h4>🧠 Deep Learning</h4>
                    <p>Empower your tasks with the power of AI</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin: 2rem 0;">
                <div class="tech-card">
                    <h4>🤖 Machine Learning</h4>
                    <p>Learn And Deploy Real Applications</p>
                </div>
                <div class="tech-card">
                    <div class="icon"></div>
                    <h4>Real Projects</h4>
                    <p>Build practical AI solutions that solve real-world problems and make an impact.</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div style="position: relative; width: 100%; height: 400px; margin: 2rem 0; border-radius: 12px; overflow: hidden;" class="hover-zoom">
                <img src="{tech_images['ai_dashboard']}" style="width: 100%; height: 100%; object-fit: cover;">
                <div class="laser-beam" style="width: 80%; left: 10%; top: 50%;"></div>
            </div>
            """, unsafe_allow_html=True)

    elif selected == "📊 Data Analysis":
        st.markdown("""
        <div style="text-align: center;">
            <h1 class="header-tech">DATA ANALYSIS TRACK</h1>
            <p style="font-size: 1.1rem; color: var(--primary-light);">Master the art of data analysis</p>
        </div>
        """, unsafe_allow_html=True)
        
        tab1, tab2, tab3 = st.tabs(["📋 Foundations", "🧹 Data Wrangling", "📈 Visualization"])
        
        with tab1:
            col1, col2 = st.columns([2, 3])
            with col1:
                st.markdown("""
                <div class="tech-card">
                    <h3 style="color: var(--primary);">Core Concepts</h3>
                    <ul style="padding-left: 1.5rem; list-style-type: none;">
                        <li>• Python for Data Analysis</li>
                        <li>• Pandas & NumPy</li>
                        <li>• Data preprocessing</li>
                        <li>• Exploratory Analysis</li>
                        <li>• Statistical Methods</li>
                        <li>• SQL</li>
                        <li>• Excel</li>
                        <li>• Power Bi</li> 
                        <li>• Dash</li>      
                    </ul>
                    <div class="laser-beam" style="width: 100%; left: 0; bottom: 10px;"></div>
                </div>
                """, unsafe_allow_html=True)
                
            with col2:
                st.markdown(f"""
                    <div style="position: relative;" class="hover-zoom">
                        <img src="data:image/png;base64,{data_science_image}" style="width: 100%; border-radius: 12px;">
                        <div class="laser-beam" style="width: 60%; left: 20%; top: 30%;"></div>
                    </div>
                """, unsafe_allow_html=True)
        
        with tab2:
            col1, col2 = st.columns([2, 3])
            with col1:
                st.markdown("""
                <div class="tech-card">
                    <h3 style="color: var(--primary);">Data Wrangling Techniques</h3>
                    <ul style="padding-left: 1.5rem; list-style-type: none;">
                        <li>• Handling Missing Data</li>
                        <li>• Data Transformation</li>
                        <li>• Feature Engineering</li>
                        <li>• Time Series Manipulation</li>
                        <li>• Advanced Pandas Techniques</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
                
            with col2:
                st.markdown(f"""
                <div style="position: relative;" class="hover-zoom">
                    <img src="{tech_images['big_data']}" style="width: 100%; border-radius: 12px;">
                    <div class="laser-beam" style="width: 60%; left: 20%; top: 30%;"></div>
                </div>
                """, unsafe_allow_html=True)
        
        with tab3:
            st.markdown("""
            <div class="tech-card">
                <h3 style="color: var(--primary);">Visualization Mastery</h3>
                <ul style="padding-left: 1.5rem; list-style-type: none;">
                    <li>• Matplotlib & Seaborn</li>
                    <li>• Plotly Interactive Viz</li>
                    <li>• Dashboard Creation</li>
                    <li>• Storytelling with Data</li>
                    <li>• Geospatial Visualization</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    elif selected == "🧠 ML":
        st.markdown("""
        <div style="text-align: center;">
            <h1 class="header-tech">MACHINE LEARNING TRACK</h1>
            <p style="font-size: 1.1rem; color: var(--primary-light);">From theory to production models</p>
        </div>
        """, unsafe_allow_html=True)
        
        tab1, tab2, tab3 = st.tabs(["🔍 Fundamentals", "👨‍🏫 Supervised", "🔮 Unsupervised"])
        
        with tab1:
            col1, col2 = st.columns([2, 3])
            with col1:
                st.markdown("""
                <div class="tech-card">
                    <h3 style="color: var(--primary);">ML Concepts</h3>
                    <ul style="padding-left: 1.5rem; list-style-type: none;">
                        <li>• Linear Regression</li>
                        <li>• Classification</li>
                        <li>• Decision Trees</li>
                        <li>• Ensemble Methods</li>
                        <li>• Model Evaluation</li>
                    </ul>
                    <div class="laser-beam" style="width: 100%; left: 0; bottom: 10px;"></div>
                </div>
                """, unsafe_allow_html=True)
                
            with col2:
                st.markdown(f"""
                <div style="position: relative;" class="hover-zoom">
                    <img src="{tech_images['machine_learning']}" style="width: 100%; border-radius: 12px;">
                    <div class="laser-beam" style="width: 60%; left: 20%; top: 40%;"></div>
                </div>
                """, unsafe_allow_html=True)
        
        with tab2:
            col1, col2 = st.columns([2, 3])
            with col1:
                st.markdown("""
                <div class="tech-card">
                    <h3 style="color: var(--primary);">Supervised Learning</h3>
                    <ul style="padding-left: 1.5rem; list-style-type: none;">
                        <li>• Linear Regression</li>     
                        <li>• Logistic Regression</li>     
                        <li>• KNN</li>    
                        <li>• Random Forests</li>
                        <li>• SVM</li>
                        <li>• Decision Tree</li>
                        <li>• XGBoost</li>  
                    </ul>
                </div>
                """, unsafe_allow_html=True)
                
            with col2:
                st.markdown(f"""
                <div style="position: relative;" class="hover-zoom">
                    <img src="{tech_images['neural_network']}" style="width: 100%; border-radius: 12px;">
                    <div class="laser-beam" style="width: 60%; left: 20%; top: 30%;"></div>
                </div>
                """, unsafe_allow_html=True)
        
        with tab3:
            st.markdown("""
            <div class="tech-card">
                <h3 style="color: var(--primary);">Unsupervised Learning</h3>
                <ul style="padding-left: 1.5rem; list-style-type: none;">
                    <li>• Clustering (K-Means)</li>
                    <li>• Dimensionality Reduction</li>
                    <li>• Anomaly Detection</li>
                    <li>• Association Rules</li>
                    <li>• Real-world Applications</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    elif selected == "🕸️ Deep Learning":
        st.markdown("""
        <div style="text-align: center;">
            <h1 class="header-tech">DEEP LEARNING TRACK</h1>
            <p style="font-size: 1.1rem; color: var(--primary-light);">
                Master deep models, language understanding, and real-world deployment
            </p>
        </div>
        """, unsafe_allow_html=True)

        tab1, tab2, tab3 = st.tabs(["🧠 Core Concepts", "🚀 Architectures & Transformers", "🔧 Applications"])

        with tab1:
            col1, col2 = st.columns([2, 3])
            with col1:
                st.markdown("""
                <div class="tech-card">
                    <h3 style="color: var(--primary);">Core Concepts</h3>
                    <ul style="padding-left: 1.5rem; list-style-type: none;">
                        <li>• Perceptrons</li>
                        <li>• Activation Functions</li>
                        <li>• Forward & Backward Propagation</li>
                        <li>• Loss Functions</li>
                        <li>• Optimization (SGD, Adam)</li>
                        <li>• Tokenization & Preprocessing</li>
                        <li>• Word Embeddings (Word2Vec, GloVe)</li>
                        <li>• LLM Models</li>
                        <li>• Prompt Engineering</li>
                    </ul>
                    <div class="laser-beam" style="width: 100%; left: 0; bottom: 10px;"></div>
                </div>
                """, unsafe_allow_html=True)
            with col2:
                st.markdown(f"""
                <div style="position: relative;" class="hover-zoom">
                    <img src="{tech_images['deep_learning']}" style="width: 100%; border-radius: 12px;">
                    <div class="laser-beam" style="width: 60%; left: 20%; top: 40%;"></div>
                </div>
                """, unsafe_allow_html=True)

        with tab2:
            st.markdown("""
            <div class="tech-card">
                <h3 style="color: var(--primary);">Architectures & Transformers</h3>
                <ul style="padding-left: 1.5rem; list-style-type: none;">
                    <li>• CNNs & RNNs</li>
                    <li>• LSTMs</li>
                    <li>• GANs</li>
                    <li>• Attention Mechanism</li>
                    <li>• Transformers</li>
                    <li>• BERT / GPT / RoBERTa</li>
                    <li>• Fine-tuning & Transfer Learning</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style="position: relative; margin-top: 2rem;" class="hover-zoom">
                <div class="laser-beam" style="width: 60%; left: 20%; top: 30%;"></div>
            </div>
            """, unsafe_allow_html=True)

        with tab3:
            st.markdown("""
            <div class="tech-card">
                <h3 style="color: var(--primary);">Applications & Deployment</h3>
                <ul style="padding-left: 1.5rem; list-style-type: none;">
                    <li>• Text Classification</li>
                    <li>• Sentiment Analysis</li>
                    <li>• Named Entity Recognition</li>
                    <li>• Chatbots</li>
                    <li>• Model Saving & Loading</li>
                    <li>• FastAPI & Flask APIs</li>
                    <li>• Real-time Inference</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style="position: relative; margin-top: 2rem;" class="hover-zoom">
                <div class="laser-beam" style="width: 60%; left: 20%; top: 30%;"></div>
            </div>
            """, unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; margin-top: 3rem; border-top: 1px solid var(--primary); padding-top: 1rem;">
    <p style="color: var(--primary-light); font-size: 0.9rem;">TECH TREK AI ACADEMY © 2025 | ALL SYSTEMS OPERATIONAL</p>
    <div style="font-size: 2rem;">
        <span style="color: var(--primary);">🚀</span>
        <span style="color: var(--primary-light);">⚡</span>
        <span style="color: var(--primary);">🤖</span>
    </div>
</div>
""", unsafe_allow_html=True)
