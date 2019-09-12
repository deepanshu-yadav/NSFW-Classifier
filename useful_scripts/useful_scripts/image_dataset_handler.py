import os
import torch
from torch.utils.data.dataset import Dataset
from torch.utils.data import DataLoader
import numpy as np
import os
from PIL import Image




def create_list_file_in_directory(datadir):
    i = 0 
    os.remove(os.path.join(datadir,'data.txt'))
    for single_label in os.listdir(datadir):
        single_full_list = os.listdir(os.path.join(datadir , single_label))
        for file_name in single_full_list:
            file = open( os.path.join(datadir,'data.txt')  ,'a')
            file.write(  '{}   {} \n'.format(os.path.join( single_label , file_name) , str(i) )  )
            file.close()
        i += 1




class DriveData(Dataset):
    __xs = []
    __ys = []

    def __init__(self, folder_dataset, transform=None , resize_tuple = (224, 224)):
        self.transform = transform
        self.resize_tuple = resize_tuple
        # Open and load text file including the whole training data
        with open( os.path.join(folder_dataset , "data.txt" ) ) as f:
            for line in f:
                # Image path
                self.__xs.append( os.path.join( folder_dataset ,line.split()[0]) )        
                # Steering wheel label
                self.__ys.append(np.float32(line.split()[1]))

    # Override to give PyTorch access to any image on the dataset
    def __getitem__(self, index):
        img = Image.open(self.__xs[index])
        img = img.convert('RGB')
        #img= img.resize( self.resize_tuple  )
        if self.transform is not None:
            img = self.transform(img)

        # Convert image and label to torch tensors
        img = torch.from_numpy(np.asarray(img))
        label = torch.from_numpy(np.asarray(self.__ys[index]).reshape([1,1]))
        return img, label

    # Override to give PyTorch size of dataset
    def __len__(self):
        return len(self.__xs)
        
        
def build_image_dataset(datadir  , batch_size=10, shuffle=True, num_workers=1 , transform=None , resize_tuple = (224, 224)  ):
    create_list_file_in_directory(datadir)
    dset_created = DriveData(datadir,transform , resize_tuple)

    #img , label = dset_train.__getitem__(0)

    data_loader = DataLoader(dset_created, batch_size=batch_size, shuffle=shuffle, num_workers=num_workers)
    return data_loader
