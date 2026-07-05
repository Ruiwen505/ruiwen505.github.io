import re

file_path = "lidar_carbon_landing_with_ground_lidar.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update the header nav
old_nav = """        <div class="links">
          <a href="#vision">Vision</a>
          <a href="#proof">Technology</a>
          <a href="#roadmap">Roadmap</a>
          <a href="#contact">Contact</a>
        </div>"""
new_nav = """        <div class="links">
          <a href="#vision">Vision</a>
          <a href="#proof">Technology</a>
          <a href="#roadmap">Roadmap</a>
          <a href="proof.html" style="color: var(--green);">Proof</a>
          <a href="#contact">Contact</a>
        </div>"""

content = content.replace(old_nav, new_nav)

# 2. Update the steps section
old_steps_part1 = """        <div class="section-head">
          <h2>Already beyond concept.</h2>
          <p>The team brings validated point-cloud workflows, field acquisition capability, forestry domain knowledge, AI engineering, finance, and GIS visualization.</p>
        </div>"""
new_steps_part1 = """        <div class="section-head">
          <h2>Already beyond concept.</h2>
          <p>The team brings validated point-cloud workflows, field acquisition capability, forestry domain knowledge, AI engineering, finance, and GIS visualization.</p>
          <a href="proof.html" style="display:inline-block; margin-top:16px; color:var(--green); text-decoration:none; font-weight:500; font-size:17px; transition:opacity 0.2s;">Click here to learn more and see our past validations &rarr;</a>
        </div>"""

content = content.replace(old_steps_part1, new_steps_part1)

old_steps_part2 = """        <div class="steps">
          <div class="step"><div><h3>Processed forest LiDAR datasets</h3><p>Prior work includes airborne, drone, terrestrial, and handheld mobile LiDAR data across coniferous forest contexts.</p></div></div>
          <div class="step"><div><h3>Segmentation evidence</h3><p>Tree canopy and ground-reference segmentation experiments demonstrate a practical technical starting point.</p></div></div>
          <div class="step"><div><h3>Operational assets</h3><p>Partner access supports drone platforms, forest survey resources, calibration data, and recurring validation materials.</p></div></div>
        </div>"""
new_steps_part2 = """        <div class="steps">
          <a href="proof.html" class="step" style="text-decoration:none; color:inherit; display:flex; transition:all 0.2s; cursor:pointer;" onmouseover="this.style.transform='translateY(-2px)'; this.style.borderColor='rgba(30,215,96,.3)';" onmouseout="this.style.transform='none'; this.style.borderColor='var(--line)';"><div><h3>Processed forest LiDAR datasets</h3><p>Prior work includes airborne, drone, terrestrial, and handheld mobile LiDAR data across coniferous forest contexts.</p></div></a>
          <a href="proof.html" class="step" style="text-decoration:none; color:inherit; display:flex; transition:all 0.2s; cursor:pointer;" onmouseover="this.style.transform='translateY(-2px)'; this.style.borderColor='rgba(30,215,96,.3)';" onmouseout="this.style.transform='none'; this.style.borderColor='var(--line)';"><div><h3>Segmentation evidence</h3><p>Tree canopy and ground-reference segmentation experiments demonstrate a practical technical starting point.</p></div></a>
          <a href="proof.html" class="step" style="text-decoration:none; color:inherit; display:flex; transition:all 0.2s; cursor:pointer;" onmouseover="this.style.transform='translateY(-2px)'; this.style.borderColor='rgba(30,215,96,.3)';" onmouseout="this.style.transform='none'; this.style.borderColor='var(--line)';"><div><h3>Operational assets</h3><p>Partner access supports drone platforms, forest survey resources, calibration data, and recurring validation materials.</p></div></a>
        </div>"""

content = content.replace(old_steps_part2, new_steps_part2)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated lidar html successfully.")
