from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import sys
from classifier import training


class Train_face:
    def __init__(self):
        print('Train_face 실행')

    def run(self):
        datadir = './aligned_img'
        modeldir = './model/20180402-114759.pb'
        #modeldir = './model/20170511-185253.pb'

        classifier_filename = './class/classifier.pkl'


        # classifier_filename = 'encodings/encodings.pkl'


        print ("Training Start")
        obj=training(datadir,modeldir,classifier_filename)
        get_file=obj.main_train()
        print('Saved classifier model to file "%s"' % get_file)
        print("Train_face Done")
