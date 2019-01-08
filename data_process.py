import pandas as pd
import os
def lat_all(loc_all,grid_sep):
    lat_sw = float(loc_all.split(',')[1])
    lat_ne = float(loc_all.split(',')[3])
    lat_list = []

    for i in range(0, int((lat_ne - lat_sw ) / grid_sep)):  # 网格大小，可根据区域内POI数目修改
        lat_list.append(lat_sw + grid_sep * i)
    lat_list.append(lat_ne)

    return lat_list
#产生纬度格
def lng_all(loc_all,grid_sep):
    lng_sw = float(loc_all.split(',')[0])
    lng_ne = float(loc_all.split(',')[2])
    lng_list = []
    for i in range(0, int((lng_ne - lng_sw ) / grid_sep)):
        lng_list.append(lng_sw + grid_sep * i)
    lng_list.append(lng_ne)

    return lng_list

def ls_com(loc_all,grid):
    l1 = sorted(grid[0],reverse=True)
    l2 = grid[1]
    ab_list = []
    for i1 in range(0, len(l1)):
        a = str(l1[i1])
        for i2 in range(0, len(l2)):
            b = str(l2[i2])
            ab = a + ',' + b
            ab_list.append(ab)
    return ab_list

def ls_row(loc_all,grid_sep):
    l1 = lat_all(loc_all,grid_sep[0])
    l2 = lng_all(loc_all,grid_sep[1])
    ls_com_v = ls_com(loc_all,[l1,l2])
    ls = []
    for n in range(0, len(l1) - 1):
        for i in range(0 + len(l2) * n, len(l2) + (len(l2)) * n - 1):
            b = ls_com_v[i+1]
            a = ls_com_v[i + len(l2) ]
            ab = a + ',' + b
            ab_list = ab.split(',')
            if (ab_list[0] < ab_list[2] and ab_list[1] < ab_list[3]):
                ls.append(ab)


    return ls
def save_grid(grid_loc,output_path):
    for line in grid_loc:
        with open(output_path, 'a') as track:
            track.write(line+'\n')
def create_grid(location,grid_num,output_path):
    lat_sw  = float(location.split(',')[1])
    lat_ne = float(location.split(',')[3])
    lng_sw = float(location.split(',')[0])
    lng_ne = float(location.split(',')[2])
    lat_sep = (lat_ne-lat_sw)/grid_num
    lng_sep = (lng_ne-lng_sw)/grid_num
    ls = ls_row(location,[lat_sep,lng_sep])
    save_grid(ls,output_path)

def create_child_grid(input_path,output_path,grid_num):
    grid = [] 
    with open(input_path) as track:
        contents = track.readlines()
        for line in contents:
            grid.append(line.rstrip())
    for loc in grid:
        loc = loc.split(',')
        loc = [loc[1],loc[0],loc[3],loc[2]]
        loc = ','.join(loc)
        create_grid(loc,grid_num,output_path)
if __name__ == '__main__':
    grid_beijing = 4
    grid_xian = 4
    beijing = "116.147282,39.740499,116.549722,40.052263"
    xian = "108.760608,34.124199,109.122805,34.382002"
    output_path1 = './file/grid_beijing.txt'
    output_path2 = './file/grid_xian.txt'
    create_grid(beijing, grid_beijing, output_path1)
    create_grid(xian, grid_xian, output_path2)
    output_beijing_1 = './file/grid_child_beijing.txt'
    output_xian_1 = './file/grid_child_xian.txt'
    input_beijing_1 = './file/grid_beijing.txt'
    input_xian_1 = './file/grid_xian.txt'
    create_child_grid(input_beijing_1,output_beijing_1,2)
    create_child_grid(input_xian_1,output_xian_1,2)