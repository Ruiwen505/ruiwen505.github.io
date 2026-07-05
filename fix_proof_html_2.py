import re

file_path = "proof.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Navigation Links
old_nav = """    <nav class="wrap" aria-label="Primary navigation">
      <a class="brand" href="#top"><span class="mark" aria-hidden="true"></span><span>CanopyLedger</span></a>
      <div class="navlinks">
        <a href="#platform">Platform</a>
        <a href="#technology">Technology</a>
        <a href="#market">Market</a>
        <a href="#proof">Proof</a>
        <a href="#roadmap">Roadmap</a>
      </div>
      <a class="btn secondary" href="#contact">Request pilot</a>
    </nav>"""

new_nav = """    <nav class="wrap" aria-label="Primary navigation">
      <a class="brand" href="lidar_carbon_landing_with_ground_lidar.html#top"><span class="mark" aria-hidden="true"></span><span>CanopyLedger</span></a>
      <div class="links">
        <a href="lidar_carbon_landing_with_ground_lidar.html#vision">Vision</a>
        <a href="lidar_carbon_landing_with_ground_lidar.html#proof">Technology</a>
        <a href="lidar_carbon_landing_with_ground_lidar.html#roadmap">Roadmap</a>
        <a href="proof.html" style="color: var(--green);">Proof</a>
        <a href="lidar_carbon_landing_with_ground_lidar.html#contact">Contact</a>
      </div>
    </nav>"""

# Sometimes it's class="links" instead of "navlinks" or vice versa. 
# We'll use regex to replace everything inside <nav class="wrap"...> ... </nav>
nav_pattern = re.compile(r'<nav class="wrap" aria-label="Primary navigation">.*?</nav>', re.DOTALL)
content = nav_pattern.sub(new_nav, content)


# 2. Update the text
old_text = """        <h2 style="color: white;">SfM Point Cloud</h2>
        <p style="color: rgba(255,255,255,0.7);">SfM from 360 cam metashape point cloud.</p>"""

new_text = """        <h2 style="color: white;">Downsampled pointcloud.</h2>"""
content = content.replace(old_text, new_text)

# 3. Update the rotation
# points.rotation.x = -Math.PI / 2;
old_rot = "points.rotation.x = -Math.PI / 2;"
new_rot = "points.rotation.x = -Math.PI / 4; // 45 degrees"
content = content.replace(old_rot, new_rot)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("proof.html updated successfully.")
