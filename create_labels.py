import os

###############################################################################
def extraxt_labels(file_path):
    
    #-- log --
    print(f'-- {file_path} ------------------------------------------')
    
    lbls = set()
    with open(file_path, "r") as file:
        for line in file:            
            if 'coco' in file_path:
                start_index = line.find('\'')
                end_index = line.find('\'', start_index + 1) 

                if start_index != -1 and end_index != -1:
                    lbl = line[start_index + 1:end_index]
                    lbl = lbl.strip().lower()
                    lbls.add(lbl)                    
            
            elif 'pascal' in file_path:
                lbl = line.strip().lower()
                lbls.add(lbl)                 
            
            elif 'image_net' in file_path:
                start_index = line.find('\'')
                end_index = line.find('\'', start_index + 1)
                if start_index != -1 and end_index != -1:
                    lbls_list = line[start_index + 1:end_index]
                    lbls_list = lbls_list.split(',')                    
                    
                    for lbl in lbls_list:                  
                        lbl = lbl.strip().lower()
                        lbls.add(lbl)                      
                
        
        return lbls
                
###############################################################################


###############################################################################
path = 'labels/'
file_name = ['coco.txt', 
         'pascal_voc.txt',
         'image_net.txt']

result_file = 'all_labels.txt'

all_lbls = set()
for file in file_name:    
    all_lbls = all_lbls.union(extraxt_labels(path + file))
    
print(len(all_lbls))

if os.path.exists(path + result_file):
    print(f'{result_file} exists, removing...')
    os.remove(path + result_file)
    
with open(path + result_file, "w") as file:
    for lbl in all_lbls:
        file.write(lbl + "\n")
        
print('Finished ;)')

    





