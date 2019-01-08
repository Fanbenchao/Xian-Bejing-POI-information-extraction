# Xian-Bejing-POI-information-extraction
using web crawler obtain the POI information toward specific area is useful. In this repository, I will show a demo obtain Xian and beijing POI information with Baidu map api.
  language: python3
  API: baidu map api http://lbsyun.baidu.com/
  Demo area: Xian and Beijing. You can change your interested area in the data_process.py
  data_process.py: Pre-process the input area bound. In order to record the checkpoint the last run and use rectangle box search POI, I split the original area into 64 block. The first run, you will start from the 1th block and record the block running. The next running, you will run from the recording place.
  baidu_api.py: this file is used for using baidu map api.
  run.py: the main running file.
