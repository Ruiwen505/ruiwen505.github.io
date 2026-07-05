import re

file_path = "proof.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the text
old_text = """        <h2 style="color: white;">Full Airborne LiDAR Dataset</h2>
        <p style="color: rgba(255,255,255,0.7);">Our massive 636MB airborne dataset (Luftbild_2.ply) covering an entire forest region.</p>
        <button id="load-big-ply" class="btn" style="margin-top: 20px; cursor: pointer; background: var(--green); color: var(--deep);">Load Interactive 3D Model (Warning: 636MB Download)</button>
      </div>
      <div id="big-pointcloud-container" class="visual" style="display: none; height: 600px; margin-top: 40px; background: #000; border: 1px solid rgba(255,255,255,0.2);">
        <div id="big-pointcloud-loading" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: var(--green); font-weight: bold; z-index: 10;">Downloading 636MB Point Cloud... Please wait.</div>"""

new_text = """        <h2 style="color: white;">SfM Point Cloud</h2>
        <p style="color: rgba(255,255,255,0.7);">SfM from 360 cam metashape point cloud.</p>
      </div>
      <div id="big-pointcloud-container" class="visual" style="display: block; height: 600px; margin-top: 40px; background: #000; border: 1px solid rgba(255,255,255,0.2);">
        <div id="big-pointcloud-loading" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: var(--green); font-weight: bold; z-index: 10;">Loading Point Cloud...</div>"""

content = content.replace(old_text, new_text)

# Replace JS logic so it just runs without the button click
# Specifically, we remove:
# document.getElementById('load-big-ply').addEventListener('click', function() {
#     this.style.display = 'none';
#     const container = document.getElementById('big-pointcloud-container');
#     container.style.display = 'block';
# And the closing brace at the end.

js_old = """  document.getElementById('load-big-ply').addEventListener('click', function() {
    this.style.display = 'none';
    const container = document.getElementById('big-pointcloud-container');
    container.style.display = 'block';"""

js_new = """  (function() {
    const container = document.getElementById('big-pointcloud-container');"""

content = content.replace(js_old, js_new)

js_old_ply = "'Assets/results/Output_Lidar-20260705T091327Z-3-001/Luftbild_2.ply'"
js_new_ply = "'Assets/results/Output_Lidar-20260705T091327Z-3-001/Luftbild_2_downsampled.ply'"

content = content.replace(js_old_ply, js_new_ply)

js_end_old = """    });
  });
</script>"""

js_end_new = """    });
  })();
</script>"""

content = content.replace(js_end_old, js_end_new)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("proof.html updated successfully.")
