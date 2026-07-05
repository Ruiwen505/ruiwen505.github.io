import re
import os

source_file = "lidar_carbon_landing_with_ground_lidar.html"
target_file = "proof.html"

with open(source_file, "r", encoding="utf-8") as f:
    html = f.read()

# Extract header and css up to </header>
header_match = re.search(r'(.*?</header>)', html, re.DOTALL)
header_part = header_match.group(1) if header_match else ""

# Extract everything from <footer> to the end, EXCLUDING the three.js script for now
# We will inject our own three.js script
footer_match = re.search(r'(<footer>.*?)<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js', html, re.DOTALL)
if footer_match:
    footer_part = footer_match.group(1)
else:
    # fallback
    footer_match = re.search(r'(<footer>.*?)</body>', html, re.DOTALL)
    footer_part = footer_match.group(1) + "</body>\n</html>"

images = [
    "Assets/results/Output_Lidar-20260705T091327Z-3-001/Screenshot 2026-05-24 at 10.25.37.png",
    "Assets/results/Output_Lidar-20260705T091327Z-3-001/Screenshot 2026-05-24 at 11.23.11.png",
    "Assets/results/Output_Lidar-20260705T091327Z-3-001/Screenshot 2026-05-24 at 11.24.06.png",
    "Assets/results/Output_Lidar-20260705T091327Z-3-001/Screenshot 2026-05-24 at 21.38.31.png",
    "Assets/results/Output_Lidar-20260705T091327Z-3-001/Screenshot 2026-07-04 at 13.53.54.png",
    "Assets/results/Output_Lidar-20260705T091327Z-3-001/Screenshot 2026-07-04 at 15.39.34.png",
    "Assets/results/Output_Lidar-20260705T091327Z-3-001/Screenshot 2026-07-04 at 15.42.30.png"
]

gallery_html = ""
for img in images:
    gallery_html += f'''
        <figure class="tech-figure" style="margin-bottom: 24px;">
          <img src="{img}" alt="Segmentation Result" style="height: auto; max-height: 500px; object-fit: contain; width: 100%; background: #000;">
        </figure>
'''

main_content = f'''
<main id="top">
  <section class="hero" style="padding: 60px 0 40px; background: var(--sand);">
    <div class="wrap">
      <div class="section-head" style="max-width: 900px;">
        <div class="eyebrow">Evidence & Validation</div>
        <h1>Past Works & Segmentation Results</h1>
        <p class="lead">Explore our processed forest LiDAR datasets, tree canopy segmentation experiments, and operational validation assets.</p>
      </div>
    </div>
  </section>

  <section style="padding: 40px 0; background: white;">
    <div class="wrap">
      <div class="section-head">
        <h2>Segmentation Evidence</h2>
        <p>Visual proofs of our vision LLM separating individual crowns and canopy layers.</p>
      </div>
      <div class="tech-grid" style="grid-template-columns: repeat(2, 1fr);">
        {gallery_html}
      </div>
    </div>
  </section>

  <section style="padding: 80px 0; background: var(--deep); color: white;">
    <div class="wrap">
      <div class="section-head" style="max-width: 100%;">
        <h2 style="color: white;">Full Airborne LiDAR Dataset</h2>
        <p style="color: rgba(255,255,255,0.7);">Our massive 636MB airborne dataset (Luftbild_2.ply) covering an entire forest region.</p>
        <button id="load-big-ply" class="btn" style="margin-top: 20px; cursor: pointer; background: var(--green); color: var(--deep);">Load Interactive 3D Model (Warning: 636MB Download)</button>
      </div>
      <div id="big-pointcloud-container" class="visual" style="display: none; height: 600px; margin-top: 40px; background: #000; border: 1px solid rgba(255,255,255,0.2);">
        <div id="big-pointcloud-loading" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: var(--green); font-weight: bold; z-index: 10;">Downloading 636MB Point Cloud... Please wait.</div>
      </div>
    </div>
  </section>
</main>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/loaders/PLYLoader.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
<script>
  document.getElementById('load-big-ply').addEventListener('click', function() {{
    this.style.display = 'none';
    const container = document.getElementById('big-pointcloud-container');
    container.style.display = 'block';
    
    // Initialize Three.js
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
    renderer.setSize(container.clientWidth, container.clientHeight);
    renderer.setPixelRatio(window.devicePixelRatio);
    container.appendChild(renderer.domElement);

    const controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.05;

    camera.position.set(0, 15, 15);
    camera.lookAt(0, 0, 0);

    // Load PLY
    const loader = new THREE.PLYLoader();
    loader.load('Assets/results/Output_Lidar-20260705T091327Z-3-001/Luftbild_2.ply', function(geometry) {{
      document.getElementById('big-pointcloud-loading').style.display = 'none';
      geometry.computeVertexNormals();
      geometry.center();

      let material;
      if (geometry.hasAttribute('color')) {{
        material = new THREE.PointsMaterial({{ size: 0.05, vertexColors: true }});
      }} else {{
        material = new THREE.PointsMaterial({{ size: 0.05, color: 0x1ed760 }});
      }}

      const points = new THREE.Points(geometry, material);
      geometry.computeBoundingBox();
      const size = geometry.boundingBox.getSize(new THREE.Vector3());
      const maxDim = Math.max(size.x, size.y, size.z);
      const scale = 10.0 / maxDim;
      points.scale.set(scale, scale, scale);
      points.rotation.x = -Math.PI / 2;

      scene.add(points);
    }});

    function animate() {{
      requestAnimationFrame(animate);
      controls.update();
      renderer.render(scene, camera);
    }}
    animate();

    window.addEventListener('resize', () => {{
      if (container.clientWidth > 0) {{
        camera.aspect = container.clientWidth / container.clientHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(container.clientWidth, container.clientHeight);
      }}
    }});
  }});
</script>
'''

with open(target_file, "w", encoding="utf-8") as f:
    f.write(header_part + "\n" + main_content + "\n" + footer_part + "\n</body>\n</html>")

print("Created proof.html successfully.")
