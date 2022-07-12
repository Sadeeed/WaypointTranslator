import os
import random

from django.conf import settings

wp_voxel_list = []
wp_xaero_list = []


def convert_to_xaero(file):
    # import pdb;pdb.set_trace()
    # filename = file.file.name
    filename = file.name

    file = os.path.join(settings.MEDIA_ROOT, filename)
    file_path = f'{settings.MEDIA_ROOT}/{filename}_converted.txt'
    out_txt = ''
    with open(file) as fp:
        for line in fp:
            wp_voxel_list.append(line.strip('\n'))

    # Voxel
    # name:name,x:x,z:z,y:y,enabled:boolean,red:r,green:g,blue:b,suffix:suffix,world:world,dimensions:dimension#

    # Xaero
    # waypoint:name:initial:x:y:z:color:disabled:type:set:rotated_teleport:rotation_yaw
    for wp in wp_voxel_list[3:]:
        wp = wp.split(',')
        name = wp[0].split(':')[1]
        x = wp[1].split(':')[1]
        y = wp[3].split(':')[1]
        z = wp[2].split(':')[1]
        enabled = wp[4].split(':')[1]
        color = hex(random.randint(0, 0xf))[2:]
        dimension = wp[10].split(':')[1]
        if enabled == 'true' and dimension == 'overworld#':
            x_wp = f'waypoint:{name}:{name[0]}:{x}:{y}:{z}:{color}:false:0:gui.xaero_default:false:0:false\n'
            out_txt = out_txt + x_wp
        elif enabled == 'false' and dimension == 'overworld#':
            x_wp = f'waypoint:{name}:{name[0]}:{x}:{y}:{z}:{color}:true:0:gui.xaero_default:false:0:false\n'
            out_txt = out_txt + x_wp

        # f = open(file_path, 'a')
        # f.write(out_txt)
        # f.close()
    return out_txt, file_path
