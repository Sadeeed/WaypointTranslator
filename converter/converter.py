import os
import random
import io
from django.conf import settings

wp_voxel_list = []
wp_xaero_list = []

possible_dimensions = ["overworld","the_nether","the_end"]

def convert_to_xaero(file):
    wp_voxel_list = [] # resetting both lists seems to fix the index out of range error 
    wp_xaero_list = []
    # filename = file.file.name
    filename = file.name
    # file = os.path.join(settings.MEDIA_ROOT, filename)
    # file_path = f'{settings.MEDIA_ROOT}{filename}_converted.txt'
    out_txt = {
        "overworld": '',
        "the_nether": '',
        "the_end": ''
    }
    for line in file:
        line = line.decode()
        wp_voxel_list.append(line.strip('\n'))
    # with open(file) as fp:
    #     for line in fp:
    #         wp_voxel_list.append(line.strip('\n'))

    # Voxel
    # name:name,x:x,z:z,y:y,enabled:boolean,red:r,green:g,blue:b,suffix:suffix,world:world,dimensions:dimension#

    # Xaero
    # waypoint:name:initial:x:y:z:color:disabled:type:set:rotated_teleport:rotation_yaw
    print(wp_voxel_list)
    for wp in wp_voxel_list[3:]:
        wp = wp.split(',')
        name = wp[0].split(':')[1]
        x = wp[1].split(':')[1]
        y = wp[3].split(':')[1]
        z = wp[2].split(':')[1]
        enabled = wp[4].split(':')[1]
        color = hex(random.randint(0, 0xf))[2:]
        dimensions = wp[10].split(':')[1]
        dimensions = dimensions.split('#')
        for dim_i in dimensions: # voxel waypoints can have multiple dimensions sometimes
            if dim_i in possible_dimensions: # added support for output of all 3 vanilla dimensions
                if enabled == 'true':
                    x_wp = f'waypoint:{name}:{name[0]}:{x}:{y}:{z}:{color}:false:0:gui.xaero_default:false:0:false\n'
                    out_txt[dim_i] = out_txt[dim_i] + x_wp
                elif enabled == 'false':
                    x_wp = f'waypoint:{name}:{name[0]}:{x}:{y}:{z}:{color}:true:0:gui.xaero_default:false:0:false\n'
                    out_txt[dim_i] = out_txt[dim_i] + x_wp

        # f = open(file_path, 'a')
        # f.write(out_txt)
        # f.close()
    # return out_txt, file_path
    return out_txt
