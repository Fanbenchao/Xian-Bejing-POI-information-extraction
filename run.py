import time
import codecs
import logging
from baidu_api import *
from data_process import *
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    print("开始爬取数据，请稍等...")
    start_time = time.time()
    input_beijing_1 = './file/grid_child_xian.txt'
    output_path ="./data/xian/"
    data_path = output_path+"xian.csv"
    grid = [] 
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    with open(input_beijing_1) as track:
        contents = track.readlines()
        for line in contents:
            grid.append(line.rstrip())
    if os.path.exists(output_path+'/checkpoint.txt'):
        with open(output_path+'/checkpoint.txt','r') as track:
            i = int(track.read().rstrip())
        
    else:
        i = 0
    num = []
    logger = logging.getLogger("baidu_api")
    
    if not os.path.exists(output_path):
            os.makedirs(output_path)
    sic = pd.read_csv('./file'+'/sic.csv')
    for j in range(i,len(grid)):
        print(grid[j])
        i += 1
        with open(output_path+'/checkpoint.txt', 'w') as track:
                track.write(str(i)+'\n')
        print("正在采集第%d个区域"%i)
        uri = u'酒店$休闲娱乐$金融$美食$医疗$交通设施$购物$生活服务$旅游景点$教育培训'
        par = urls(uri, grid[j])
        a = baidu_search(par,grid[j],sic)
        b = len(a)
        num.append(b)
        print("第%d个区域采集数量为%d"%(i,b))

        for ax in a:
            item = ','.join(ax)
            with codecs.open(data_path, 'a', encoding='utf8') as data:
                data.write(item+'\n')
            with open(output_path+'/ids.txt', 'a') as track:
                track.write(ax[0]+'\n')
            msg = "New Venue ! -> "+ax[1]
            logger.info(msg)
    end_time = time.time()
    print("爬取完毕，用时%.2f秒" % (end_time - start_time))