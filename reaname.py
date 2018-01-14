import os
path="H:\\work\\everyday\\2015-DQTEST"
path_all = os.listdir(path)
for path_all_obj in range(0,len(path_all)):
	this_path = os.path.join(path,path_all[path_all_obj])
	if os.path.isfile(this_path):
		os.rename(this_path,this_path.lower())