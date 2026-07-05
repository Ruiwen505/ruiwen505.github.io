import struct
import random

input_file = 'Assets/merged_result_20260131_1_dalu21p5k_CutResult.ply'
output_file = 'Assets/merged_result_colored.ply'

with open(input_file, 'rb') as f:
    lines = []
    while True:
        line = f.readline().decode('ascii')
        lines.append(line)
        if line.strip() == 'end_header':
            break

    # modify header
    new_lines = []
    for line in lines:
        if line.strip() == 'end_header':
            new_lines.append('property uchar red\n')
            new_lines.append('property uchar green\n')
            new_lines.append('property uchar blue\n')
            new_lines.append('end_header\n')
        else:
            new_lines.append(line)

    vertex_count = 0
    for line in lines:
        if line.startswith('element vertex'):
            vertex_count = int(line.split()[2])

    data = f.read()

# Generate some colors for instances
colors = {}
def get_color(instance_id):
    if instance_id not in colors:
        if instance_id == 0:
            colors[instance_id] = (100, 100, 100) # ground or unassigned
        else:
            colors[instance_id] = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
    return colors[instance_id]

# Struct format: 3 floats, 2 shorts = 16 bytes
in_fmt = '<fffhh'
in_size = struct.calcsize(in_fmt)

out_fmt = '<fffhhBBB'
out_size = struct.calcsize(out_fmt)

out_data = bytearray(vertex_count * out_size)

for i in range(vertex_count):
    offset = i * in_size
    vertex = struct.unpack_from(in_fmt, data, offset)
    
    x, y, z, inst, sem = vertex
    
    r, g, b = get_color(inst)
    
    out_offset = i * out_size
    struct.pack_into(out_fmt, out_data, out_offset, x, y, z, inst, sem, r, g, b)

with open(output_file, 'wb') as f:
    for line in new_lines:
        f.write(line.encode('ascii'))
    f.write(out_data)

print(f"Successfully converted {vertex_count} vertices. Output saved to {output_file}")
