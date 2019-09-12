import os
import numpy as np
import shutil

# # Creating Train / Val / Test folders (One time use)

def split_dataset_one_time(root_dir , valid_size, test_size , train_path , valid_path , test_path):
    

    class_names = os.listdir(root_dir)

    #print(class_names)
    for single_class in class_names:
        try :


            os.makedirs(os.path.join( train_path , single_class))
            os.makedirs(os.path.join( valid_path , single_class))
            os.makedirs(os.path.join( test_path , single_class))


            train_single_path = os.path.join( train_path , single_class)
            test_single_path = os.path.join( test_path , single_class)
            valid_single_path = os.path.join( valid_path , single_class)
        except FileExistsError:
            pass
        
        single_full_list = os.listdir(os.path.join(root_dir , single_class))
        #print(single_full_list[0])

        num_examples_per_class = len(single_full_list)
        indices = list(range(num_examples_per_class))
        split_valid = int(np.floor(valid_size * num_examples_per_class))
        split_test = int(np.floor(test_size * num_examples_per_class)) + split_valid
        np.random.shuffle(indices)
        train_idx, valid_idx , test_idx = indices[split_test:], indices[:split_valid] , indices[split_valid:split_test]

        #print(train_idx[:5])
        single_full_list_np = np.array(single_full_list)
        train_list , valid_list , test_list = single_full_list_np[train_idx].tolist() , single_full_list_np[valid_idx].tolist() , single_full_list_np[test_idx].tolist()

        #print(len(train_list) , len(valid_list) , len(test_list) , len(single_full_list))



        for name in train_list:
            #print(os.path.join(root_dir , single_class , name) , train_single_path)
            shutil.move( os.path.join(root_dir , single_class , name) , train_single_path)

        for name in valid_list:
            #print(os.path.join(root_dir , single_class , name) , valid_single_path)
            shutil.move(os.path.join(root_dir , single_class , name) ,valid_single_path)

        for name in test_list:
            #print(os.path.join(root_dir , single_class , name) , test_single_path)
            shutil.move(os.path.join(root_dir , single_class , name), test_single_path)

