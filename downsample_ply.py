import struct

input_ply = r"Assets\results\Output_Lidar-20260705T091327Z-3-001\Luftbild_2.ply"
output_ply = r"Assets\results\Output_Lidar-20260705T091327Z-3-001\Luftbild_2_downsampled.ply"
sample_rate = 50

with open(input_ply, "rb") as f:
    header = []
    vertex_count = 0
    while True:
        line = f.readline()
        header.append(line)
        line_str = line.decode('utf-8').strip()
        if line_str.startswith("element vertex"):
            vertex_count = int(line_str.split()[2])
        if line_str == "end_header":
            break
    
    new_vertex_count = vertex_count // sample_rate
    
    # modify header
    new_header = []
    for hline in header:
        hline_str = hline.decode('utf-8')
        if hline_str.startswith("element vertex"):
            new_header.append(f"element vertex {new_vertex_count}\n".encode('utf-8'))
        else:
            new_header.append(hline)
            
    with open(output_ply, "wb") as out_f:
        for hline in new_header:
            out_f.write(hline)
            
        point_size = 29 # 6 floats + 5 uchars
        for i in range(new_vertex_count):
            # read sample_rate points, but we only need the first one, then skip the rest
            point_data = f.read(point_size)
            if not point_data:
                break
            out_f.write(point_data)
            # skip the next (sample_rate - 1) points
            f.seek(point_size * (sample_rate - 1), 1)

print(f"Downsampled from {vertex_count} to {new_vertex_count} points.")
