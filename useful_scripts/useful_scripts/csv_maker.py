import os 
import csv
import re 
import numpy as np

def give_prediction_label(result_string):
    #x = re.match("[(.*)]", result_string)
    x = result_string[result_string.find('[')+1 : result_string.find(']')].split(',')
    x_float = [ float(xi) for xi in x ]
    ind = x_float.index(max(x_float))        
    
    return ind 



def make_results_csv( results_directory , csv_path , csv_file_name  , eval_image_path ):
    with open(os.path.join(csv_path , csv_file_name), mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)    
        writer.writerow(['Image_path', 'ground_truth_label', 'Predicted'])
        i = 0
        sorted_list = sorted(os.listdir(results_directory))
        for single_class in sorted_list:
            list_of_files = os.listdir(os.path.join( results_directory , single_class ))
            for img_result in list_of_files:
                result_file = open(  os.path.join( results_directory , single_class , img_result )  , 'r')
                result_string = result_file.read()
                prediction_val = give_prediction_label(result_string)
                #print(result_string.split(','))
                label = str(i)
                img_path = os.path.join( eval_image_path , single_class ,img_result[:-4] )
                writer.writerow([img_path, label , prediction_val  ])            
                result_file.close()
            #print(i)
            i += 1
#make_results_csv('analyze/analyze' , 'dump' , 'results.csv' , 'nsfw_dataset_test' )