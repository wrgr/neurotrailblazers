---
layout: dataset
title: "MouseConnects Dataset - Complete Hippocampal Connectome"
---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MouseConnects Dataset - Complete Hippocampal Connectome</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #fff;
        }

        .gradient-bg {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            position: relative;
            overflow: hidden;
        }

        .gradient-bg::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grid" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M 10 0 L 0 0 0 10" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="0.5"/></pattern></defs><rect width="100" height="100" fill="url(%23grid)"/></svg>');
            opacity: 0.3;
        }

        .hero-section {
            padding: 4rem 0;
            display: flex;
            align-items: center;
            position: relative;
            z-index: 1;
        }

        .hero-content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4rem;
            align-items: center;
        }

        .hero-badge {
            background: rgba(255,255,255,0.15);
            backdrop-filter: blur(10px);
            padding: 0.5rem 1rem;
            border-radius: 25px;
            font-size: 0.9rem;
            margin-bottom: 1.5rem;
            display: inline-block;
        }

        .hero-text h1 {
            font-size: 4rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            background: linear-gradient(45deg, #fff, #f0f8ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .hero-subtitle {
            font-size: 1.5rem;
            margin-bottom: 1rem;
            opacity: 0.9;
        }

        .hero-description {
            font-size: 1.1rem;
            margin-bottom: 2rem;
            opacity: 0.8;
            line-height: 1.7;
        }

        .hero-title-impact {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }

        .hero-title-impact span {
            font-weight: 400;
            font-size: 1.5rem;
        }

        .hero-description-box {
            background: rgba(255,255,255,0.15);
            backdrop-filter: blur(10px);
            padding: 1rem;
            border-radius: 8px;
            max-width: 700px;
            margin-bottom: 1rem;
        }

        .hero-actions {
            display: flex;
            gap: 1rem;
        }

        .btn {
            padding: 1rem 2rem;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
            border: none;
            cursor: pointer;
        }

        .btn-primary {
            background: white;
            color: #667eea;
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        }

        .btn-secondary {
            background: transparent;
            color: white;
            border: 2px solid white;
        }

        .btn-secondary:hover {
            background: white;
            color: #667eea;
        }

        .hero-visual {
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .connectome-preview {
            width: 400px;
            height: 400px;
            position: relative;
            border-radius: 50%;
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            border: 2px solid rgba(255,255,255,0.2);
            display: flex;
            align-items: center;
            justify-content: center;
            animation: float 6s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
        }

        .hippocampus {
            width: 200px;
            height: 120px;
            background: linear-gradient(45deg, #ff6b6b, #feca57);
            border-radius: 50px;
            position: relative;
            animation: pulse 4s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); opacity: 0.8; }
            50% { transform: scale(1.1); opacity: 1; }
        }

        .data-streams {
            position: absolute;
            width: 100%;
            height: 100%;
        }

        .stream {
            position: absolute;
            width: 2px;
            height: 100px;
            background: linear-gradient(to bottom, rgba(255,255,255,0.8), transparent);
            animation: stream 3s linear infinite;
        }

        .stream-1 {
            top: 20%;
            left: 30%;
            animation-delay: 0s;
        }

        .stream-2 {
            top: 40%;
            right: 25%;
            animation-delay: 1s;
        }

        .stream-3 {
            bottom: 30%;
            left: 60%;
            animation-delay: 2s;
        }

        @keyframes stream {
            0% { opacity: 0; transform: translateY(20px); }
            50% { opacity: 1; }
            100% { opacity: 0; transform: translateY(-20px); }
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        .project-overview {
            padding: 6rem 0;
        }

        .overview-grid {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 4rem;
        }

        .overview-main h2 {
            font-size: 2.5rem;
            margin-bottom: 1.5rem;
            color: #2c3e50;
        }

        .overview-main p {
            font-size: 1.1rem;
            margin-bottom: 2rem;
            color: #5a6c7d;
        }

        .key-innovations,
        .scientific-impact {
            margin-bottom: 3rem;
        }

        .key-innovations h3,
        .scientific-impact h3 {
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: #34495e;
        }

        .key-innovations ul,
        .scientific-impact ul {
            list-style: none;
        }

        .key-innovations li,
        .scientific-impact li {
            margin-bottom: 1rem;
            padding-left: 1.5rem;
            position: relative;
        }

        .key-innovations li::before,
        .scientific-impact li::before {
            content: '→';
            position: absolute;
            left: 0;
            color: #667eea;
            font-weight: bold;
        }

        .overview-stats {
            display: grid;
            gap: 2rem;
        }

        .stat-highlight {
            background: linear-gradient(135deg, #f8f9ff, #e8f0fe);
            padding: 2rem;
            border-radius: 12px;
            text-align: center;
            border: 1px solid #e0e8f7;
        }

        .stat-value {
            font-size: 2.5rem;
            font-weight: 700;
            color: #667eea;
            margin-bottom: 0.5rem;
        }

        .stat-label {
            font-size: 1.1rem;
            font-weight: 600;
            color: #34495e;
            margin-bottom: 0.5rem;
        }

        .stat-desc {
            font-size: 0.9rem;
            color: #7f8c8d;
        }

        .technology-section {
            padding: 6rem 0;
            background: #f8f9fa;
        }

        .technology-section h2 {
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 3rem;
            color: #2c3e50;
        }

        .tech-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 2rem;
        }

        .tech-card {
            background: white;
            padding: 2.5rem;
            border-radius: 12px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
            transition: transform 0.3s ease;
        }

        .tech-card:hover {
            transform: translateY(-5px);
        }

        .tech-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
        }

        .tech-card h3 {
            font-size: 1.3rem;
            margin-bottom: 1rem;
            color: #34495e;
        }

        .tech-card p {
            margin-bottom: 1.5rem;
            color: #5a6c7d;
        }

        .tech-card ul {
            list-style: none;
        }

        .tech-card li {
            margin-bottom: 0.5rem;
            padding-left: 1rem;
            position: relative;
            color: #6c757d;
        }

        .tech-card li::before {
            content: '✓';
            position: absolute;
            left: 0;
            color: #28a745;
        }

        .team-section {
            padding: 6rem 0;
        }

        .team-section h2 {
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 3rem;
            color: #2c3e50;
        }

        .team-institutions {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .institution {
            background: linear-gradient(135deg, #fff, #f8f9ff);
            padding: 2.5rem;
            border-radius: 12px;
            text-align: center;
            border: 1px solid #e0e8f7;
            transition: transform 0.3s ease;
        }

        .institution:hover {
            transform: translateY(-5px);
        }

        .institution-logo {
            font-size: 3rem;
            margin-bottom: 1rem;
        }

        .institution h3 {
            font-size: 1.3rem;
            margin-bottom: 0.5rem;
            color: #34495e;
        }

        .institution p {
            margin-bottom: 0.5rem;
            color: #5a6c7d;
        }

        .data-section {
            padding: 6rem 0;
            background: #f8f9fa;
        }

        .data-section h2 {
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 3rem;
            color: #2c3e50;
        }

        .data-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .data-card {
            background: white;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        }

        .data-card h3 {
            margin-bottom: 1rem;
            color: #34495e;
        }

        .footer {
            background: #2c3e50;
            color: white;
            padding: 3rem 0;
            text-align: center;
        }

        .footer-content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        .footer-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-bottom: 2rem;
        }

        .footer-section h4 {
            margin-bottom: 1rem;
            color: #ecf0f1;
        }

        .footer-section a {
            color: #bdc3c7;
            text-decoration: none;
            display: block;
            margin-bottom: 0.5rem;
        }

        .footer-section a:hover {
            color: #ecf0f1;
        }

        @media (max-width: 768px) {
            .hero-content {
                grid-template-columns: 1fr;
                text-align: center;
            }
            
            .hero-text h1 {
                font-size: 2.5rem;
            }
            
            .overview-grid {
                grid-template-columns: 1fr;
            }
            
            .connectome-preview {
                width: 300px;
                height: 300px;
            }
        }
    </style>
</head>
<body>
    <div class="hero-section gradient-bg">
        <div class="hero-content">
            <div class="hero-text">
                <div class="hero-badge">NIH BRAIN Initiative • $40M Project • 2023-2028</div>
                <h1 class="hero-title-impact">MouseConnects<span>: Complete Hippocampal Connectome</span></h1>
                <div class="hero-description-box">
                    <p class="hero-description">
                        One of the most ambitious connectomics project ever undertaken. A synapse-level reconstruction
                        of 10 mm³ of mouse hippocampal formation - revolutionizing our understanding of memory circuits.
                    </p>
                </div>
                <div class="hero-actions">
                    <a href="#explore-data" class="btn btn-primary btn-large">Explore the Data</a>
                    <a href="/datasets/workflow" class="btn btn-secondary btn-large">View Pipeline</a>
                </div>
            </div>
            <div class="hero-visual">
                <div class="connectome-preview">
                    <div class="brain-region hippocampus"></div>
                    <div class="data-streams">
                        <div class="stream stream-1"></div>
                        <div class="stream stream-2"></div>
                        <div class="stream stream-3"></div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="container">
        <div class="project-overview">
            <div class="overview-grid">
                <div class="overview-main">
                    <h2>Revolutionary Scale & Impact</h2>
                    <p>
                        MouseConnects represents a quantum leap in connectomics, targeting the mouse hippocampal 
                        formation - the brain region essential for memory formation and spatial navigation. This 
                        project will generate the first complete synaptic wiring diagram of a mammalian memory circuit.
                    </p>
                    
                    <div class="key-innovations">
                        <h3>Key Innovations</h3>
                        <ul>
                            <li><strong>Novel mSEM-IBEAM Technology:</strong> Combines multibeam electron microscopy with ion beam milling</li>
                            <li><strong>Distributed Imaging:</strong> Multiple sites working in parallel for unprecedented speed</li>
                            <li><strong>AI-Powered Reconstruction:</strong> State-of-the-art machine learning for automated segmentation</li>
                            <li><strong>Open Science:</strong> All data and tools freely available to the global research community</li>
                        </ul>
                    </div>
                    
                    <div class="scientific-impact">
                        <h3>Scientific Questions Addressed</h3>
                        <ul>
                            <li>How do hippocampal circuits encode spatial information and episodic memories?</li>
                            <li>What are the detailed microcircuit motifs underlying grid and place cell function?</li>
                            <li>How do different cell types contribute to memory formation and retrieval?</li>
                            <li>What circuit principles enable the hippocampus to act as a cognitive map?</li>
                        </ul>
                    </div>
                </div>

                <div class="overview-stats">
                    <div class="stat-highlight">
                        <div class="stat-value">10 mm³</div>
                        <div class="stat-label">Brain Volume</div>
                        <div class="stat-desc">50x larger than previous connectomes</div>
                    </div>
                    
                    <div class="stat-highlight">
                        <div class="stat-value">8 nm</div>
                        <div class="stat-label">Resolution</div>
                        <div class="stat-desc">Isotropic nanometer precision</div>
                    </div>
                    
                    <div class="stat-highlight">
                        <div class="stat-value">>10 PB</div>
                        <div class="stat-label">Data Size</div>
                        <div class="stat-desc">Unprecedented scale</div>
                    </div>
                    
                    <div class="stat-highlight">
                        <div class="stat-value">7 Sites</div>
                        <div class="stat-label">Global Team</div>
                        <div class="stat-desc">Leading institutions worldwide</div>
                    </div>
                </div>
            </div>
        </div>

        <div class="technology-section">
            <h2>Cutting-Edge Technology Stack</h2>
            <div class="tech-grid">
                <div class="tech-card">
                    <div class="tech-icon">🔬</div>
                    <h3>mSEM-IBEAM Imaging</h3>
                    <p>91-beam scanning electron microscopy combined with ion beam milling for automated blockface imaging at unprecedented scale.</p>
                    <ul>
                        <li>Two imaging sites: Harvard & Princeton</li>
                        <li>Automated wafer handling</li>
                        <li>Real-time quality monitoring</li>
                    </ul>
                </div>
                
                <div class="tech-card">
                    <div class="tech-icon">☁️</div>
                    <h3>Google Cloud Processing</h3>
                    <p>Massive-scale data processing using Google's cloud infrastructure for alignment, segmentation, and analysis.</p>
                    <ul>
                        <li>Flood-filling networks for neuron tracing</li>
                        <li>Automated synapse detection</li>
                        <li>Real-time collaborative proofreading</li>
                    </ul>
                </div>
                
                <div class="tech-card">
                    <div class="tech-icon">🧬</div>
                    <h3>Multi-Modal Integration</h3>
                    <p>Combining EM data with Patch-seq recordings, fMOST morphology, and transcriptomic cell typing.</p>
                    <ul>
                        <li>4,000+ Patch-seq recordings</li>
                        <li>Whole-brain fMOST reconstructions</li>
                        <li>Cross-modal cell type matching</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="team-section">
            <h2>World-Class Collaborative Team</h2>
            <div class="team-institutions">
                <div class="institution">
                    <div class="institution-logo">🏛️</div>
                    <h3>Harvard University</h3>
                    <p><strong>Jeff Lichtman, PI</strong></p>
                    <p>Sample preparation and imaging expertise with decades of connectomics experience</p>
                </div>
                
                <div class="institution">
                    <div class="institution-logo">🎓</div>
                    <h3>Princeton University</h3>
                    <p><strong>Sebastian Seung & David Tank</strong></p>
                    <p>mSEM imaging technology and deep learning algorithms for automated reconstruction</p>
                </div>
                
                <div class="institution">
                    <div class="institution-logo">☁️</div>
                    <h3>Google Research</h3>
                    <p><strong>Viren Jain</strong></p>
                    <p>Cloud-scale processing infrastructure and machine learning segmentation algorithms</p>
                </div>
                
                <div class="institution">
                    <div class="institution-logo">🧮</div>
                    <h3>MIT</h3>
                    <p><strong>Ila Fiete</strong></p>
                    <p>Circuit analysis, computational modeling, and theoretical frameworks for spatial coding</p>
                </div>
                
                <div class="institution">
                    <div class="institution-logo">🧠</div>
                    <h3>Allen Institute</h3>
                    <p><strong>Hongkui Zeng</strong></p>
                    <p>Patch-seq recordings, transcriptomic cell typing, and multi-modal data integration</p>
                </div>
                
                <div class="institution">
                    <div class="institution-logo">🔬</div>
                    <h3>University of Cambridge</h3>
                    <p><strong>Gregory Jefferis</strong></p>
                    <p>Data integration, analysis pipelines, and connectome interpretation methods</p>
                </div>
                
                <div class="institution">
                    <div class="institution-logo">🚀</div>
                    <h3>Johns Hopkins APL</h3>
                    <p><strong>William Gray-Roncal</strong></p>
                    <p>Connectome quality assurance, community training, and data dissemination</p>
                </div>
            </div>
        </div>

        <div class="data-section" id="explore-data">
            <h2>Dataset Access</h2>
            <div style="text-align: center; padding: 4rem 2rem;">
                <div style="background: linear-gradient(135deg, #f8f9ff, #e8f0fe); padding: 3rem; border-radius: 12px; border: 1px solid #e0e8f7; max-width: 600px; margin: 0 auto;">
                    <div style="font-size: 4rem; margin-bottom: 1rem;">🚧</div>
                    <h3 style="font-size: 1.8rem; margin-bottom: 1rem; color: #34495e;">Data Release Coming Soon</h3>
                    <p style="color: #5a6c7d; font-size: 1.1rem; line-height: 1.6;">
                        The MouseConnects dataset is currently in active development. Data release, interactive browsers, 
                        and analysis tools will be made available as the project progresses. Stay tuned for updates!
                    </p>
                    <div style="margin-top: 2rem;">
                        <a href="#" class="btn btn-primary" style="display: inline-block;">Get Notified</a>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <footer class="footer">
        <div class="footer-content">
            <div class="footer-grid">
                <div class="footer-section">
                    <h4>Project</h4>
                    <a href="#">About MouseConnects</a>
                    <a href="#">Publications</a>
                    <a href="#">Team</a>
                    <a href="#">News & Updates</a>
                </div>
                
                <div class="footer-section">
                    <h4>Data & Tools</h4>
                    <a href="#">Data Browser</a>
                    <a href="#">Download Center</a>
                    <a href="#">API Documentation</a>
                    <a href="#">Analysis Tools</a>
                </div>
                
                <div class="footer-section">
                    <h4>Community</h4>
                    <a href="#">Discussion Forum</a>
                    <a href="#">Tutorials</a>
                    <a href="#">Workshops</a>
                    <a href="#">Collaborate</a>
                </div>
                
                <div class="footer-section">
                    <h4>Support</h4>
                    <a href="#">Documentation</a>
                    <a href="#">FAQ</a>
                    <a href="#">Contact Us</a>
                    <a href="#">Cite This Work</a>
                </div>
            </div>
            
            <div style="border-top: 1px solid #34495e; padding-top: 2rem; margin-top: 2rem;">
                <p>&copy; 2025 MouseConnects Consortium. Funded by the NIH BRAIN Initiative. All data freely available under Creative Commons licensing.</p>
            </div>
        </div>
    </footer>
</body>
</html>